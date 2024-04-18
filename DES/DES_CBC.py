#!/usr/bin/env python3

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

key_hex = '0e46c73c3f23c58e'
plaintext = 'La lunghezza di questa frase non è divisibile per 8'

key = bytes.fromhex(key_hex)
plaintext_bytes = plaintext.encode('utf-8')

pad_len = 8 - (len(plaintext_bytes) % 8)
padded_plaintext = pad(plaintext_bytes, 8, style='x923')

iv = get_random_bytes(8)
print("IV (hex):", iv.hex())

cipher = DES.new(key, DES.MODE_CBC, iv)
ciphertext = cipher.encrypt(padded_plaintext)
print("ciphertext (hex):", ciphertext.hex())