import hashlib
import time
import json
from colorama import init, Fore, Style

init()

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    timestamp = time.time()
    hash = calculate_hash(0, "0", timestamp, "Genesis Block")
    return Block(0, "0", timestamp, "Genesis Block", hash)

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

def print_block(block):
    block_info = {
        "index": block.index,
        "previous_hash": block.previous_hash,
        "timestamp": block.timestamp,
        "data": block.data,
        "hash": block.hash
    }
    print(Fore.CYAN + json.dumps(block_info, indent=2) + Style.RESET_ALL)

def main():
    print(Fore.YELLOW + "=== Blockchain Simülasyonuna Hoş Geldiniz! ===" + Style.RESET_ALL)
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    print(Fore.GREEN + "Genesis Blok oluşturuldu:" + Style.RESET_ALL)
    print_block(blockchain[0])
    time.sleep(1)

    while True:
        print(Fore.YELLOW + "\nYeni bir işlem eklemek ister misiniz? (e/h)" + Style.RESET_ALL)
        choice = input().lower()
        if choice != 'e':
            break

        data = input(Fore.MAGENTA + "İşlem verisini girin (örneğin, 'Ali -> Veli: 10 BTC'): " + Style.RESET_ALL)
        if not data:
            data = f"Transaction {previous_block.index + 1}"

        new_block = create_new_block(previous_block, data)
        blockchain.append(new_block)
        previous_block = new_block

        print(Fore.GREEN + f"\nBlok #{new_block.index} eklendi. Hash: {new_block.hash}" + Style.RESET_ALL)
        print_block(new_block)
        time.sleep(1)

    print(Fore.YELLOW + "\n=== Son Blockchain Durumu ===" + Style.RESET_ALL)
    for block in blockchain:
        print_block(block)

if __name__ == "__main__":
    main()