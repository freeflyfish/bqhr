# coding:utf-8

import base64


import hashlib
data = b'scx1123'
hash_new = hashlib.md5(data) #或hashlib.md5()
hash_value = hash_new.hexdigest() #生成40位(sha1)或32位(md5)的十六进制字符串
print(hash_value)
print(len(hash_value))
print(base64.b64encode(data))
# e17910c91985a9923d87c516330dda05b50e272ca092c0b90aedfa63bf9b77aed63abf3b41d2045a5459ed38dc4343ed1997e90c4d1fa5fa408690cfedc5f2e5
# 7cfabd1aa17366f656f798f561059aeb80fccc35dd1c3af4caac4f6eb478c7b6350cc35e29e54e3f654ef0f57324302e9ba3aed0aba23b7446bc1b875d097ba1d39af4d8ce81131e6b8064a7a179f30d712a35b425eedf878571d0b598bc03faa251766810366fe3e5e16db99d714b1e2aefa2791287fc765df0e53ef1a9ca4f
# 48f47223167479066fa329b6912fb2bd
# 48f47223167479066fa329b6912fb2bd
s = 'a6db11202856a75dd057be58673f99752de7520bb9ca5fc7a1bcf692f510602a2e23a99183a40ef98edecf11c2887fa5ac3663282ee464cbb01a810c154f4ad25a17ea3650e2147cc425bb591a86e0e13bad750100180d0beaa3bb0d41ad0a4668092cddc29ee259937f1ad0cb4b1879f7944ce3195fcb88f4fec9a2d2b22701'

print(len(s))


def strxor(a, b):  # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


# print('密码高强度加密方法')
# key = 'android123456'
# salt = 'python'
# print(key)
# '''''
# data=strxor("123456",key)
# print(data)
# data=strxor("123456",data)
# print(data)
# '''
#
# key1 = base64.b64encode(key.encode('utf-8'))
# print(key1)
# key2 = hashlib.md5(key1 + salt.encode('utf-8')).hexdigest()
# print(key2)
# key3 = hashlib.sha1(key2 + salt.encode('utf-8')).hexdigest()
# print('该sha1密文不可逆')
# print(key3)
# key4 = hashlib.sha512(key3 + salt.encode('utf-8')).hexdigest()
# print('该sha512密文不可逆')
# print(key4)
#
# print('test===========')
# print(hashlib.algorithms_available)
# h = hashlib.new('md5')
# print(h)
# h.update('begin')
# print(h.hexdigest())
# print(h.digest())
# print(h.digest_size)
# print(h.block_size)
# h2 = hashlib.new('ripemd160', 'what')
# print(h2)
# print(h2.hexdigest())
# print(h2.digest_size)
# print(h2.block_size)