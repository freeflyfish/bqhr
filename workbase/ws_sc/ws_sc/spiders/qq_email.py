import scrapy
import time
import json
import requests
from urllib.parse import quote
from scrapy.http import Request, FormRequest
from ws_sc.items.dkm_items import DKMItem
from captcha.qqemail.slider import *

from contextlib import suppress
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException


class QQSpider(scrapy.Spider):
    name = 'qq_email'
    allowed_domains = ["qq.email.com"]
    username = '380784649@qq.com'
    password = 'xiongtaozting123'
    password_p = 'scx1123'
    start_urls = [
        'https://mail.qq.com/'
    ]
    headers = {
        'Host': 'mail.qq.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://mail.qq.com/cgi-bin/frame_html?sid=gyf5d0xfanPedWw1&r=cc7a72fa2f220344ac30afee53fc806a',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }

    # def start_requests(self):
    #     yield Request(url='https://www.baidu.com/', callback=self.parse, dont_filter=True)

    def parse(self, response):
        driver = webdriver.Chrome(r'D:\chromedriver.exe')
        wait = WebDriverWait(driver, 20)
        driver.get('https://mail.qq.com/')
        wait.until(lambda the_driver: the_driver.find_element_by_xpath('//iframe[@id="login_frame"]'))
        driver.switch_to.frame("login_frame")
        # driver.execute_script('document.getElementById("switcher_plogin").click()')
        # 注入用户密码
        script = "document.getElementById('qlogin').style='display: none;';" \
                 "document.getElementById('web_qr_login').style='height: 330px;';"

        driver.execute_script(script)
        driver.implicitly_wait(1)
        driver.find_element_by_id('switcher_plogin').click()  # 用非PhantomJSWebdriverSpider注释此句
        time.sleep(0.5)
        wait.until(lambda the_driver: the_driver.find_element_by_xpath('//input[@id="p"]'))
        driver.find_element_by_id("u").send_keys(self.username)
        time.sleep(0.5)
        driver.find_element_by_id("p").send_keys(self.password)
        driver.find_element_by_id("login_button").click()
        time.sleep(2)
        if "验证独立密码" in driver.page_source:
            # 验证是否存在独立密码
            wait.until(lambda the_driver: the_driver.find_element_by_xpath('//input[@id="pp"]'))
            driver.find_element_by_id("pp").send_keys(self.password_p)
            driver.find_element_by_id('btlogin').click()
        if '安全验证' in driver.page_source:
            try:
                driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
                slide = None
                # 滑块
                with suppress(NoSuchElementException):
                    slide = driver.find_element_by_id('slide')

                    qq = QQEmailSlider(driver, wait)
                    reslut = qq.drag_slider("//*[@id='slideBkg']",
                                            "//*[@id='tcaptcha_drag_thumb']",
                                            "//*[@id='slideBkg']", "//div[@id='web_login']", False)
                    if not reslut:
                        self.logger(self.username,
                                                      msg="qq---验证码输入错误：(username:%s, password:%s) %s"
                                                          % (self.username, self.password, '滑块滑动异常'),
                                                      tell_msg='滑块滑动异常')
                        return
                if not slide:
                    # 验证码
                    captcha_url = driver.find_element_by_id('capImg').get_attribute('src')

                    headers = {
                        "Host": "ssl.captcha.qq.com",
                        "Connection": "keep-alive",
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
                        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
                        "Referer": "https://ssl.captcha.qq.com/cap_union_new_show?aid=522005705&asig=&captype=&protocol=https&clientype=2&disturblevel=&apptype=2&curenv=inner&sess=4RFB8HtQhN8gqH-MW0SN6OQp1T0lUhtJpSFO23NWR16t4OdTYcucKXClp_2uSv7OaGezMdv9qelpQw_8iVnxf47bi8Lzmzabpi1Rt0suI5URDm8MNvI9_p-SdTXg1RRx0xvyXVklkCJCmMHh6wOA46nfGv4fh6KBS00CPl9SCxExSP24SubZtTxD_rBCUnBG6XD4k5iLqWU*&theme=&noBorder=noborder&fb=1&showtype=embed&uid=421084068&cap_cd=YZt-qzys3zjj6l2Sbjb6B60UiL7WQ78n1MzPh9vmlIrif9kkijY58g**&lang=2052&rnd=992371",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Accept-Language": "zh-CN,zh;q=0.8",

                    }
                    cookies = driver.get_cookies()
                    code_body = requests.get(captcha_url, headers=headers, cookie_jar=cookies)

                    captcha_code = self.ask_image_captcha(code_body, self.username)
                    script = "document.getElementById('capAns').value='{0}';".format(captcha_code)
                    driver.execute_script(script)
                    script = "document.getElementById('submit').click();".format(captcha_code)
                    driver.execute_script(script)
                    driver.implicitly_wait(1)
                    with suppress(NoSuchElementException):
                        err_message = driver.find_element_by_id('capAns')
                        self.logger(self.username,
                                                      msg="qq---验证码输入错误：(username:%s, password:%s) %s"
                                                          % (self.username, self.password, err_message),
                                                      tell_msg='验证码输入错误')
                        return
            except Exception:
                pass
            if '安全验证' in driver.page_source:
                try:
                    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
                    slide = None
                    # 滑块
                    with suppress(NoSuchElementException):
                        slide = driver.find_element_by_id('slide')
                        wait = WebDriverWait(driver, 20)
                        qq = QQEmailSlider(driver, wait)
                        reslut = qq.drag_slider("//*[@id='slideBkg']",
                                                "//*[@id='tcaptcha_drag_thumb']",
                                                "//*[@id='slideBkg']", "//div[@id='web_login']", False)
                        if not reslut:
                            self.logger(self.username,
                                                          msg="qq---验证码输入错误：(username:%s, password:%s) %s"
                                                              % (self.username, self.password, '滑块滑动异常'),
                                                          tell_msg='滑块滑动异常')
                            return
                    if not slide:
                        # 验证码
                        captcha_url = driver.find_element_by_id('capImg').get_attribute('src')

                        headers = {
                            "Host": "ssl.captcha.qq.com",
                            "Connection": "keep-alive",
                            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
                            "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
                            "Referer": "https://ssl.captcha.qq.com/cap_union_new_show?aid=522005705&asig=&captype=&protocol=https&clientype=2&disturblevel=&apptype=2&curenv=inner&sess=4RFB8HtQhN8gqH-MW0SN6OQp1T0lUhtJpSFO23NWR16t4OdTYcucKXClp_2uSv7OaGezMdv9qelpQw_8iVnxf47bi8Lzmzabpi1Rt0suI5URDm8MNvI9_p-SdTXg1RRx0xvyXVklkCJCmMHh6wOA46nfGv4fh6KBS00CPl9SCxExSP24SubZtTxD_rBCUnBG6XD4k5iLqWU*&theme=&noBorder=noborder&fb=1&showtype=embed&uid=421084068&cap_cd=YZt-qzys3zjj6l2Sbjb6B60UiL7WQ78n1MzPh9vmlIrif9kkijY58g**&lang=2052&rnd=992371",
                            "Accept-Encoding": "gzip, deflate, br",
                            "Accept-Language": "zh-CN,zh;q=0.8",

                        }
                        cookies = get_cookies_dict_from_webdriver(driver)
                        code_body = get_content_by_requests(captcha_url, headers=headers, cookie_jar=cookies)

                        captcha_code = self.ask_image_captcha(code_body, self.username)
                        script = "document.getElementById('capAns').value='{0}';".format(captcha_code)
                        driver.execute_script(script)
                        script = "document.getElementById('submit').click();".format(captcha_code)
                        driver.execute_script(script)
                        driver.implicitly_wait(1)
                        with suppress(NoSuchElementException):
                            err_message = driver.find_element_by_id('capAns')
                            self.logger(self.username,
                                                          msg="qq---验证码输入错误：(username:%s, password:%s) %s"
                                                              % (self.username, self.password, err_message),
                                                          tell_msg='验证码输入错误')
                            return
                except Exception:
                    pass