#!/usr/bin/env python3

def vernam_cipher(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        encrypted_char = chr(ord(text[i]) ^ ord(key[i % len(key)]))
        encrypted_text += encrypted_char

    return encrypted_text.encode().hex()


text = "this is a message"
key = "lkdwnfwielfnsdlk"
    
ciphertext = vernam_cipher(text, key)
print("ciphertext: ", ciphertext)

plaintext = vernam_cipher(bytes.fromhex(ciphertext).decode(), key)
print("plaintext: ", plaintext)
