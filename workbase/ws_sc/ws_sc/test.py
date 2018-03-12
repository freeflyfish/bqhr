# coding:utf-8

import os.path as os_path
file = os_path.dirname(os_path.abspath(__file__))

print(file)
with open(file+'\proxies.txt', 'r') as f:
    print(f.readlines()[0][:-1])