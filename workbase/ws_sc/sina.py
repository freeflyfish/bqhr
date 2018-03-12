import requests
from time import sleep
from selenium import webdriver


def get_cookies_list_from_phantomjs(url, sleep_time=0.1):
    driver = webdriver.PhantomJS(
        r'D:\workspaces\py-workspace\crawler\crawler_bqjr\crawler_bqjr\browsers\phantomJS\phantomjs.exe')
    try:
        driver.get(url)
        cookies_list = get_cookies_list_from_webdriver(driver, sleep_time)
        return cookies_list
    except Exception:
        return []
    finally:
        driver.quit()


def get_cookies_dict_from_phantomjs(url, sleep_time=0.1):
    return {cookie["name"]: cookie["value"] for cookie
            in get_cookies_list_from_phantomjs(url, sleep_time)}


def get_cookies_list_from_webdriver(driver, sleep_time=0.1):
    cookies_list = []
    for i in range(3):
        cookies_list = driver.get_cookies()
        if cookies_list:
            break
        else:
            sleep(sleep_time)
    return cookies_list


def get_content_by_requests(url, headers, cookie_str=None, cookie_jar=None):
    resp = get_response_by_requests(url, headers=headers,
                                    cookie_str=cookie_str, cookie_jar=cookie_jar)
    return resp.content


def get_response_by_requests(url, headers, cookie_str=None, cookie_jar=None):
    if cookie_str is not None:
        headers.update({'Cookie': cookie_str})

    kwargs = {"headers": headers,
              "timeout": 11,
              "verify": False,
              }

    if cookie_jar is not None:
        kwargs["cookies"] = cookie_jar

    return requests.get(url, **kwargs)


from base64 import b64encode
from time import time
from random import random
from urllib.parse import quote, unquote
from re import findall
import requests
from json import loads

from base64 import b64encode, b64decode
from binascii import b2a_hex, a2b_hex
from rsa import PublicKey, PrivateKey, encrypt, decrypt

password = 'abc123456'


def enb64(text):
    if isinstance(text, str):
        text = text.encode()
    return b64encode(text)


def deb64(text):
    if isinstance(text, str):
        text = text.encode()
    return b64decode(text)


def url_encode(text):
    if isinstance(text, str):
        text = text.encode()
    return quote(text)


def url_decode(text):
    if isinstance(text, str):
        text = text.encode()
    return unquote(text)


class RsaUtil(object):
    """
    RSA加解密工具类
    """

    def __init__(self, key_is_hex=False):
        self.__pub_key = None  # 公钥对象
        self.__priv_key = None  # 私钥对象
        self._key_is_hex = key_is_hex  # 公钥私钥默认为base64编码

    def __set_pubkey(self, pubkey):
        """
        设置公钥
        :param pubkey:
        :return:
        """
        if self._key_is_hex:
            b_str = a2b_hex(pubkey)
            pubkey = b64encode(b_str)
        pkl = self._convert_key(pubkey)
        modulus = int(pkl[0], 16)
        exponent = int(pkl[1], 16)
        self.__pub_key = PublicKey(modulus, exponent)

    def __set_privkey(self, priv_key):
        """
        设置私钥
        :param priv_key:
        :return:
        """
        if self._key_is_hex:
            b_str = a2b_hex(priv_key)
            priv_key = b64encode(b_str)
        pkl = self._convert_key(priv_key, is_pubkey=False)
        n = int(pkl[0], 16)
        e = int(pkl[1], 16)
        d = int(pkl[2], 16)
        p = int(pkl[3], 16)
        q = int(pkl[4], 16)
        self.__priv_key = PrivateKey(n, e, d, p, q)

    def _convert_key(self, key, is_pubkey=True):
        """
        转换key
        :param is_pubkey:
        :return:
        """
        b_str = b64decode(key)

        if len(b_str) % 128 == 0:
            n = b2a_hex(b_str)
            e = b'10001'
            return (n, e)

        hex_str = ''

        # 按位转换成16进制
        for x in b_str:
            h = hex(x)[2:]
            h = h.rjust(2, '0')
            hex_str += h

        # 找到模数和指数的开头结束位置
        if is_pubkey:
            # 转换公钥
            n_start = 29 * 2
            e_start = 159 * 2
            n_len = 128 * 2
            e_len = 3 * 2

            n = hex_str[n_start:n_start + n_len]
            e = hex_str[e_start:e_start + e_len]

            return (n, e)
        else:
            # 转换私钥
            n_start = 11 * 2
            e_start = 141 * 2
            d_start = 147 * 2
            p_start = 278 * 2
            q_start = 345 * 2

            n_len = 128 * 2
            e_len = 3 * 2
            d_len = 128 * 2
            p_len = 64 * 2
            q_len = 64 * 2

            n = hex_str[n_start:n_start + n_len]
            e = hex_str[e_start:e_start + e_len]
            d = hex_str[d_start:d_start + d_len]
            p = hex_str[p_start:p_start + p_len]
            q = hex_str[q_start:q_start + q_len]

            return (n, e, d, p, q)

    def encrypt(self, text, pubkey, get_hex=False):
        """
        加密(公钥加密)
        :param text:
        :param pubkey:
        :param get_hex:
        :return:
        """
        self.__set_pubkey(pubkey)
        crypto = encrypt(text.encode("utf-8"), self.__pub_key)
        if get_hex:
            hex_str = str(b2a_hex(crypto))[2:-1]
            return hex_str
        else:
            return b64encode(crypto).decode("utf-8")

    def decrypt(self, msg, priv_key, is_hex=False):
        """
        解密(私钥解密)
        :param msg:
        :param priv_key:
        :param is_hex:
        :return:
        """
        self.__set_privkey(priv_key)
        if is_hex:
            content = a2b_hex(msg)
        else:
            content = b64decode(msg)
        message = decrypt(content, self.__priv_key).decode("utf-8")
        return message


