import datetime
from hashlib import sha256

red = 0
blue = 0

class Block:
  def __init__(self, transactions, previous_hash):
    self.time_stamp = datetime.datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    #self.red = 0
    #self.blue = 0
    self.nonce = 0
    self.hash = self.generate_hash()

  def generate_hash(self):
    block_header = str(self.time_stamp) + str(self.transactions) +str(self.previous_hash) + str(self.nonce)
    block_hash = sha256(block_header.encode())
    return block_hash.hexdigest()

  def print_contents(self):
    global red
    global blue
    print("timestamp:", self.time_stamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())
    print("previous hash:", self.previous_hash)
    if(self.transactions != []):
      print("vote color:", self.transactions["vote"])
      if(self.transactions["vote"] == "red"):
        red += 1
      else:
        blue +=1
    print("\n--------The Democrat candidate has " + str(blue) + " votes and the Republican candidate has " + str(red) + " votes.--------\n")


  """
  def vote_count(self):
    if(self.transactions != []):
      print("vote color:", self.transactions["vote"])
      if(self.transactions["vote"] == "red"):
        self.red += 1
      else:
        self.blue +=1
  """
