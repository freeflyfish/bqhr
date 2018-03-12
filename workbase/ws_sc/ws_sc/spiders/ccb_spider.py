# -*- coding:utf-8 -*-

import requests
import re


import scrapy
from scrapy.http import Request,FormRequest

from urllib.parse import quote
from selenium import webdriver


class CCBSpider(scrapy.Spider):

    name = 'ccb'
    allowed_domains = 'ccb.com'
    start_urls = ['https://ibsbjstar.ccb.com.cn/CCBIS/V6/common/login.jsp']

    username = '510121199009123831'
    password = '暂缺'

    def parse(self, response):
        url = "https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlat_09?SERVLET_NAME=B2CMainPlat_09&CCB_IBSVersion=V6&" \
              "PT_STYLE=1&CUSTYPE=0&TXCODE=CLOGIN&DESKTOP=0&EXIT_PAGE=login.jsp&WANGZHANGLOGIN=&FORMEPAY=2"

        # 校验身份证号
        identity_code = self.username
        if identity_code is None or identity_code == "":
            # yield from self.except_handle(identity_code, "", tell_msg="账户不能为空")
            print('账户不能为空')
            return
        if not re.match('^[0-9Xx]+$', identity_code):
            # yield from self.except_handle(identity_code, "", tell_msg="账号只能包含数字和X")
            print('账号只能包含数字和X')
            return
        # 校验密码
        password = self.password
        if password is None or password == "":
            # yield from self.except_handle(item["username"], "", tell_msg="密码不能为空")
            print('密码不能为空')
            return
        if password is not None and (not re.match('^[0-9a-zA-Z]+$', password)):
            # yield from self.except_handle(item["username"], "", tell_msg="密码只能包含数字和字母")
            print('密码只能包涵字母和数字')
            return
        if password is not None and (len(password) > 10 or len(password) < 6):
            # yield from self.except_handle(item["username"], "", tell_msg="密码必须是6至10位")
            print('密码必须是6-10位')
            return
        # 开始登陆
        try:
            driver = webdriver.Chrome(executable_path='D:\\chromedriver.exe')
            driver.get(url)
            # wait.until(lambda dr: dr.find_element_by_id("USERID").is_displayed())
            # 填写登录表单
            # driver.get_screenshot_as_file("screenshot1.png")
            id_no_input = driver.find_element_by_id("USERID")
            id_no_input.send_keys(self.username)
            password_input = driver.find_element_by_id("LOGPASS")
            password_input.send_keys(self.encode_password(self.password))
            # 验证码
            captcha_input = None
            # 暂不考虑验证码 提交登陆
            driver.find_element_by_id("loginButton").submit()
        except Exception:
            pass
        pass

    def encode_password(self, password):
        """
        加密密码
        :param password:
        :return:
        """
        try:
            url = "https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlat_09?SERVLET_NAME=B2CMainPlat_09&CCB_IBSVersion=V6&" \
                  "PT_STYLE=1&CUSTYPE=0&TXCODE=CLOGIN&DESKTOP=0&EXIT_PAGE=login.jsp&WANGZHANGLOGIN=&FORMEPAY=2"
            ifUseYinshe = '1'
            encode_pwd = ""

            response = requests.get(url)
            page = response.content.decode("utf-8")
            a = re.search("a\|(.+?)\|b", page).group(1)
            self.logger.info("A:%s" % a)
            b = self.get_b_value(page)
            if not b:
                return

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
            return encode_pwd
        except Exception as e:
            self.logger.exception("加密密码失败:%s" % str(e))
            return

    def get_b_value(self, page):
        """
        获取b的值
        :param page:
        :return:
        """
        try:
            eval_str = re.search('(eval[\s\S]+?)function check_bfr_submit', page)
            if eval_str is not None:
                eval_str = eval_str.group(1).strip()
            else:
                return
            eval_js = eval_str.replace("eval", "document.write")
            driver = webdriver.PhantomJS(executable_path='D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
            driver.execute_script(eval_js)  # 解密JS
            de_js_str = driver.page_source
            self.logger.info("Js:%s" % de_js_str)
            reg = re.compile(r"b\[\d+\]='(.+?)';", re.S)
            b_list = reg.findall(de_js_str)
            if b_list and len(b_list) > 0:
                return b_list
            self.logger.debug("获取值失败:%s" % str(b_list))
            return
        except Exception as e:
            self.logger.exception("获取值出错:%s" % str(e))
            return