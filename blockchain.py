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
'''区块类结构'''
class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        # 创世纪区块
        self.new_block(proof=100, previous_hash=1)

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
        block_string = json.dump(block, sort_keys=True).encode()
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

# 通过flask实现与其他节点的通信
# flask是轻量级的web server
app = Flask(__name__)

#  给服务器添加路由（api)
# 添加新的交易
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transactions"

# 挖矿（POW）
@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new block"
# 返回区块链信息
@app.route('/chain', methods=['GET'])
def full_chain():
    return 'full chain'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

