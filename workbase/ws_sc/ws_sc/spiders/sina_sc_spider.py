# coding:utf-8

import re
import time
import scrapy
import random
from scrapy.http import Request, FormRequest
from base64 import b64encode, b64decode
from re import findall
from json import loads
from urllib.parse import quote
from requests import get as http_get

from tools.rsa_tool import RsaUtil


class EmailSohuSpider(scrapy.Spider):
    name = 'sina_sc'
    allowed_domains = 'xina.com'
    custom_settings = {
        'DOWNLOAD_DELAY': 1,  # 防封杀
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
    }
    su = b'tazxuan@sina.com'
    sp = '123456123456'
    start_urls = [
        'http://mail.sina.com.cn/'
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.PAGE_PER_COUNT = 20
        self.seach_url = 'http://m0.mail.sina.com.cn/classic/findmail.php'  # post
        self.headers = {
            'Host': 'm0.mail.sina.com.cn',
            'Origin': 'http://m0.mail.sina.com.cn',
            'Referer': 'http://m0.mail.sina.com.cn/classic/index.php',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        }
        self.callback_partten = re.compile('CallBack\((.*?)\)')

    def parse(self, response):
        su = self._enb64(self._url_encode(self.su)).decode()
        prelogin_url = "https://login.sina.com.cn/sso/prelogin.php?entry=cnmail&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js(v1.4.19)&_=%s" % (
            su, str(int(time.time() * 1E3)))
        yield Request(prelogin_url, callback=self.prelogin, dont_filter=True)

    def prelogin(self, response):
        su = self._enb64(self._url_encode(self.su)).decode()
        step1_url = 'http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js(v1.4.19)' % su
        yield Request(step1_url, callback=self.step1, dont_filter=True)

    def step1(self, response):
        login_url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)&_=%s' % str(int(time.time() * 1E3))
        su = self._enb64(self._url_encode(self.su)).decode()
        response_js = loads(findall(self.callback_partten, response.text)[0])
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
        headers = {
            'Host': 'login.sina.com.cn',
            'Connection': 'keep-alive',
            'Origin': 'http://mail.sina.com.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Referer': 'http://mail.sina.com.cn/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        # 验证码请求
        captcha_url = 'https://login.sina.com.cn/cgi/pin.php?r=%s&s=0&p=%s' % (int(random.random() * (10**8)), pcid)
        post_data = {
            'entry': 'freemail',
            'gateway': '1',
            'from': '',
            'savestate':str(response_js.get("savestate")) or '0',
            'qrcode_flag': 'false',
            'useticket': '0',
            'pagerefer': '',
            'su': su,
            'service': 'sso',
            'servertime': str(servertime),
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
        # 发送验证码
        print(response.request.headers['Cookie'])
        headers = dict()
        headers['Cookie'] = response.request.headers['Cookie']
        # captcha_url = response.meta['captcha_url']
        captcha_vcode = http_get(captcha_url, headers=headers, verify=False)
        with open('captcha.png', 'wb') as f:
            f.write(captcha_vcode.content)
            f.close()
        captcha_code = input('>')
        # post_data = response.meta['post_data']
        # pcid = response.meta['pcid']
        post_data.update({'door': captcha_code, 'pcid': pcid})
        yield FormRequest(url=login_url,
                          formdata=post_data,
                          callback=self.user_login,
                          headers=headers,
                          meta={'captcha_url': captcha_url, 'pcid': pcid},
                          dont_filter=True)

    def user_login(self, response):
        login_js = loads(response.text)
        print(login_js)
        yield Request(url=login_js['crossDomainUrlList'][1],
                      callback=self.cross_domain_one,
                      meta={'cross': login_js['crossDomainUrlList'][0]},
                      dont_filter=True)
        # yield FormRequest('')

    def cross_domain_one(self, response):
        cross_url = response.meta['cross']
        yield Request(url=cross_url,
                      callback=self.user_login_two,
                      dont_filter=True)

    def user_login_two(self, response):
        login_url = 'http://mail.sina.com.cn/cgi-bin/sla.php?a={0}&b={1}&c=0&ssl=1'.format(str(int(time.time() * 1E3)), str(int(time.time() * 1E3)))
        yield Request(login_url, callback=self.find_sla, dont_filter=True)

    def find_sla(self, response):

        sla_url = re.findall(re.compile('replace\(\"(.*?)\"\)'), response.text)[0]
        yield Request(url=sla_url,
                      callback=self.find_detail,
                      dont_filter=True)

    def find_detail(self, response):
        search_url = 'https://m0.mail.sina.com.cn/classic/findmail.php'
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
        yield FormRequest(url=search_url,
                          formdata=data_form,
                          callback=self.search_detail,
                          dont_filter=True)

    def search_detail(self, response):
        print(response.text)
        pass

    def _enb64(self, text):
        if isinstance(text, str):
            text = text.encode()
        return b64encode(text)

    def _url_encode(self, text):
        if isinstance(text, str):
            text = text.encode()
        return quote(text)

