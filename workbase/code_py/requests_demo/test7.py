# coding:utf-8

import requests

url = 'https://www.uu143.com/htm/novellist2/'
# url = 'https://www.uu143.com/htm/novel2/110172.htm'

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
}


response = requests.get(url, headers=headers, verify=False)
print(response.content)