# coding:utf-8

from selenium import webdriver
from selenium.webdriver.support import ui
import requests
from random import random as rand_0_1
from time import sleep

from requests_demo.test2 import parse_capatcha

username = 'zt193823'
password = 'scx1123'
headers = {
    'Referer': 'https://ipcrs.pbccrc.org.cn/top1.do',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
}
url = 'https://ipcrs.pbccrc.org.cn/page/login/loginreg.jsp'

dr = webdriver.PhantomJS(executable_path='D:\\phantomjs.exe')
wait = ui.WebDriverWait(dr, 20)
dr.get(url)
wait.until(lambda dr: dr.find_element_by_xpath("//input[@type='submit']"))
dr.maximize_window()
dr.execute_script("username_input=document.getElementById('loginname');"
                  "username_input.value='%s';"
                  "username_input.focus();" % username)
dr.execute_script("password_input=document.getElementById('password');"
                  "password_input.value='%s';"
                  "password_input.focus();" % password)
cookies = dr.get_cookies()
str_cookies = ';'.join([str(item['name'])+'='+ str(item['value']) for item in cookies])
print(str_cookies)
captcha_code = ''
headers['Cookie'] = str_cookies
while True:
    if len(captcha_code) == 6:
        break
    else:
        url = "https://ipcrs.pbccrc.org.cn/imgrc.do?" + str(rand_0_1())
        captcha_body = requests.get(url, headers=headers, verify=False)
        captcha_code = parse_capatcha(captcha_body.content)
print(captcha_code)
dr.execute_script("password_input=document.getElementById('_@IMGRC@_');"
                  "password_input.value='%s';"
                  "password_input.focus();" % captcha_code)

dr.execute_script('document.getElementsByClassName("inputBtn btn2")[0].click()')
# //a[text()='申请信用信息']
curr_url = dr.current_url
if curr_url == url:
    print('登陆失败')

dr.switch_to.frame('leftFrame')
wait.until(lambda dr: dr.find_element_by_xpath("//a[@id='infohelp']/span[text()='信息服务 >']"))
dr.execute_script('document.getElementById("infohelp").click()')
wait.until(lambda dr: dr.find_element_by_xpath("//a[text()='申请信用信息']"))
dr.execute_script("document.getElementsByTagName('ul')[1]."
                  "getElementsByTagName('li')[0]."
                  "getElementsByTagName('a')[0].click()")
dr.switch_to.default_content()
dr.switch_to.frame('mainFrame')
wait.until(lambda dr: dr.find_element_by_xpath("//input[@value='下一步']"))
dr.execute_script('document.getElementById("ApplicationOption3").checked="checked"')
dr.execute_script('document.getElementById("ApplicationOption2").checked="checked"')
dr.execute_script('document.getElementById("ApplicationOption1").checked="checked"')
dr.execute_script("submit_btn = document.getElementById('nextstep');"
                  "submit_btn.click();")
dr.switch_to.default_content()
dr.switch_to.frame('mainFrame')
wait.until(lambda dr: dr.find_element_by_xpath("//input[@id='gettradecode']"))
dr.execute_script("document.getElementById('gettradecode').click()")
print(dr.current_url)