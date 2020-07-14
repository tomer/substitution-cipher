#!/usr/bin/env python3
import argparse
import string
import sys

"""
   Substition encryption/decryption algorithm 
   Tomer Cohen https://github.com/tomer/
"""

def Encrypt(message, key):
    return encrypt_decrypt(message, cipher_alphabet=key)

def Decrypt(message, key):
    return encrypt_decrypt(message, plaintext_alphabet=key)

def encrypt_decrypt(message, cipher_alphabet=None, plaintext_alphabet=None):
    if plaintext_alphabet == None: plaintext_alphabet = string.ascii_uppercase
    if cipher_alphabet == None: cipher_alphabet = string.ascii_uppercase

    cipher = ''
    for letter in message:
        if letter.isalpha():
            index = plaintext_alphabet.find(letter.upper())
            if index >= 0:
                if letter.isupper():
                    cipher += cipher_alphabet[index].upper()
                else: 
                    cipher += cipher_alphabet[index].lower()
        else: # not alpha
            cipher += letter
    return cipher

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="substitution cipher manager")
    parser.add_argument('action', choices=['encrypt', 'decrypt'])
    parser.add_argument('message', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('--key', help='26 characters encrytion key', default='JIECHSDUGFRVAWNQTYBZOLKMPX')
    args = parser.parse_args()

    with args.message as message:
        if args.action == 'decrypt':
            for line in message:
                print (Encrypt(line, args.key), end='')
        else:
            for line in message:
                print (Decrypt(line, args.key), end='')