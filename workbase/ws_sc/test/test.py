# coding:utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

# 1501032730789
# 1501033005927
# print(int(time.time()*1000))

# T7iMKq2AyKlvMhYg/UMl9zTYs4I4jWRNwqexh67G0D/MX+84te/XzJtrwuwwSX8gZ3EVQAol9YzF0ljZ8Z2Y7hqtHWK+UZM1DnrUEqNgsd3Rd2wDTD44GHsdFaGTWxdz0Tw2oEdYVNrenH861FQlX2TZTerlW9GuK1wbvilY78Y=
# ihTtguRdUtnEsZhkjawtVtp2zg6bZZ+gNlakt5mNwa0TKrNZ7rXhV2zOj/mzg62k+ttvNPvP+jQKqIQPyJB/wGKbxt5wlkoTTEbWWc4tHgO7JOKEHHK6LVUuzk/LKdUMY23n+87ccDW09SY824TlkEQq/hPcdGwfcCiDRqIG//c=


driver = webdriver.Chrome(executable_path='D:\\chromedriver.exe')
# driver.get('http://email.163.com/')
# time.sleep(5)
# print(driver.page_source)
# elem_user = driver.find_element_by_name("userNameIpt")
# elem_user.send_keys("xiongtaozz")
# elem_pwd = driver.find_element_by_name("password")
# elem_pwd.send_keys("scx1123")
# elem_pwd.send_keys(Keys.RETURN)
# time.sleep(5)
# assert "baidu" in driver.title

# driver = webdriver.Chrome()
# 大化窗口
# driver.maximize_window()
url = 'http://mail.163.com/'
driver.get(url)
time.sleep(2)
# 切换到表单
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys('xiongtaozz')
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys('scx1123')
driver.find_element_by_id("dologin").click()
# 判断url是否改变如果改变,那么登录成功
# 登录失败则,返回重新登录
time.sleep(3)
curr_url = driver.current_url
print(curr_url)
if url == curr_url:
    # 说明未登录成功
    pass
# 获取cookie信息
cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
# 打印
cookiestr = ';'.join(item for item in cookie)
print(cookiestr)
# driver.close()
# driver.quit()
# 收件箱页面
# http://mail.163.com/js6/main.jsp?sid=pBcSiePLJkzEkmbVdWLLvWLBdgIuBWNn&df=mail163_letter#module=mbox.ListModule%7C%7B%22fid%22%3A1%2C%22order%22%3A%22date%22%2C%22desc%22%3Atrue%7D
# http://mail.163.com/js6/main.jsp?sid=RCzajBCarYXrcNkKuKaalNlHcWTlAHUC&df=mail163_letter#module=mbox.ListModule%7C%7B%22fid%22%3A1%2C%22order%22%3A%22date%22%2C%22desc%22%3Atrue%7D
# 所有收件箱标题信息
# http://mail.163.com/js6/s?sid=RCfqyBCauScrcNdSyKaaUEHPAOAiHemC&func=mbox:listMessages
sid = curr_url.split('?')[1].split('&')[0]
con_url = 'http://mail.163.com/js6/s?%s&func=mbox:listMessages' % sid

# 模拟头信息
headers = {
    'Content-type': 'application/x-www-form-urlencoded',
    'Host': 'mail.163.com',
    'Origin': 'http://mail.163.com',
    'Referer': 'http://mail.163.com/js6/main.jsp?%s&df=mail163_letter' % sid,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3050.3 Safari/537.36',
}

# headers['Cookie'] = cookiestr
# # con = requests.get(con_url, headers)
# # print(con.content)
# s_url = 'http://mail.163.com/js6/main.jsp?'+sid+'&df=mail163_letter#module=' \
#                                                 'mbox.ListModule%7C%7B%22fid%22%3A1%2C%22order%22%3A%22date%' \
#                                                 '22%2C%22desc%22%3Atrue%7D'
# print(s_url)
# print(con_url)
# req = requests.session()
# req.headers = headers
# req.get(s_url)
# con = req.get(con_url)
# print(con.content)

