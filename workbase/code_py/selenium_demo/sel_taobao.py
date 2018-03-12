# coding:utf-8

from selenium import webdriver
from selenium.webdriver.support import ui
import time
from selenium_demo.utils.utils import *

username = 'xiongtaox123'

password = 'scx1123'

driver = webdriver.Chrome(executable_path='D:\\chromedriver.exe')

wait = ui.WebDriverWait(driver, 20)

driver.get('https://login.taobao.com/member/login.jhtml')


# 尝试使用二维码登陆
# 将二维码存储在本地,本地使用手机登陆淘宝
wait.until(lambda dr: dr.find_element_by_xpath('//button[@id="J_SubmitStatic"]'))

# driver.execute_script('document.getElementById("J_Quick2Static").click();')  # 防止不是转跳的密码登陆页面

# 存储二维码图片

captcha_image = driver.find_element_by_xpath('//div[@id="J_QRCodeImg"]/img')
location = captcha_image.location
size = captcha_image.size
left = location["x"] - 8
top = location["y"]
right = left + size["width"]
bottom = top + size["height"]

photo_base64 = driver.get_screenshot_as_base64()
captcha_body = driver_screenshot_2_bytes(photo_base64, (left, top, right, bottom))

with open('rwm.png', 'wb') as f:
    f.write(captcha_body)
    f.close()

# 开始登陆
# driver.execute_script('username = document.getElementById("TPL_username_1");'
#                       'username.value="%s";username.focus();' % username)
# time.sleep(0.2)
# driver.execute_script('passwd = document.getElementById("TPL_password_1");'
#                       'passwd.value="%s";passwd.focus();' % password)
#
# driver.execute_script('document.getElementById("J_SubmitStatic").click()')
#
# wait.until(lambda dr: dr.find_element_by_xpath('//li[text()="我已经买到的宝贝"]'))
