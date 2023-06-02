import hashlib
import binascii
import hmac
import os
import secrets
import time

from bip32utils import BIP32Key
from mnemonic import Mnemonic

def generate_mnemonic():
    # Generating random entropy
    entropy = secrets.token_bytes(16)
    mnemonic = Mnemonic('english').to_mnemonic(entropy)
    return mnemonic

def generate_address(mnemonic):
    # Getting a seed from a mnemonic phrase
    seed = Mnemonic.to_seed(mnemonic)

    # Create a key BIP32
    root = BIP32Key.fromEntropy(seed)

    # Getting a public address
    address = root.Address()

    return address

def check_addresses(database_file, num_addresses):
    with open(database_file, 'r') as file:
        # Reading a database with addresses
        addresses = [line.strip() for line in file]

    found_addresses = []
    attempts = 0

    start_time = time.time()

    while len(found_addresses) < num_addresses:
        mnemonic = generate_mnemonic()
        address = generate_address(mnemonic)
        attempts += 1

        if address in addresses:
            found_addresses.append((mnemonic, address))
            # Create a file with a mnemonic phrase associated with the found address
            filename = f"found_mnemonic_{address}.txt"
            create_file_with_mnemonic(mnemonic, filename)

        # We display information about the state of the enumeration every 1000 attempts
        if attempts % 1000 == 0:
            elapsed_time = time.time() - start_time
            speed = attempts / elapsed_time
            print(f"Checked seed phrases: {attempts}, Found addresses: {len(found_addresses)}, Speed: {speed:.2f} attempts/sec")

    return found_addresses

def create_file_with_mnemonic(mnemonic, filename):
    with open(filename, 'w') as file:
        file.write(mnemonic)

# Usage example
num_addresses = 10  # Number of addresses to check
database_path = os.path.join(r'database.txt')
found_addresses = check_addresses(database_path, num_addresses)

print("Found addresses in the database:")
if found_addresses:
    for mnemonic, address in found_addresses:
        print("Mnemonic phrase:", mnemonic)
        print("Address:", address)
        print("---------------------------")
else:
    print("Addresses Not found.")