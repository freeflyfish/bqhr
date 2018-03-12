# coding:utf-8


import cv2
import numpy
from PIL import Image
from piltesseract import get_text_from_image
from string import digits, ascii_letters
from re import compile as re_compile, S as re_S
from io import BytesIO

import requests
from lxml import etree
from random import random as rand_0_1
from selenium import webdriver


def parse_capatcha(captcha_body):
    with BytesIO(captcha_body) as captcha_filelike, Image.open(captcha_filelike) as img:
        # img.show()

        # 构造算子为32位浮点三维矩阵kernel：[(1 / 20, 1 / 20, 1 / 20, 1 / 20, 1 / 20)
        #                      (1 / 20, 1 / 20, 1 / 20, 1 / 20, 1 / 20)
        #                      (1 / 20, 1 / 20, 1 / 20, 1 / 20, 1 / 20)
        #                      (1 / 20, 1 / 20, 1 / 20, 1 / 20, 1 / 20)
        #                      (1 / 20, 1 / 20, 1 / 20, 1 / 20, 1 / 20)]
        # kernel = numpy.ones((5, 5), numpy.float32) / 19
        # sobelX = numpy.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        # sobelY = numpy.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        # kernel = numpy.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

        # 做卷积去噪点
        eroded = numpy.array(img)
        eroded = cv2.fastNlMeansDenoisingColored(eroded)

        mask_img_arr = numpy.zeros((eroded.shape[0], eroded.shape[1]), numpy.uint8)
        dst_img = numpy.array(img)
        cv2.inpaint(eroded, mask_img_arr, 10, cv2.INPAINT_TELEA, dst=dst_img)

        # 图像灰度化处理
        eroded = cv2.cvtColor(eroded, cv2.COLOR_BGR2GRAY)

        # 图像二值化处理
        ret, eroded = cv2.threshold(eroded, 125, 255, cv2.THRESH_BINARY)

        dest_img = Image.fromarray(eroded)
        code = get_text_from_image(dest_img,
                                   tessedit_char_whitelist=digits + ascii_letters).replace(' ', '')
        dest_img.close()

    return code


headers = {
    'Referer': 'https://ipcrs.pbccrc.org.cn/top1.do',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
}
# ff99a149769c8e6b683f6dff90210803  caaa9eb0d51c416ecc35845357f507a4
# data = {
#     'method': 'getAcvitaveCode',
#     'mobileTel': '18702898679'
# }

# datas = {"org.apache.struts.taglib.html.TOKEN": token or "",
#              "method": "checkIdentity",
#              "_@IMGRC@_": captcha_code,
#              "userInfoVO.name": '刘力',
#              "userInfoVO.certType": '0',
#              "userInfoVO.certNo": '511324199408071339',
#              "1": "on",
#              }

# html = requests.post(url='https://ipcrs.pbccrc.org.cn/userReg.do', data=data, headers=headers, verify=False)
# print(html.cookies)
# print(html.text)
# x = etree.HTML(html.content)
# l = x.xpath("//input[@name='org.apache.struts.taglib.html.TOKEN']/@value")
# print(l[0])
# req_ses = requests.session()
# login1 = req_ses.get(url='https://ipcrs.pbccrc.org.cn/page/login/loginreg.jsp', headers=headers, verify=False)
# # token = etree.HTML(login1.text).xpath("//input[@name='org.apache.struts.taglib.html.TOKEN']/@value")[0]
# vcode = ''
# cookies = req_ses.cookies.get_dict()
# while True:
#     if len(vcode) == 6:
#         break
#     else:
#         url = "https://ipcrs.pbccrc.org.cn/imgrc.do?" + str(rand_0_1())
#         captcha_body = req_ses.get(url, headers=headers, verify=False)
#         vcode = parse_capatcha(captcha_body.content)
# print(vcode)

