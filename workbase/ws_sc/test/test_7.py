# coding:utf-8

from selenium import webdriver
from time import sleep
from lxml import etree
from re import sub
from urllib.parse import unquote
import requests
import json
import jsbeautifier

driver = webdriver.Chrome(executable_path='D:\\chromedriver.exe')

driver.get('http://www.ipe.org.cn/MapWater/water.aspx?q=2')
sleep(2)

session = requests.session()
# session.cookies = driver.get_cookies()
value = driver.get_cookie('ajaxkey')['value']

headers = {
    'Cookie': 'ajaxkey=%s' % value,
    'Host': 'www.ipe.org.cn',
    'Origin': 'http://www.ipe.org.cn',
    'Referer': 'http://www.ipe.org.cn/MapWater/water.aspx?q=2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
session.headers = headers
data = {
    'headers[Cookie]': value,
    'cmd': 'gethch_content',
}

html = etree.HTML(driver.page_source)
trs = html.xpath('//table[@class="table-list"]/tbody/tr')
for x in range(len(trs)):
    print(trs[x].xpath('td[3]/a/text()')[0])
    print(sub('\s+', '', trs[x].xpath('td[1]/text()')[0]))
    print(sub('\s+', '', trs[x].xpath('td[2]/text()')[0]))
    print(sub('\s+', '', trs[x].xpath('td[3]/a/text()')[0]))
    print(sub('\s+', '', trs[x].xpath('td[4]/text()')[0]))
    data['mid'] = trs[x].xpath('td[3]/a/@href')[0].split('(')[-1][:-2]
    res = session.post(url='http://www.ipe.org.cn/data_ashx/GetAirData.ashx', data=data)
    con = json.loads(res.content)['Content']
    # 通过urllib解密js混淆加密
    con_html = unquote(con)
    com_xpath = etree.HTML(con_html)
    tr_count = com_xpath.xpath('//tbody/tr')
    for i in range(len(tr_count)):
        try:
            print(eval("u'%s'" % sub('%(u[0-9a-zA-Z]{4})', r'\\' + "\g<1>", sub('\s+', '', tr_count[i].xpath('th/text()')[0]))))
            print(eval("u'%s'" % sub('%(u[0-9a-zA-Z]{4})', r'\\' + "\g<1>", sub('\s+', '', tr_count[i].xpath('td/text()')[0]))))
        except Exception:
            pass
# driver.quit()

# sj = '%20%3Cdiv%20class%3D%22side-con%22%3E%0D%0A%3Cdiv%20class%3D%22section-info%22%3E%0D%0A%3Cdiv%20class%3D%22table-con%20table-selection%22%3E%0D%0A%3Cdiv%20class%3D%22table-main%22%3E%0D%0A%3Ctable%20class%3D%22table-list%22%3E%0D%0A%3Ctbody%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u9ED1%u81ED%u7A0B%u5EA6%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%u8F7B%u5EA6%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u6240%u5728%u5730%u533A%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%u5317%u4EAC-%u5317%u4EAC%u5E02%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u9ED1%u81ED%u6CB3%u6BB5%u8D77%u70B9%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%u901A%u9A6C%u8DEF%u6865%u4E0B%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u9ED1%u81ED%u6CB3%u6BB5%u7EC8%u70B9%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%u5165%u8427%u592A%u540E%u6CB3%u6BB5%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u957F%u5EA6%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A0%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u9762%u79EF%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u8D23%u4EFB%u4EBA%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%u5F20%u79C0%u6377%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u7535%u8BDD%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A60524515%u300161532389%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u6CBB%u7406%u65F6%u9650%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%u5165%u8427%u592A%u540E%u6CB3%u6BB5%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u6CBB%u7406%u8FDB%u5EA6%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%u5F00%u5DE5%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Ctd%20colspan%3D%222%22%20class%3D%22text-left%20water-pic-case%22%3E%0D%0A%3Cdiv%20class%3D%22water-pic%22%20id%3D%22pic_list%22%3E%0D%0A%3Cul%20class%3D%22clearfix%22%3E%0D%0A%3C/ul%3E%0D%0A%3C/div%3E%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3C/tbody%3E%0D%0A%3C/table%3E%0D%0A%3C/div%3E%0D%0A%3C/div%3E%0D%0A%3Cdiv%20class%3D%22side-source%22%3E%0D%0A%3Cp%3E%0D%0A%u6570%u636E%u6765%u6E90%3A%u5168%u56FD%u57CE%u5E02%u9ED1%u81ED%u6C34%u4F53%u6574%u6CBB%u4FE1%u606F%u5E73%u53F0%3C/p%3E%0D%0A%3C/div%3E%0D%0A%3C/div%3E%0D%0A%3C/div%3E%0D%0A'
#
# from lxml.html import fromstring
# from bs4 import BeautifulSoup as bs_format
# from urllib.parse import unquote
# # import jsbeautifier
# print(bytes.decode('\u9ED1\u81ED\u7A0B\u5EA6'.encode('utf-8')))
# page = unquote(sj)
# html = etree.HTML(page)
# trs = html.xpath('//tbody/tr')
# # import re
# # s = "\u9ED1\u81ED\u7A0B\u5EA6"
# # print(s)
# # res = re.sub('%(u[0-9a-zA-Z]{4})', r'\\' + "\g<1>", s)
# # print(res)
# # res = eval("u'%s'" % res)
# # print(res)
#
#
# for x in range(len(trs)):
#     try:
#         print(eval("u'%s'" % sub('%(u[0-9a-zA-Z]{4})', r'\\' + "\g<1>", sub('\s+', '', trs[x].xpath('th/text()')[0]))))
#         print(eval("u'%s'" % sub('%(u[0-9a-zA-Z]{4})', r'\\' + "\g<1>", sub('\s+', '', trs[x].xpath('td/text()')[0]))))
#         # print(("u'%s'" % trs[x].xpath('th/text()')[0]).replace('%', '\\').encode('utf-8'))
#     except Exception:
#         pass
