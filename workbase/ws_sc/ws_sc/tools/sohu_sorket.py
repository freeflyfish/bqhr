# coding: utf-8

import requests
import hashlib
from time import sleep, time
from selenium import webdriver
import re

from ws_sc.tools.http_socket import SocketUtil

jv_pattern = re.compile('\("(.*?)"\)', re.S)


def get_cookies_dict_from_webdriver(driver, sleep_time=0.1):
    return {cookie["name"]: cookie["value"] for cookie
            in get_cookies_list_from_webdriver(driver, sleep_time)}


def get_cookies_list_from_webdriver(driver, sleep_time=0.1):
    cookies_list = []
    for i in range(3):
        cookies_list = driver.get_cookies()
        if cookies_list:
            break
        else:
            sleep(sleep_time)
    return cookies_list


headers = {
    # # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # # 'Accept-Encoding': 'gzip, deflate, br',
    # # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # # 'Cache-Control': 'max-age=0',
    # # 'Connection': 'keep-alive',
    # # 'Host': 'mail.sohu.com',
    # 'P3P': "CP='CURa ADMa DEVa PSAo PSDo OUR BUS UNI PUR INT DEM STA PRE COM NAV OTC NOI DSP COR'",
    # 'Referer': 'https://mail.sohu.com/fe/',
    # # 'Upgrade-Insecure-Requests': '1',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    'Host': 'v4.passport.sohu.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://mail.sohu.com',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Referer': 'https://mail.sohu.com/fe/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

index_url = 'https://mail.sohu.com/fe/#/login'
driver = webdriver.PhantomJS('d:\\phantomjs.exe')
driver.get(index_url)
sleep(2)
driver.save_screenshot('1.jpg')
call_back_time = int(time() * 1E3)
conn_url = url_conn = "https://v4.passport.sohu.com/i/jf/code?callback=passport403_cb%s&type=0&_=%s" % (
    call_back_time, int(time() + 1))
sleep(2)
req_ss = requests.session()
# driver.get(conn_url)
cookies_dict = get_cookies_dict_from_webdriver(driver)
jv_conn = req_ss.get(conn_url, cookies=cookies_dict, verify=False)
jv = jv_pattern.findall(jv_conn.text)
dr_val = driver.execute_script('var val = %s; return val;' % jv[0])
cookies_dict.update({dr_val.split('=')[0]: dr_val.split('=')[1].split(';')[0]})
print(cookies_dict)

data = {
    'userid': 'xiongtaozt@sohu.com',
    'password': 'e2894b0ebe3626ae40bbef54e8182936',
    'appid': '101305',
    'callback': 'passport403_cb%s' % int(time()*1E3)
}

login_url = 'https://v4.passport.sohu.com/i/login/101305'
sock = SocketUtil()
res = req_ss.post(login_url, data=data, headers=headers, cookies=cookies_dict, verify=False)
print(res.cookies)
print(res.text)
list_url = 'https://mail.sohu.com/fe/folders?t=1515047670913'
# list_url = 'https://mail.sohu.com/fe/getList?offset=0&limit=20&folderId=1&order=id&sort=0&t=%s' % int(time() * 1E3)
call_back = req_ss.post('https://mail.sohu.com/fe/login/callback', cookies=cookies_dict, verify=False)
print(call_back.cookies.get_dict())
# print(call_back.text)
# cookies_dict.update(call_back.cookies.get_dict())
# list_res = req_ss.get(list_url, cookies=cookies_dict, verify=False)
# print(list_res.text)
#
# ppmdig = requests.get(
#     'https://v4.passport.sohu.com/i/jf/code?callback=passport403_cb1515121785513&type=0&_=1515122080437',
#     cookies=cookies_dict, verify=False)
# print(ppmdig.cookies.get_dict())
# cookies_dict.update(ppmdig.cookies.get_dict())
#
# print(cookies_dict)
# data = {
#     'userid': 'xiongtaozt@sohu.com',
#     'callback': 'passport403_cb%s' % int(time() * 1E3)
# }
# logout = 'https://v4.passport.sohu.com/i/logout/101305'
# log_res = requests.post(logout, cookies=cookies_dict, data=data, verify=False)
# print(log_res.text)
# login_res = req_ss.post(login_url, data=data, headers=headers)
# print(login_res.cookies)
# print(login_res.text)
driver.delete_all_cookies()
driver.quit()