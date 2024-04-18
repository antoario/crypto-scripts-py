#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def generate_aes_key_and_iv():
    key = get_random_bytes(32)
    iv = get_random_bytes(16)
    
    return key.hex(), iv.hex()

key, iv = generate_aes_key_and_iv()
print("key generated (256): ", key)    
print("IV generated: ", iv)
