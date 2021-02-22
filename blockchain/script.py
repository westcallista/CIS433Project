from blockchain import Blockchain
  
block_one_transactions = {"sender":"Alice", "receiver": "US Government", "vote": "blue"}
block_two_transactions = {"sender": "Bob", "receiver":"US Government", "vote":"blue"}
block_three_transactions = {"sender":"Nate", "receiver":"US Government", "vote":"red"}
fake_transactions = {"sender": "Joe", "receiver":"US Government", "vote":"blue"}

print("beginning of script\n")
local_blockchain = Blockchain()
local_blockchain.print_blocks()
print("after blockchain...\n")
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()
local_blockchain.chain[2].transactions = fake_transactions
local_blockchain.validate_chain()

