# coding:utf-8

from selenium import webdriver


dr = webdriver.Ie(executable_path='D:\\IEDriverServer_233.exe')
dr.get('https://nper.cmbc.com.cn/pweb/static/login.html')

# text = dr.find_element_by_id('kBaobtn').text
# print(text)
# error = dr.find_element_by_class_name('logon-error')
# print(error)
#
# print(error.get_attribute('title'))
# print('main.html' not in 'https://nper.cmbc.com.cn/pweb/static/login.html')
d = dr.find_element_by_xpath("//form[@class='WellForm v-pristine v-valid']/h3")
print(d.text)
