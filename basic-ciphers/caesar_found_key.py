#!/usr/bin/env python3

from caesar_enc_dec import decrypt

text = "khoor zruog"

for key in range(0, 26):
    translated = decrypt(text, key)
    print('Is this the key?! %s: %s' % (key, translated))
