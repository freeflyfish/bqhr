# coding:utf-8

import sys
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        cryptor = AES.new(text, self.mode, self.key)
        length = 16
        count = len(text)
        if count % length != 0:
            add = length - (count % length)
        else:
            add = 0
            text = text + (b'\0' * add)
            self.ciphertext = cryptor.encrypt(text)
            return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip(b'\0')


if __name__ == '__main__':
    pc = prpcrypt(b'keyskeyskeyskeys')  # 初始化密钥
    e = pc.encrypt(b"0123456789ABCDEF")
    d = pc.decrypt(e)
    print(e, d)
    e = pc.encrypt(b"0000000000000000")
    d = pc.decrypt(e)
    print(e, d)
