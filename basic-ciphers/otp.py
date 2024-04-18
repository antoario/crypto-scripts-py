#!/usr/bin/env python3

def xor(a, b):
  return bytes([x^y for x,y in zip(a,b)])

plaintext = "this is a secret mess"
key = "ewfbwlfksjfopesnfòdsk"

plaintext_bytes = plaintext.encode()
key_bytes = key.encode()
ciphertext_bytes = xor(plaintext_bytes, key_bytes)

print("plaintext (hex): " + plaintext_bytes.hex())
print("key (hex): " + key_bytes.hex())
print("ciphertext (hex): " + ciphertext_bytes.hex())
