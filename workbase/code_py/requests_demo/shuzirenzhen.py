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


username = 'xt123831'
password = 'scx1123'


headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 60.0.3112.90Safari / 537.36',
    }
req_ses = requests.session()

login_url = 'https://ipcrs.pbccrc.org.cn/page/login/loginreg.jsp'
response = req_ses.get(url=login_url, headers=headers, verify=False)
response = etree.HTML(response.text)
# token = response.xpath("//input[@name='org.apache.struts.taglib.html.TOKEN']/@value")[0]
date = response.xpath("//input[@name='date']/@value")[0]
captcha_code = ''
while True:
    if len(captcha_code) == 6:
        break
    else:
        url = "https://ipcrs.pbccrc.org.cn/imgrc.do?" + str(rand_0_1())
        captcha_body = req_ses.get(url, headers=headers, verify=False)
        captcha_code = parse_capatcha(captcha_body.content)
print(captcha_code)
datas = {"org.apache.struts.taglib.html.TOKEN":  "",
         "method": "login",
         "date": date,
         "loginname": username,
         "password": password,
         "_@IMGRC@_": captcha_code
        }
headers['Referer'] = login_url
result = req_ses.post(url='https://ipcrs.pbccrc.org.cn/login.do', data=datas, headers=headers, verify=False)
print(result.text)