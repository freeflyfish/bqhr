# coding : utf-8

import scrapy
from scrapy.http import Request
from selenium import webdriver
import time
import json
import requests

from ..items.wssc_items import WsScItem, WsScItemDetail


class WjSpider(scrapy.Spider):
    name = 'ws'
    allowed_domains = 'email.163.com'
    start_urls = [
        'http://mail.163.com/',  # 首页信息
        'http://dl.reg.163.com/ini?pd=mail163&pkid=CvViHzl&pkht=mail.163.com&nocache=',  # 获取当前时间戳
        'http://dl.reg.163.com/gt?un=%s&pkid=CvViHzl&pd=mail163&nocache=%s',  # 验证用户信息 得到Tk验证
        'http://dl.reg.163.com/l'  # 执行页面登录
        # 最后转跳页面
        ]
    email = 'xiongtaozz'
    passwd = 'scx1123'
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
    }
    headers = {
        'Referer': 'https://dl.reg.163.com/',
        'User-Agent': 'Mozilla / 5.0(WindowsNT6.1;WOW64;rv: 54.0) Gecko / 20100101Firefox / 54.0'
    }

    fromData = {   # 需登录传递信息
        'd': 10,
        'domains': "163.com",
        'l': 0,
        'pd': "mail163",
        'pkid': "CvViHzl",
        'pw': "Xca8yR0cYTdBKTOEH77cGUdPXC2HvXGBOboRaCMl5ZzCh49Bjtf5oKNZb9VvyR0AgeiPdGSJr5kj+OM+HluvnAQ10UJyqhjHOWdUVdVAuwHLRRZcyvn/lFtlwq9RFKpmzJkRS02rE9QrDsgEib5OfEevaQ0YoY0UZeOA9afl34Q=",
        'pwdKeyUp': 1,
        't': 1501034716819,
        'tk': "fe35363dfcef6ca6ea00708d3bf666a4",
        'topURL': "http://mail.163.com/",
        'un': "xiongtaozz@163.com"
    }

    def start_requests(self):
        try:
            driver = webdriver.Chrome(executable_path='D:\\chromedriver.exe')
            url = 'http://mail.163.com/'
            driver.get(url)
            time.sleep(2)
            # 切换到表单
            driver.switch_to.frame("x-URS-iframe")
            driver.find_element_by_name("email").clear()
            driver.find_element_by_name("email").send_keys(self.email)
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys(self.passwd)
            driver.find_element_by_id("dologin").click()
            # 判断url是否改变如果改变,那么登录成功
            # 登录失败则,返回重新登录
            time.sleep(3)
            curr_url = driver.current_url
            print(curr_url)
            if url == curr_url:
                # 说明未登录成功
                pass
        except Exception:
            pass
        else:
            # 获取cookie信息
            cookie = driver.get_cookies()
            # 打印
            # cookiestr = ';'.join(item for item in cookie)
            # print(cookiestr)
            # 收件箱页面
            # http://mail.163.com/js6/main.jsp?sid=pBcSiePLJkzEkmbVdWLLvWLBdgIuBWNn&df=mail163_letter#module=mbox.ListModule%7C%7B%22fid%22%3A1%2C%22order%22%3A%22date%22%2C%22desc%22%3Atrue%7D
            # http://mail.163.com/js6/main.jsp?sid=RCzajBCarYXrcNkKuKaalNlHcWTlAHUC&df=mail163_letter#module=mbox.ListModule%7C%7B%22fid%22%3A1%2C%22order%22%3A%22date%22%2C%22desc%22%3Atrue%7D
            # 所有收件箱标题信息
            # http://mail.163.com/js6/s?sid=RCfqyBCauScrcNdSyKaaUEHPAOAiHemC&func=mbox:listMessages
            sid = curr_url.split('?')[1].split('&')[0]
            con_url = 'http://mail.163.com/js6/s?%s&func=mbox:listMessages' % sid

            # 模拟头信息  这里有可能会去验证防盗链. 所以对防盗链进行格式化处理
            headers = {
                'Content-type': 'application/x-www-form-urlencoded',
                'Host': 'mail.163.com',
                'Origin': 'http://mail.163.com',
                'Referer': 'http://mail.163.com/js6/main.jsp?%s&df=mail163_letter' % sid,
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3050.3 Safari/537.36',
            }
            #
            # 登录完成后,因163登录相对比较严谨,所以必须按照一部一部流程执行,这里得到cookie 和header
            # 首先执行, 收件箱页面
            s_url = 'http://mail.163.com/js6/main.jsp?' + sid + '&df=mail163_letter#module=' \
                                                                'mbox.ListModule%7C%7B%22fid%22%3A1%2C%22order%22%3A%22date%' \
                                                                '22%2C%22desc%22%3Atrue%7D'
            # headers['Cookie'] = cookiestr
            # req = requests.session()
            # req.headers = headers
            # req.cookies = cookie
            # req.get(s_url)
            # time.sleep(2)

            # print(req.cookies)
            # cookies = req.cookies

            # # print(cookies.items())
            # this = '; '.join(['='.join(item) for item in cookies.items()])
            # # dict((line.split('=') for line in this.strip().split(";")))
            # print('cookie', '; '.join(['='.join(item) for item in cookies.items()]))
            # # headers['Cookie'] = '; '.join(['='.join(item) for item in cookies.items()])
            # con = requests.get(con_url)

            yield Request(url=s_url, headers=headers, cookies=cookie, meta={'con_url': con_url, 'headers': headers, 'cookie': cookie}, callback=self.parse,  dont_filter=True)
        # yield scrapy.Request(url=self.start_urls[0], headers=self.headers, callback=self.parse)

    def parse(self, response):
        cookie = response.meta['cookie']
        # print(cookie)
        headers = response.meta['headers']
        con_url = response.meta['con_url']
        Cookie = response.request.headers.getlist('Cookie')
        print('Cookie', Cookie)
        # 响应Cookie
        Cookie = response.headers.getlist('Set-Cookie')
        print('Set-Cookie', Cookie)

        # print(response.body)
        # 打印原始数据
        # print(response.body.decode(response.encoding))
        yield Request(url=con_url, headers=headers, cookies=cookie, meta={'headers': headers, 'cookie': cookie}, callback=self.pase_xml, dont_filter=True)

    def pase_xml(self, response):
        cookie = response.meta['cookie']
        # print(cookie)
        headers = response.meta['headers']
        sellers = response.xpath('//object')  # 查询所有 邮件信息
        # http://mail.163.com/js6/read/readhtml.jsp?mid=57:1tbiOR0galXlZ6bG2AABsA&font=15&color=064977
        text_url = 'http://mail.163.com/js6/read/readhtml.jsp?mid=%s&font=15&color=064977'  # 最终详情页面信息
        for sel in sellers:
            subject = sel.xpath('string[@name="subject"]/text()').extract_first()  # 获取当前邮件头信息,以便筛选
            id = sel.xpath('string[@name="id"]/text()').extract_first()  # 获取当前ID 方便url传递
            print(subject)
            if subject:
                if '中国建设银行信用卡电子账单' in subject:
                    # 进行二级页面抓取
                    yield Request(url=text_url % id, headers=headers, cookies=cookie, callback=self.parse_deail, dont_filter=True)

    def parse_deail(self, response):
        wsi = WsScItem()
        wsi['card_num'] = response.xpath('//table[@width="875"]/tr[2]/td[1]/font/text()').extract_first().replace('\xa0', '')
        wsi['new_balance'] = response.xpath('//table[@width="875"]/tr[2]/td[3]/font/text()').extract_first().replace('\xa0', '')
        wsi['min_payment'] = response.xpath('//table[@width="875"]/tr[2]/td[4]/font/text()').extract_first().replace('\xa0', '')
        sumer = response.xpath('//table[@width="875"]/tr')
        price_lis = []
        for x in range(6, len(sumer) - 1):
            price_lis.append({
                'id': sumer[x].xpath('td[1]/font/text()').extract_first().replace('\xa0', ''),
                't_date': sumer[x].xpath('td[2]/font/text()').extract_first().replace('\xa0', ''),
                'p_date': sumer[x].xpath('td[3]/font/text()').extract_first().replace('\xa0', ''),
                'description': sumer[x].xpath('td[4]/font/text()').extract_first().replace('\xa0', ''),
                'curr_price': sumer[x].xpath('td[6]/font/text()').extract_first().replace('\xa0', ''),
            })
        wsi['price_detail'] = price_lis
        yield wsi

# http://mail.163.com
# 1.http://dl.reg.163.com/ini?pd=mail163&pkid=CvViHzl&pkht=mail.163.com&nocache=” ＋ 时间_取现行时间戳 ()
# 2.“http://dl.reg.163.com/gt?un=” ＋ User ＋ “&pkid=CvViHzl&pd=mail163&nocache=” ＋ 时间_取现行时间戳 ()
# 3.http://dl.reg.163.com/l
# 4.https://mail.163.com/entry/cgi/ntesdoor?
#
# 现在是第二步,{"ret":"201","tk":"6a82c2db8cf67f77088b942fef5d1657"},总是返回一个值,不会变动,原因在哪啊?
