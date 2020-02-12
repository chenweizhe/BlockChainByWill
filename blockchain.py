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