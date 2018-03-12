# coding: utf-8

from selenium import webdriver
from selenium.webdriver.support import ui
from lxml import etree
import time
import requests

driver = webdriver.Chrome(executable_path='D:\\chromedriver.exe')

try:

    wait = ui.WebDriverWait(driver, 20)

    driver.get('http://zhongce.lenovo.com.cn/index')

    wait.until(lambda dr: dr.find_element_by_xpath('//a[@class="lenovo-login"]'))

    # 登陆
    driver.execute_script('document.getElementsByClassName("lenovo-login")[0].click()')

    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@class="testiframe jsIframe"]'))

    driver.execute_script('user = document.getElementById("tuser");'
                          'user.value=%s;user.focus();' % '13029452117')

    driver.find_element_by_xpath('//input[@name="password"]').send_keys('92211Yao')

    driver.execute_script('document.getElementsByClassName("jsSubBtn")[0].click()')

    wait.until(lambda dr: dr.find_element_by_xpath('//li[@ref-link="/square"]/a[text()="产品广场"]'))

    driver.find_element_by_xpath('//li[@ref-link="/square"]/a[text()="产品广场"]').click()

    products_html = etree.HTML(driver.page_source)
    pro_urls = products_html.xpath('//div[@class="lieBox"]/@ref-link')
    # 获取cookie 并且解析cookie
    cookies = driver.get_cookies()
    cookie = {}
    for s in cookies:
        cookie[s['name']] = s['value']

    # 开始获取 产品页面信息
    if pro_urls:
        for pro_url in pro_urls:
            detail_url = 'http://zhongce.lenovo.com.cn/api/product/feedbacks?product_id=%s&page_num=1&per_page=10&_=%s' % (pro_url.split('/')[-1], str(int(time.time()*1000)))
            result = requests.get(detail_url, cookies=cookie)
            print(result.text)
            print('*' * 50)
except Exception as e:
    print(e)
finally:
    driver.quit()