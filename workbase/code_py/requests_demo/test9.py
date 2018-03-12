# coding:utf-8

import requests

http_session = requests.session()
headers = {
            'Host': 'm0.mail.sina.com.cn',
            'Origin': 'http://m0.mail.sina.com.cn',
            'Referer': 'http://m0.mail.sina.com.cn/classic/index.php',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        }

url = 'http://mail.sina.com.cn/'
response = http_session.get(url, headers=headers)
print(response.cookies)