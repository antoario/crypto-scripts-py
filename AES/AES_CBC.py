#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util import Padding

key = b'16_r4ndom_bytes!'

iv_hex = '7ceb9c2e8af7d9d4'
iv_bytes = bytes.fromhex(iv_hex)

c = 'f38caf2394a4d05e131930553a76913acfbaaa46065ee9f87ceb9c2e8af7d9d4'
c_bytes = Padding.pad(c.encode(), 16)

#cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
#ciphertext_bytes = cipher.encrypt(plaintext_bytes)

cipher = AES.new(key, AES.MODE_CBC, iv_bytes)
newplaintext_bytes = cipher.decrypt(c_bytes)

print(c_bytes.hex())
print(newplaintext_bytes.decode())
