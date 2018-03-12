# coding:utf-8
from lxml import etree
import requests
# lis = [{'domain': 'ipcrs.pbccrc.org.cn', 'httpOnly': False, 'name': 'TSf75e5b', 'path': '/', 'secure': False, 'value': '52b83869bc9afcd1ab7b9cae2ecea42aaf8ff938f753277e59ae0c06'}, {'domain': 'ipcrs.pbccrc.org.cn', 'httpOnly': True, 'name': 'BIGipServerpool_ipcrs_app', 'path': '/', 'secure': True, 'value': '6To5BoeC390kUTkvb+H7Of3zy4BZ/4Cp/KquP7rKrwtAEswd/M7lbFQISLf7pSHkJHXDkHW+2iV35qFVrMmbDHhOxcn7C/AMAG1As4+K7yfyfouDTKBM0CFUx+98hPK+dH541GVL++eUMc2gbVWFJ2zmUqgRGw=='}, {'domain': 'ipcrs.pbccrc.org.cn', 'httpOnly': False, 'name': 'JSESSIONID', 'path': '/', 'secure': False, 'value': 'Gm1WZnMGX5CsPDCB8sC26N244ttt9BFj2HHhH1sYV9CgMRTDpn8l!-456774902'}, {'domain': 'ipcrs.pbccrc.org.cn', 'httpOnly': True, 'name': 'BIGipServerpool_ipcrs_web', 'path': '/', 'secure': True, 'value': '+xs2zqntf4jpYFAvb+H7Of3zy4BZ/4SgLzTrYkdVz5XZRtGCNhkXRCxCQg5ZwyTt6l+vBD/RZ0vE'}]
#
# str_cookies = ''
# # for i in lis:
# #     str_cookies += str(i['name']) + '=' + str(i['value']) + ';'
# str_cookies = ';'.join([str(item['name'])+'='+ str(item['value']) for item in lis])
# print(str_cookies)

headers = {
    'Referer': 'https://ipcrs.pbccrc.org.cn/top1.do',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
}

# headers['Referer'] = 'https://ipcrs.pbccrc.org.cn/page/login/loginreg.jsp'
# url = "https://ipcrs.pbccrc.org.cn/findLoginName.do?method=init"
# req_ses = requests.session()
# res = req_ses.get(url=url, headers=headers, verify=False)
# print(res.text)
# data = {
#
# }
ss = '''<li class="margin_top_20 height32">
			            <font class="regist_text span-14">手机号码：</font>
			            <span class="user_text span-14 span-grey">187*****679</span>
			        </li>'''
s = etree.HTML(ss).xpath('//span[@class="user_text span-14 span-grey"]/text()')[0]
print(s)

import random
# 86934465
print(int(random.random()*(100000000)))