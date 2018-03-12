# coding:utf-8


import requests
import urllib.request
import json
import hashlib
from selenium import webdriver

# url = 'https://nper.cmbc.com.cn/pweb/static/login.html'
req = requests.session()
headers = {
    'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*',
    'Accept-Language': 'zh-CN',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'nper.cmbc.com.cn',
    'DNT': 1,
    'Connection': 'Keep-Alive',
    'Cache-Control': 'no-cache',
    'Cookie': 'org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN'
}
# data = {
#     'BankId': "9999",
#     'CspName': 'null',
#     'LoginType': "C",
#     'PwdResult': "aa0P4otwzQO8I6SCQrkSNDCuV9nNj8j+yUml622s6EtIXrQmMvCGzhweVkjVMMk1madFQWVu+/zlomPGEGMrAvx7G01zvAnQLu0uLws3QkMQIjWljbydu1lyjSWag89Ae/S0nXwO3ujvZSXrWOBfnJwM5DAW+H1JHmPe6owuYPY=",
#     'UserId': "6226220681208897",
#     '_UserDN': 'null',
#     '_asii': 6,
#     '_locale': "zh_CN",
#     '_targetPath': 'null',
#     '_vTokenName': ""
# }
# params = {
#     "PwdResult": "ORZg17MADyzTOQMNCV++L4W8ExdJoTpHbQiImlmMzVb4OkUXUUIDqbb6MYc8lameiFMnyplzqHsxso8wLgk7gyx5n53lxZ1dbiRdQj5nalCCoEVHbCZ7IEACD2H8qnJKjZ5YzcbCqzG0XcabAy3eJLkW1cVmtO5Y5IIkUNwkf0o=",
#     "CspName": 'null',
#     "BankId": "9999",
#     "LoginType": "C",
#     "_locale": "zh_CN",
#     "UserId": "6226220681208895",
#     "_vTokenName": "4A7A",
#     "_UserDN": 'null',
#     "_asii": 6,
#     "_targetPath": 'null'}
# req.get('https://nper.cmbc.com.cn/pweb/static/login.html')
# req.post('https://nper.cmbc.com.cn/pweb/UserTokenCheckCtrl.do')
# html = req.post("https://nper.cmbc.com.cn/pweb/clogin.do", data=data, headers=headers)
# print(req.cookies.get_dict())
# print(bytes.decode(html.content))

# pro_frie = r'C:\Users\BQ0391\AppData\Roaming\Mozilla\Firefox\Profiles\dasww1y6.default-1502261976932'
# jes_url = 'https://nper.cmbc.com.cn/pweb/UserTokenCheckCtrl.do'
# # url = "https://nper.cmbc.com.cn/pweb/static/login.html"
# profile = webdriver.FirefoxProfile(profile_directory=pro_frie)
# dr = webdriver.Firefox(executable_path='D:\\geckodriver.exe', firefox_profile=profile)
#
# dr.get(jes_url)
# print(dr.get_cookies())
# dr.get(url)
# print(dr.get_cookies())
# webdriver.Ie(executable_path='D:\\IEDriverServer_233.exe')



# # 获取Tomcat服务器产生的JSESSIONID
# # request = urllib.request.Request(url)
# # set_cookie = urllib.request.urlopen(request).info()['Set-Cookie']
# # json_id = set_cookie.split(';')[0]  # JSESSIONID=3037DCDF69A6454FC525E38C41E6B611
# # # json_id = json_id.split('=')[-1]
# # print(json_id)
# print(json.dumps(req.cookies.get_dict()))
# print(req.headers)

# md = 'aa0P4otwzQO8I6SCQrkSNDCuV9nNj8j+yUml622s6EtIXrQmMvCGzhweVkjVMMk1madFQWVu+' \
#      '/zlomPGEGMrAvx7G01zvAnQLu0uLws3QkMQIjWljbydu1lyjSWag89Ae/S0nXwO3ujvZSXrWOBfnJwM5DAW+H1JHmPe6owuYPY='
#
# s = '840808'
# md5 = hashlib.sha224()
# md5.update(s.encode('utf-8'))
# print(md5.hexdigest())

# s = b'\r\n\r\n\r\n\r\n{\r\n"errmsg":"\xe4\xbc\x9a\xe8\xaf\x9d\xe5\xb7\xb2\xe8\xb6\x85\xe6\x97\xb6",\r\n"errtype":"defaultPublicError"\r\n}'
# print(bytes.decode(s))
cookie = {'JSESSIONID': 't23fZLMSVkBTC8DTk4bF7vgZ31jHB6Ly2hqBwGBk4hQrJSh51FHV!2068902010',
          'app_lb_cookie': '16781322.24538.0000',
          'web_lb_cookie': '273678346.23770.0000',
          'org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE': 'zh_CN'
          }
data = {"ProductId": "ActTrsQry","PageNo":"P01030001"}
fromdata = {
                'AcNo': '6226220681208897',
                'BankAcType': '03',
                'BeginDate': '2017-05-10',
                'EndDate': '2017-08-10',
                'QueryType': '',
                'SubAcSeq': '0001',
                '_Download': 'xls',
                '_PrintCurrentPage': 'true',
                'checkflag': '2',
                'recordNumber': '10',
            }
url = 'https://nper.cmbc.com.cn/pweb/ActTrsQryDownload4BigFile.do'
html = requests.post(url, cookies=cookie, data=fromdata)
print(bytes.decode(html.content))
# with open('test.xls', 'wb') as f:
#     f.write(html.content)
