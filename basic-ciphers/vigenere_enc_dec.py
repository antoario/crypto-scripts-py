#!/usr/bin/env python3

def encrypt(text, key):
    result = ""
    key_length = len(key)
    for i in range(len(text)):
        if text[i].isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A') if key_char.isupper() else ord(key_char) - ord('a')
            if text[i].isupper():
                result += chr((ord(text[i]) + shift - 65) % 26 + 65)
            elif text[i].islower():
                result += chr((ord(text[i]) + shift - 97) % 26 + 97)
        else:
            result += text[i]
    return result

def decrypt(text, key):
    result = ""
    key_length = len(key)
    for i in range(len(text)):
        if text[i].isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A') if key_char.isupper() else ord(key_char) - ord('a')
            if text[i].isupper():
                result += chr((ord(text[i]) - shift - 65) % 26 + 65)
            elif text[i].islower():
                result += chr((ord(text[i]) - shift - 97) % 26 + 97)
        else:
            result += text[i]
    return result


text = "this is a message"
key = "lkdwnfwielfnsdlk"
    
#print("ciphertext: ", encrypt(text, key)) # remove previous comment if you want to encrypt
#print("plaintext: ", decrypt(text, key)) # remove previous comment if you want to decrypt