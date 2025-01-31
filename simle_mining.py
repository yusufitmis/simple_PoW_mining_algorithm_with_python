from hashlib import sha256
import time

def _SHA256(val):
    return sha256(val.encode()).hexdigest()

def mine(transaction, previous_hash, difficulty):
    prefix_zeros = '0' * difficulty
    nonce = 0
    while True:
        nonce += 1
        val = transaction + previous_hash + str(nonce)
        hash = _SHA256(val)
        if(hash.startswith(prefix_zeros)):
            print("Nonce bulundu")
            return hash
        
def main():
    difficulty = 4
    transaction = '4f26a1ce5afae21e7d28cf7147db6edb4d7411d751fd93f9f9af1cdfcb1ff96f'
    previous_hash = 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb'
    start_time = time.time()
    print("mining başladı")
    hash = mine(transaction, previous_hash, difficulty)
    total_time = str(time.time() - start_time)
    print(f"Total Time = {total_time}")
    print(f"Hash = {hash}")
    
main()