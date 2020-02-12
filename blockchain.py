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
'''区块类结构'''
class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    # 新添加一个快
    def new_block(self):
        pass

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
        pass

    # get last block in blockchain
    @property
    def last_block(self):
        pass