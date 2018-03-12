# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
from selenium.webdriver.common.keys import Keys  # 需要引入keys包

chromedriver = "D:\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

# 使用谷歌浏览器，方便查看效果，如果追求速度可以用phantomJS
driver = webdriver.Chrome(chromedriver)
# driver=webdriver.Chrome()

# 调整最大窗口，否则某些元素无法显示
driver.maximize_window()
driver.get('https://login.taobao.com/member/login.jhtml')
time.sleep(2)
driver.find_element_by_id('J_Quick2Static').click()
driver.find_element_by_id("TPL_username_1").clear()
driver.find_element_by_id("TPL_username_1").send_keys("")

# tab的定位相相于清除了密码框的默认提示信息，等同上面的clear()
driver.find_element_by_id("TPL_username_1").send_keys(Keys.TAB)
time.sleep(1)
driver.find_element_by_id("TPL_password_1").send_keys("")

# 通过定位密码框，enter（回车）来代替登陆按钮
driver.find_element_by_id("TPL_password_1").send_keys(Keys.ENTER)
time.sleep(3)
try:
    driver.find_element_by_link_text("我的收货地址").click()
    time.sleep(3)
except Exception as e:
    print(e)
    # 定位滑块元素
    source = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")
    # 定义鼠标拖放动作
    ActionChains(driver).drag_and_drop_by_offset(source, 400, 0).perform()
    # 等待JS认证运行,如果不等待容易报错
    time.sleep(2)
    # 查看是否认证成功，获取text值
    text = driver.find_element_by_xpath("//div[@id='nc_1__scale_text']/span")
    # 目前只碰到3种情况：成功（请在在下方输入验证码,请点击图）；无响应（请按住滑块拖动)；失败（哎呀，失败了，请刷新）
    if text.text.startswith(u'请在下方'):
        print('成功滑动')
    if text.text.startswith(u'请点击'):
        print('成功滑动')
    if text.text.startswith(u'请按住'):
        pass

driver.find_element_by_link_text("我的收货地址").click()
time.sleep(3)
handles = driver.window_handles
driver.switch_to_window(handles[1])
print('默认地址:' + driver.find_element_by_css_selector(".thead-tbl-address.address-default").find_elements_by_tag_name("td")[2].text)
print('其余地址:')
total = len(driver.find_element_by_xpath("//table[@class='tbl-main']/tbody").find_elements_by_tag_name("tr"))
count = 1
while (count < total):
    count = count + 1
    print(driver.find_element_by_xpath("//table[@class='tbl-main']/tbody/tr[%s]/td[3]" % count).text)
driver.quit()