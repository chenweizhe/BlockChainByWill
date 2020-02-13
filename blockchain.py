# {
#     'index': 0,
#     'timestamp': '',
#     'transactions': [
#         {
#             'sender': '',
#             'recipient': '',
#             'amout': 5,
#         }
#     ],
#     'proof': '',
#     'previous_hash': '',
# }
from time import time
import hashlib
import json
from flask import Flask
from flask import jsonify
from flask import request
from uuid import uuid4
from urllib.parse import urlparse
import requests
from argparse import ArgumentParser
'''区块类结构'''
class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        # 保存节点信息  set集合中的元素是独一无二的 不可重复的 数组的元素是可以重复的
        self.nodes = set()

        # 创世纪区块
        self.new_block(proof=100, previous_hash=1)


    #  注册一个节点
    def register_node(self, address: str):
        # 地址形式一般是http://127.0.0.1:5001
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    # 检查链表是否合法
    def valid_chain(self, chain) -> bool:
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]

            # 不合法的第一种情况：块的哈希不等于计算出来的哈希 则这是一条虚假的链
            if block['previous_hash'] != self.hash(last_block):
                return False

            # 不合法的第二种情况：工作量证明不合格
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False
            last_block = block
            current_index += 1

        return True

    # 解决冲突 选择最长链
    def resolve_conflicts(self) -> bool:
        neighbours = self.nodes
        max_length = len(self.chain)
        new_chain = None

        for node in neighbours:
            response = requests.get(f'http://{node}/chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                if length > max_length and self.valid_chain(chain):
                    max_length= length
                    new_chain = chain

        if new_chain:
            self.chain = new_chain
            return True

        return False

    # 新添加一个快
    def new_block(self, proof, previous_hash = None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.last_block)
        }
        # 打包之后将交易清空
        self.current_transactions = []
        self.chain.append(block)

        return block


    # add new transcation
    def new_transaction(self, sender, recipient, amount) -> int:
        self.current_transactions.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount
            }
        )
        return self.last_block['index'] + 1
    # hash static function
    @staticmethod
    def hash(block):
        # 将block转化成一个字节数组
        block_string = json.dumps(block, sort_keys=True).encode()
        # 返回哈希之后的摘要信息
        return hashlib.sha256(block_string).hexdigest()

    # get last block in blockchain
    @property
    def last_block(self):
        return self.chain[-1]


    # 实现工作量证明
    def proof_of_work(self, last_proof: int) -> int:
        proof = 0
        # 验证哈希结果是否满足4个0开头
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        # print(proof)
        return proof

    def valid_proof(self, last_proof: int, proof: int) -> bool:
        # 转换并拼接成为字符串，再进行编码
        guess = f'{last_proof}{proof}'.encode()
        # 获取哈希之后的摘要
        guess_hash = hashlib.sha256(guess).hexdigest()

        # 验证guess_hash前四个字符是否为4个0 如果是就返回true 反之false
        # if guess_hash[0: 4] == '0000':
        #     return True
        # else:
        #     return  False
        # print(guess_hash)
        return guess_hash[0:4] == '0000'
        # 在现实生活中 比特币是以十八个0开头的 这个只是演示




'''======================================================================='''
# 通过flask实现与其他节点的通信
# flask是轻量级的web server
app = Flask(__name__)
# 实例化blockchain
blockchain = Blockchain()

# 使用uuid随机生成模拟节点的地址
node_identify = str(uuid4()).replace('-','')

#  给服务器添加路由（api)
# 添加新的交易
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender','recipient','amount']
    if values is None:
        return 'missing values', 400

    if not all(k in values for k in required):
        return 'missing values', 400
    index = blockchain.new_transaction(values['sender'],
                               values['recipient'],
                               values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

# 挖矿（POW）
@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    # 再添加一笔给自己的交易
    blockchain.new_transaction(sender='0',
                               recipient=node_identify,
                               amount=1)
    block = blockchain.new_block(proof, None)
    response = {
        'message': 'new block forged',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200

    return "We'll mine a new block"


# 返回区块链信息
@app.route('/chain', methods=['GET'])
def full_chain():
    reponse = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    # 将json转化成字符串
    return jsonify(reponse), 200

# 接受来自一个节点的请求 注册节点
@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return 'Error! please supply a valid list of nodes', 400
    for node in nodes:
        blockchain.register_node(node)
    response = {
        'message': 'new nodes have been added',
        'total_nodes': list(blockchain.nodes)
    }
    return jsonify(response), 201

# 解决冲突的请求
@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain was authoritative',
            'chain': blockchain.chain
        }
    return jsonify(response), 200

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('-p','--port',default=5000, type=int, help='port to listen to')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)

