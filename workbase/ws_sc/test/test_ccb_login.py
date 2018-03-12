# coding:utf-8

import re
import requests
from ws_sc.jh import get_b_value
from urllib.parse import quote

req = requests.session()

password = 'pm988311'
headers = {
    "Referer": "https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlat_09?SERVLET_NAME=B2CMainPlat_09&CCB_IBSVersion=V6&PT_STYLE=1&CUSTYPE=0&TXCODE=CLOGIN&DESKTOP=0&EXIT_PAGE=login.jsp&WANGZHANGLOGIN=&FORMEPAY=2",
    "Origin": "https://ibsbjstar.ccb.com.cn",
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50)",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,en,*"
}

url = 'https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlatP1?SERVLET_NAME=B2CMainPlatP1&CCB_IBSVersion=' \
      'V6&PT_STYLE=1&CUSTYPE=0&TXCODE=CLOGIN&DESKTOP=0&EXIT_PAGE=login.jsp&WANGZHANGLOGIN=&FORMEPAY=2'
req.headers = headers
html = req.get(url)
print(html.status_code)
# print(html.content)
try:
    ifUseYinshe = '1'
    encode_pwd = ""

    # response = requests.get(url)
    page = html.content.decode("utf-8")
    a = re.search("a\|(.+?)\|b", page).group(1)
    print("A:%s" % a)
    b = get_b_value(page)
    if not b:
        # return
        pass
    newValue = password
    specialChar = 0
    if ifUseYinshe == "1":
        everyone = ''
        afterPass = ''
        for i in range(len(newValue)):
            if specialChar == 1:
                break
            everyone = newValue[i]
            for j in range(len(b) // 2):
                if everyone == b[2 * j]:
                    afterPass = afterPass + b[2 * j + 1]
                    break
                if j == len(b) // 2 - 1:
                    if everyone != b[2 * j]:
                        specialChar = 1
                        break
        if specialChar == 0:
            encode_pwd = afterPass
        else:
            ret = ""
            afterPass = ''
            for i in range(len(newValue)):
                c = newValue[i]
                ts = quote(c)
                if ts[:2] == "%u":
                    ret = ret + ts.replace("%u", "(^?)")
                else:
                    ret += c
            encode_pwd = ret
            for n in range(len(ret)):
                everyone = ret[n]
                for w in range(len(b) // 2):
                    if everyone == b[2 * w]:
                        afterPass = afterPass + b[2 * w + 1]
                        break
            encode_pwd = afterPass
    print('this password', encode_pwd)
except Exception as e:
    # self.logger.exception("加密密码失败:%s" % str(e))
    print(e)
    # return

# 开始模拟登陆

