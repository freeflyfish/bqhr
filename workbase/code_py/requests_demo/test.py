# coding:utf-8

import requests
from lxml import etree
from selenium import webdriver
from time import sleep

headers = {
        'Referer': 'https://ipcrs.pbccrc.org.cn/page/login/loginreg.jsp',
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 60.0.3112.90Safari / 537.36',
    }
dr = webdriver.Chrome(executable_path='D:\\chromedriver.exe')
try:
    dr.get('https://ipcrs.pbccrc.org.cn/page/login/loginreg.jsp')
    sub = dr.find_element_by_xpath('//form[@name="userForm"]/div/div/input')
    sub.click()
    sleep(1)
    token = dr.find_element_by_xpath("//input[@name='org.apache.struts.taglib.html.TOKEN']").get_attribute('value')
    captcha_code = input('>')
    id_no = ''
    cookies = {}
    while True:
        list_cookies = dr.get_cookies()  # 这里返回的是一个更多信息的字典列表
        for s in list_cookies:
            cookies[s['name']] = s['value']
        print(cookies)
        if cookies.has_key('BAIDUID'):
            break
        sleep(2)
    sn = requests.Session()
    datas = {"org.apache.struts.taglib.html.TOKEN": token or "",
             "method": "checkIdentity",
             "_@IMGRC@_": captcha_code,
             "userInfoVO.name": '刘力',
             "userInfoVO.certType": '0',
             "userInfoVO.certNo": '511324199408071339',
             "1": "on",
             }
    html = requests.post(url='https://ipcrs.pbccrc.org.cn/userReg.do', cookies=cookies, headers=headers, verify=False)
    print(html.content)
except Exception:
    pass
finally:
    dr.close()