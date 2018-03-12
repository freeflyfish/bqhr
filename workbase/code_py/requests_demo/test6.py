# coding:utf-8


import requests
import json
import time
from requests_demo.test2 import parse_capatcha
from urllib.parse import quote

name = "刘力"

url = 'http://www.dailianmeng.com/xinyong/q/%s.html' % quote(name)
headers = {
    'Referer': url,  # %E7%8E%8B%E6%9E%97
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
ses = requests.session()

# res = ses.get('http://www.dailianmeng.com/xinyong/q/王林.html', headers=headers)
# 获取验证码
json_vcode = ses.get('http://www.dailianmeng.com/xinyong/captcha.html?refresh=1&_=%s' % str(int(time.time()*1000)), headers=headers)
# http://www.dailianmeng.com/xinyong/captcha.html?v=59b0e5a22c032
vcode_url = 'http://www.dailianmeng.com' + json.loads(json_vcode.text)['url']
result = ses.get(vcode_url, headers=headers)
with open('vcode.jpg', 'wb') as f:
    f.write(result.content)
print(parse_capatcha(result.content))
vcode = input('>')
data = {
    'SearchForm[verifyCode]': vcode,
    'yt0': '',
}
response = ses.post(url=url, data=data)
print(response.text)
