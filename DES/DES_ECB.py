#!/usr/bin/env python3

from Crypto.Cipher import DES

key = 'abcdefgh'
key_bytes = key.encode('utf-8')

def pad(text):
        while len(text) % 8 != 0:
            text += b'\0'
        return text

des = DES.new(key_bytes, DES.MODE_ECB)

text = 'this is a message'
padded_text = pad(text.encode())

ciphertext = des.encrypt(padded_text)
print("ciphertext (hex): " + ciphertext.hex())
print("plaintext: " + des.decrypt(ciphertext).decode())