# datas = {"org.apache.struts.taglib.html.TOKEN": token or "",
#          "method": "checkIdentity",
#          "userInfoVO.name": '张晓瑶'.encode('gb2312', 'replace'),
#          "userInfoVO.certType": '0',
#          "userInfoVO.certNo": '371425199202116824',
#          "_@IMGRC@_": vcode,
#          "1": "on",
#          }
# print(datas)
# url = "https://ipcrs.pbccrc.org.cn/userReg.do"
# headers['Referer'] = 'https://ipcrs.pbccrc.org.cn/userReg.do?method=initReg'
# response = requests.post(url, data=datas, headers=headers, verify=False, cookies=cookies)
# print(response.text)
#
#
# cookies = response.cookies.get_dict()
# data = {
#         'method': 'getAcvitaveCode',
#         'mobileTel': '18328530785'
#     }
# headers['Referer'] = 'https://ipcrs.pbccrc.org.cn/userReg.do'
# phcode = requests.post(url=url, data=data, headers=headers, verify=False, cookies=cookies)
# print(phcode.text)
# token = etree.HTML(login1.text).xpath("//input[@name='org.apache.struts.taglib.html.TOKEN']/@value")[0]
#
# verifyCode = input('>')
# datas = {
#         'org.apache.struts.taglib.html.TOKEN': token or '',
#         'method': ' saveUser',
#         'counttime': '1',
#         'tcId': phcode,
#         'userInfoVO.loginName': 'zxy116824',
#         'userInfoVO.password': 'scx1123',
#         'userInfoVO.confirmpassword': 'scx1123',
#         'userInfoVO.email': '912085065@qq.com',
#         'userInfoVO.mobileTel': '18328530785',
#         'userInfoVO.verifyCode': verifyCode,
#         'userInfoVO.smsrcvtimeflag': '2'
#     }
# res = requests.post(url=url, data=datas, headers=headers,  verify=False, cookies=cookies)
# print(res.text)

# username = 'zt193823'
# password = 'scx1123'
# login_url = 'https://ipcrs.pbccrc.org.cn/page/login/loginreg.jsp'
# response = req_ses.get(url=login_url, headers=headers, verify=False)
# response = etree.HTML(response.text)
# token = response.xpath("//input[@name='org.apache.struts.taglib.html.TOKEN']/@value")[0]
# date = response.xpath("//input[@name='date']/@value")[0]
# captcha_code = ''
# while True:
#     if len(captcha_code) == 6:
#         break
#     else:
#         url = "https://ipcrs.pbccrc.org.cn/imgrc.do?" + str(rand_0_1())
#         captcha_body = req_ses.get(url, headers=headers, verify=False)
#         captcha_code = parse_capatcha(captcha_body.content)
# print(captcha_code)
# datas = {
#     "method": "login",
#     "date": date,
#     "loginname": username,
#     "password": password,
#     "_@IMGRC@_": captcha_code
# }
# headers['Referer'] = login_url
# result = req_ses.post(url='https://ipcrs.pbccrc.org.cn/login.do', data=datas, headers=headers, verify=False)
# print(result.text)
# cookies = req_ses.cookies.get_dict()
# dr = webdriver.Chrome(executable_path='D:\\chromedriver.exe')
# for k, v in cookies.items():
#     dr.add_cookie({'name': k, 'value': v})
#
# # response = req_ses.get('https://ipcrs.pbccrc.org.cn/unionpayAction.do', verify=False)
# # print(response.text)
# dr.get('https://ipcrs.pbccrc.org.cn/reportAction.do?method=applicationReport')










# url = 'https://ipcrs.pbccrc.org.cn/reportAction.do?method=applicationReport'
# headers['Referer'] = 'https://ipcrs.pbccrc.org.cn/menu.do'
# report_action = requests.get(url=url, headers=headers, cookies=cookies, verify=False)
# print(report_action.text)
# token = etree.HTML(report_action.text).xpath("//input[@name='org.apache.struts.taglib.html.TOKEN']/@value")[0]
#
# # 获取答题信息
# data = {
#     'method': 'checkishasreport',
#     'org.apache.struts.taglib.html.TOKEN': token,
#     'authtype': '2',
#     'ApplicationOption': '25',
#     'ApplicationOption': '24',
#     'ApplicationOption': '21',
# }
# url = 'https://ipcrs.pbccrc.org.cn/reportAction.do'
# checkishasreport = requests.post(url=url, data=data, headers=headers, cookies=cookies, verify=False)
# print(checkishasreport.text)
