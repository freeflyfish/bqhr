# coding:utf-8

import requests
import time
import json

headers = {
    'Host': 'https://mail.sohu.com',
    # 'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    # 'Upgrade-Insecure-Requests': '1',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    'Referer': 'https://mail.sohu.com/fe/',
    'Content-Type': 'application/x-www-form-urlencoded'

}

url = 'https://mail.sohu.com/fe/anoy/login'
req_session = requests.session()
# req_session.get(url, headers=headers)
# data = {
#         'entry': 'freemail',
#         'gateway': '1',
#         'from': '',
#         'savestate': '0',
#         'qrcode_flag': 'false',
#         'useticket': '0',
#         'pagerefer': 'http://mail.sina.com.cn/',
#         'su': 'aGEuMjM2LmcxLnF4Zy5sYi5zaW5hbm9kZS5jb20',
#         'service': 'sso',
#         'servertime': '%s' % (int(int(time.time())/10)),
#         'nonce': 'YAB1T0',
#         'pwencode': 'rsa2',
#         'rsakv': '1330428213',
#         'sp': 'a6db11202856a75dd057be58673f99752de7520bb9ca5fc7a1bcf692f510602a2e23a99183a40ef98edecf11c2887fa5ac3663282ee464cbb01a810c154f4ad25a17ea3650e2147cc425bb591a86e0e13bad750100180d0beaa3bb0d41ad0a4668092cddc29ee259937f1ad0cb4b1879f7944ce3195fcb88f4fec9a2d2b22701',
#         'sr': '1366 * 768',
#         'encoding': 'UTF-8',
#         'cdult': '3',
#         'domain': 'sina.com.cn',
#         'prelt': '229',
#         'returntype': 'TEXT'
#     }
data = {"username": "xiongtaozt@sohu.com", "password": "48f47223167479066fa329b6912fb2bd",
        "m": '1', "autologin": 'false'}

result = requests.post('https://mail.sohu.com/fe/anoy/login', json=data, headers=headers, verify=False)
print(result.text)
print(result.headers)
print(result.cookies)