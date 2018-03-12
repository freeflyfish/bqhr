# coding:utf-8

import hashlib
import time
import scrapy
from scrapy.http import Request,FormRequest
from base64 import b64encode, b64decode
from requests import session
from re import findall
from json import loads

from tools.rsa_tool import RsaUtil


class EmailSohuSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = 'xina.com'
    custom_settings = {
        'DOWNLOAD_DELAY': 1,  # 防封杀
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
    }
    su = b'xiongtaozt@sina.com'
    sp = 'scx1123'
    start_urls = [
        'http://mail.sina.com.cn/',
    ]

    headers = {
        'Host': 'm0.mail.sina.com.cn',
        'Origin': 'http://m0.mail.sina.com.cn',
        'Referer': 'http://m0.mail.sina.com.cn/classic/index.php',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }

    def start_requests(self):
        result = self._sina_login()
        cookies = result.cookies.get_dict()
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
        yield FormRequest(url='http://m0.mail.sina.com.cn/classic/findmail.php',
                          formdata=data_form,
                          headers=result.headers,
                          cookies=cookies,
                          callback=self.seach_detail,
                          meta={'cookie': cookies, 'data_form': data_form},
                          dont_filter=True)

    def seach_detail(self, response):
        print(response.text)


    def _sina_login(self):
        su = self._enb64(self.su)
        step1_url = 'http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js(v1.4.19)' % su
        http_session = session()
        http_session.get("http://mail.sina.com.cn/", headers=self.headers)
        prelogin_url = "https://login.sina.com.cn/sso/prelogin.php?entry=cnmail&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js(v1.4.19)&_=%s" % (
            su, str(int(time.time() * 1E3)))
        b = http_session.get(prelogin_url)
        r1 = http_session.get(step1_url)
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
        msg = str(servertime) + '\t' + str(nonce) + '\n' + str(self.sp)
        password = my_rsa.encrypt(msg, pubkey=pubkey, get_hex=True)
        post_data = {
            'entry': 'freemail',
            'gateway': '1',
            'from': '',
            'savestate': response_js.get("savestate") or 0,
            'qrcode_flag': 'false',
            'useticket': '0',
            'pagerefer': '',
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
            'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)&_=%s' % str(int(time.time() * 1E3)),
            data=post_data)
        r_json = loads(r.text)
        print(r_json)
        http_session.get(r_json['crossDomainUrlList'][1])
        http_session.get(r_json['crossDomainUrlList'][0])
        r2 = http_session.get(
            'http://mail.sina.com.cn/cgi-bin/sla.php?a={0}&b={1}&c=0&ssl=1'.format(str(int(time.time() * 1E3)),
                                                                                   str(int(time.time() * 1E3))))
        import re
        url1 = re.findall('replace\(\"(.*?)\"\)', r2.text)[0]
        r3 = http_session.get(url1)
        return r3

    def _enb64(self, text):
        if isinstance(text, str):
            text = text.encode()
        return b64encode(text)