s = b'daniel543@sina.cn'
# if s 是 "手机号": type = cmmail else type = freemail
su = enb64(url_encode(s)).decode()
print(su)
step1_url = 'http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js(v1.4.19)' % su
from requests import session, get as http_get, post as http_post

headers = {
    'Origin': 'http://mail.sina.com.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Referer': 'http://mail.sina.com.cn/',
}
http_session = session()
a = http_session.get("http://mail.sina.com.cn/", headers=headers, verify=False)
prelogin_url = "https://login.sina.com.cn/sso/prelogin.php?entry=cnmail&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js(v1.4.19)&_=%s" % (
su, str(int(time() * 1E3)))

b = http_session.get(prelogin_url, verify= False)
r1 = http_session.get(step1_url, verify=False)
response_js = loads(findall('CallBack\((.*?)\)', r1.text)[0])
retcode = response_js.get('retcode', '')
servertime = response_js.get('servertime', '')
pcid = response_js.get('pcid', '')
nonce = response_js.get('nonce', '')
pubkey = response_js.get('pubkey', '')
rsakv = response_js.get('rsakv', '')
uid = response_js.get('uid', '')
exectime = response_js.get('exectime', '')
my_rsa = RsaUtil(key_is_hex=True)
msg = str(servertime) + '\t' + str(nonce) + '\n' + str(password)
password = my_rsa.encrypt(msg, pubkey=pubkey, get_hex=True)

import random
captcha_url = 'https://login.sina.com.cn/cgi/pin.php?r=%s&s=0&p=%s' % (int(random.random()*100000000), pcid)
# rsaPublickey = int(pubkey, 16)
# key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥
# message = str(servertime) + '\t' + str(nonce) + '\n' + str(password) #拼接明文js加密文件中得到
# passwd = rsa.encrypt(message, key) #加密
# passwd = binascii.b2a_hex(passwd) #将加密信息转换为16进制。
# 3f8812b08fea18143443dff9dba111f1398232b0a1559d57f50f18c10808bc1fc3e5d63370a654fae2256431009b9707523b1cd118ac3a8b47a5df73896f4977e079c53c365911f035e3dd4473c093343052da18bcf7afc4b4833bac41f0dad4397f311bb3552803d646b5bc11410f8b5d84a07964803df79e91b9545fa99a1d
# captcha_vcode = http_session.get(captcha_url)
# with open('captcha.png', 'wb') as f:
#     f.write(captcha_vcode.content)
#     f.close()
# captcha_code = input('>')
headers = {
    # 'Host': 'login.sina.com.cn',
    # 'Connection': 'keep-alive',
    # 'Origin': 'http://mail.sina.com.cn',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'Accept': '*/*',
    # 'Referer': 'http://mail.sina.com.cn/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
}
post_data = {
    'entry': 'freemail',
    'gateway': '1',
    'from': '',
    'savestate': response_js.get("savestate") or 0,
    'qrcode_flag': 'false',
    'useticket': '0',
    'pagerefer': 'http://mail.sina.com.cn/?logout',
    # 'door': captcha_code,
    'pcid': pcid,
    'su': su,
    'service': 'sso',
    'servertime': servertime,
    'nonce': nonce,
    'pwencode': 'rsa2',
    'rsakv': rsakv,
    'sp': password,
    'sr': '1366*768',
    'encoding': 'UTF-8',
    'cdult': '3',
    'domain': 'sina.com.cn',
    'prelt': '213',
    'returntype': 'TEXT',
}
r = http_session.post(
    'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)&_=%s' % str(int(time() * 1E3)), data=post_data)
url = 'https://m1.mail.sina.com.cn/classic/findmail.php'
data_form = {
                'act': 'findmail',
                'fid[]': '',
                'order': 'htime',
                'sorttype': 'desc',
                'flag': '',
                'pageno': '1',
                'fol': 'allfolder',
                'phrase': '账单',
                'attlimit': '2',
                'timelimit': '0',
                'starttime': '1505750400000',
                'endtime': '1505750400000',
                'contlimit[]': ['3', '2', '1'],
                'readflag': '2',
                'searchType': '1',
                'tag': '-1',
                'webmail': '1',
            }
r_json = loads(r.text)
print(r_json)
corss = http_session.get(r_json['crossDomainUrlList'][1], verify=False)

corss2 = http_session.get(r_json['crossDomainUrlList'][0], verify=False)

r2 = http_session.get('http://mail.sina.com.cn/cgi-bin/sla.php?a={0}&b={1}&c=0&ssl=1'.format(str(int(time() * 1E3)),str(int(time() * 1E3))), verify=False)

import re
url1 = re.findall('replace\(\"(.*?)\"\)', r2.text)[0]
r3 = http_session.get(url1, verify=False)
print(http_session.cookies.get_dict())
headers['Cookie'] = ''
for x in http_session.cookies.get_dict().items():
    headers['Cookie'] += x[0] + '=' + x[1] + ';'
print(headers['Cookie'])
res = requests.post(url, data=data_form, headers=headers, verify=False)
print(res.text)

# 退出
logout_url = 'https://m0.mail.sina.com.cn/classic/logout.php?from=mail'

lot = http_session.get(logout_url, verify=False)
print(lot.text)
lot2 = http_session.get('https://login.sina.com.cn/cgi/login/logout.php?r=http%3A%2F%2Fmail.sina.com.cn%2F%3Flogout', verify=False)
print(lot2.text)
lot3_url = re.findall('replace\("(.*?)"\);', lot2.text)[0]
lot3 = http_session.get(lot3_url, verify=False)
print(lot3.text)