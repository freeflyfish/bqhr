# coding:utf-8

import re
import requests
from time import time
from selenium import webdriver

jv_pattern = re.compile('\("(.*?)"\)', re.S)


def js_driver(content):
    index_url = 'https://www.baidu.com/'
    driver = webdriver.PhantomJS('d:\\phantomjs.exe')
    driver.get(index_url)
    jv = jv_pattern.findall(content)
    dr_val = driver.execute_script('var val = %s; return val;' % jv[0])
    return dr_val


url = 'https://v4.passport.sohu.com/fe/'

headers = {
    'Host': 'v4.passport.sohu.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://mail.sohu.com',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # 'Referer': 'https://mail.sohu.com/fe/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
cookies_dict = {'a': '123'}
req_ss = requests.session()

index_res = req_ss.get(url, headers=headers, verify=False)
print(index_res.text)
print('index_url', index_res.cookies.get_dict())
cookies_dict.update(index_res.cookies.get_dict())
# 获取cookies
index_cookie_url = 'https://v4.passport.sohu.com/i/cookie/common?callback=passport403_cb%s&_=%s' % \
                   (int(time() * 1E3), int(time() * 1E3) + 789)
index_cookie_res = req_ss.get(index_cookie_url, verify=False)
print(index_cookie_res.text)
print('index_cookies_url', index_cookie_res.cookies.get_dict())
cookies_dict.update(index_cookie_res.cookies.get_dict())
code_callback_url = 'https://v4.passport.sohu.com/i/jf/code?callback=passport403_cb%s&type=0&_=%s' % \
                    (int(time() * 1E3), int(time() * 1E3) + 789)
code_callback_res = req_ss.get(code_callback_url, verify=False)
print('code_call_url', code_callback_res.cookies.get_dict())
cookies_dict.update(code_callback_res.cookies.get_dict())
# 解析
jv_val = js_driver(code_callback_res.text)
req_ss.cookies.update({jv_val.split('=')[0]: jv_val.split('=')[1].split(';')[0]})
cookies_dict.update({jv_val.split('=')[0]: jv_val.split('=')[1].split(';')[0]})
# req_ss.get('http://127.0.0.1:49194/wd/hub/session')
# req_ss.get('http://127.0.0.1:49194/wd/hub/session/848805f0-fa64-11e7-a4b8-8b8ea0f67765/url')

data = {
    'userid': 'xiongtaozt@sohu.com',
    'password': 'e2894b0ebe3626ae40bbef54e8182936',
    'appid': '101305',
    'callback': 'passport403_cb%s' % int(time() * 1E3)
}
login_url = 'https://v4.passport.sohu.com/i/login/101305'
res = req_ss.post(login_url, data=data, verify=False)
print('login_url', res.cookies.get_dict())
cookies_dict.update(res.cookies.get_dict())
print(res.text)
list_url = 'https://mail.sohu.com/fe/folders?t=%s' % int(time() * 1E3)
# list_url = 'https://mail.sohu.com/fe/getList?offset=0&limit=20&folderId=1&order=id&sort=0&t=%s' % int(time() * 1E3)
call_back = req_ss.post('https://mail.sohu.com/fe/login/callback', verify=False)
cookies_dict.update(call_back.cookies.get_dict())
print(call_back.text)
list_res = req_ss.get(list_url, verify=False)
print(list_res.text)
print('cookies_dict', cookies_dict)
logout_code_url = 'https://v4.passport.sohu.com/i/jf/code?callback=passport403_cb%s&type=0&_=%s' % (
int(time() * 1E3), int(time() * 1E3) + 789)
logout_code_res = req_ss.get(logout_code_url, verify=False)
jv_val = js_driver(logout_code_res.text)
cookies_dict.update({jv_val.split('=')[0]: jv_val.split('=')[1].split(';')[0]})
cookies_dict.update(logout_code_res.cookies.get_dict())
print(cookies_dict)
# cookies_dict = {'a': '123', 'gidinf': 'x099980109ee0d3a51f5d8815000acf97050d3f0994e', 'reqtype': 'pc', 'jv': 'a6d0bcc60d7178dfa5ffa1eeea640165-xRPeT1Gv1516087080387', 'ppinf': '2|1516087091|1517296691|bG9naW5pZDowOnx1c2VyaWQ6MTk6eGlvbmd0YW96dEBzb2h1LmNvbXxzZXJ2aWNldXNlOjMwOjAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMHxjcnQ6MTA6MjAxOC0wMS0xNnxlbXQ6MTowfGFwcGlkOjY6MTAxMzA1fHRydXN0OjE6MXxwYXJ0bmVyaWQ6MTowfHJlbGF0aW9uOjA6fHV1aWQ6MDp8dWlkOjA6fHVuaXFuYW1lOjA6fA', 'pprdig': 'aQ1UEjBreyR8e_bmC0nsth7qu3h8cQmqCVOOXh4bVcseqoLQDf3cycHNQoR0OiVnU5uh1wIXuTLt0o34YuPL710VIYtogYdh8LIuLlV-6bG1zEGSd9XTkkTKKFxgQSExAXXhEa1TiTWtky54SaOVg2Lgq7H7RJ2ZlMbmID0poGg', 'mailinfo': 'xiongtaozt@sohu.com:xiongtaozt@sohu.com:f0687d68d8ba188355aae1630593771a', 'ppmdig': '15160870820000007aefc8176842f52069ca0540ff925354'}
logout_headers = {
        'Host': 'v4.passport.sohu.com',
        'Connection': 'keep-alive',
        'Content-Length': '49',
        'Cache-Control': 'max-age=0',
        'Origin': 'https://mail.sohu.com',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://mail.sohu.com/fe/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
}
logout_url = 'https://v4.passport.sohu.com/i/logout/101305'
data = {'appid': '101305', 'callback': 'passport403_cb%s' % int(time() * 1E3)}

logout_res = requests.post(logout_url, data=data, cookies=cookies_dict, verify=False)
print(logout_res.text)
