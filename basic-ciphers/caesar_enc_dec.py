#!/usr/bin/env python3

def encrypt(plaintext, k):
  ciphertext = ""

  for i in range(len(plaintext)):
    c = plaintext[i]
    if c == " ":
      ciphertext += " "
    elif c.islower():
      x = ord(c) - 97
      enc = (x + k) % 26
      ciphertext += chr(enc + 97)
      
  return ciphertext


def decrypt(ciphertext, k):
  plaintext = ""

  for i in range(len(ciphertext)):
    p = ciphertext[i]
    if p == " ":
      plaintext += " "
    elif p.islower():
      x = ord(p) - 97                 
      enc = (x - k) % 26
      plaintext += chr( enc + 97 )    

  return plaintext


# insert data below
text = "hello world"  
idx = 3

#print("Ciphertext: " + encrypt(text, idx)) # remove previous comment if you want to encrypt
#print("Plaintext: " + decrypt(text, idx)) # remove previous comment if you want to decrypt