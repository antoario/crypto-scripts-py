#!/usr/bin/env python3

import re

# Remove spaces and non-alphabetic characters and convert to uppercase
def prepare_input(text):
    text = re.sub(r'[^A-Za-z]+', '', text).upper()
    text = text.replace("J", "I")

    return text

# Initialize the matrix with the keyword and add the rest of the alphabet
def create_playfair_matrix(key):
    key = prepare_input(key)
    matrix = []

    for char in key:
        if char not in matrix:
            matrix.append(char)

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]

    return playfair_matrix

def find_char_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def encrypt_pair(matrix, pair):
    row1, col1 = find_char_position(matrix, pair[0])
    row2, col2 = find_char_position(matrix, pair[1])
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(matrix, pair):
    row1, col1 = find_char_position(matrix, pair[0])
    row2, col2 = find_char_position(matrix, pair[1])
    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def encrypt(plain_text, key):
    matrix = create_playfair_matrix(key)
    plain_text = prepare_input(plain_text)
    pairs = [plain_text[i:i+2] for i in range(0, len(plain_text), 2)]
    if len(pairs[-1]) == 1:
        pairs[-1] += 'X'
    encrypted_text = ''.join(encrypt_pair(matrix, pair) for pair in pairs)
    return encrypted_text

def decrypt(cipher_text, key):
    matrix = create_playfair_matrix(key)
    decrypted_text = ''.join(decrypt_pair(matrix, pair) for pair in zip(cipher_text[0::2], cipher_text[1::2]))
    return decrypted_text

key = "security"
plain_text = "buona giornata"
cipher_text = encrypt(plain_text, key)
print("Ciphertext:", cipher_text)
decrypted_text = decrypt(cipher_text, key)
print("Plaintext:", decrypted_text)
