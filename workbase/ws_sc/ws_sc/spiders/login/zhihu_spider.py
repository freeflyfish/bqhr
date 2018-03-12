# coding:utf-8

import requests

zhihu_index_url = 'https://www.zhihu.com/signup?next=%2F'

zhihu_login_url = 'https://www.zhihu.com/api/v3/oauth/sign_in'

headers = {
    'Host': 'www.zhihu.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://www.zhihu.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
req_session = requests.session()
response = req_session.get(zhihu_index_url, headers=headers, verify=False)
print(response.headers)
print(response.cookies.get_dict())
login_res = requests.post(zhihu_login_url)