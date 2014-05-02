#-*- coding: utf-8 -*-
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from binascii import hexlify, unhexlify

iterations  = 14253
padding_size= 16

plaintext   = "Big brother is watching you"

pad = lambda s: s + (padding_size - len(s) % padding_size) *\
        chr(padding_size - len(s) % padding_size)
unpad = lambda s: s[:-s[-1]]
padding = lambda s : s + (padding_size - len(s) % padding_size)*\
        (padding_size - len(s) % padding_size)

def encrypt(text):
    salt        = get_random_bytes(16)
    passwd      = get_random_bytes(32)
    iv          = get_random_bytes(16)
    key         = PBKDF2(passwd, salt, dkLen=32, count=iterations)
    cipher      = AES.new(key, AES.MODE_CBC, iv)
    return (iv + cipher.encrypt(pad(text)))

def decrypt(ciphered, key, iv):
    return unpad(AES.new(key, AES.MODE_CBC, ciphered[:len(iv)]).decrypt(ciphered[len(iv):]))
print (hexlify(encrypt(plaintext)))
print (plaintext)


