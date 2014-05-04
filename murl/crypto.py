#-*- coding: utf-8 -*-
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from binascii import hexlify, unhexlify

iterations      = 14253
padding_size    = 16
iv_size         = 16

pad = lambda s: s + (padding_size - len(s) % padding_size) *\
        chr(padding_size - len(s) % padding_size)
unpad = lambda s: s[:-s[-1]]
padding = lambda s : s + (padding_size - len(s) % padding_size)*\
        (padding_size - len(s) % padding_size)

def encrypt(text):
    salt        = get_random_bytes(16)
    passwd      = get_random_bytes(32)
    iv          = get_random_bytes(iv_size)
    key         = PBKDF2(passwd, salt, dkLen=32, count=iterations)
    cipher      = AES.new(key, AES.MODE_CBC, iv)
    return (hexlify(iv + cipher.encrypt(pad(text))), key)

def decrypt(ciphered, key):
    data        = unhexlify(ciphered)
    iv          = data[:iv_size]
    ciphered    = data[iv_size:]
    return unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(ciphered))
