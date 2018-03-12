import requests
import re
from urllib.parse import quote
from selenium import webdriver


def encode_password(password):
    """
    加密密码
    :param password:
    :return:
    """
    try:
        url = "https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlat_09?SERVLET_NAME=B2CMainPlat_09&CCB_IBSVersion=V6&" \
              "PT_STYLE=1&CUSTYPE=0&TXCODE=CLOGIN&DESKTOP=0&EXIT_PAGE=login.jsp&WANGZHANGLOGIN=&FORMEPAY=2"
        ifUseYinshe = '1'
        encode_pwd = ""

        response = requests.get(url)
        page = response.content.decode("utf-8")
        a = re.search("a\|(.+?)\|b", page).group(1)
        print("A:%s" % a)
        b = get_b_value(page)
        if not b:
            return

        newValue = password
        specialChar = 0
        if ifUseYinshe == "1":
            everyone = ''
            afterPass = ''
            for i in range(len(newValue)):
                if specialChar == 1:
                    break
                everyone = newValue[i]
                for j in range(len(b) // 2):
                    if everyone == b[2 * j]:
                        afterPass = afterPass + b[2 * j + 1]
                        break
                    if j == len(b) // 2 - 1:
                        if everyone != b[2 * j]:
                            specialChar = 1
                            break
            if specialChar == 0:
                encode_pwd = afterPass
            else:
                ret = ""
                afterPass = ''
                for i in range(len(newValue)):
                    c = newValue[i]
                    ts = quote(c)
                    if ts[:2] == "%u":
                        ret = ret + ts.replace("%u", "(^?)")
                    else:
                        ret += c
                encode_pwd = ret
                for n in range(len(ret)):
                    everyone = ret[n]
                    for w in range(len(b) // 2):
                        if everyone == b[2 * w]:
                            afterPass = afterPass + b[2 * w + 1]
                            break
                encode_pwd = afterPass
        return encode_pwd
    except Exception as e:
        # self.logger.exception("加密密码失败:%s" % str(e))
        print(e)
        return


def get_b_value(page):
    """
    获取b的值
    :param page:
    :return:
    """
    try:
        eval_str = re.search('(eval[\s\S]+?)function check_bfr_submit', page)
        if eval_str is not None:
            eval_str = eval_str.group(1).strip()
        else:
            return
        eval_js = eval_str.replace("eval", "document.write")
        driver = webdriver.PhantomJS(executable_path='D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
        driver.execute_script(eval_js)  # 解密JS
        de_js_str = driver.page_source
        print("Js:%s" % de_js_str)
        reg = re.compile(r"b\[\d+\]='(.+?)';", re.S)
        b_list = reg.findall(de_js_str)
        if b_list and len(b_list) > 0:
            return b_list
        print("获取值失败:%s" % str(b_list))
        return
    except Exception as e:
        print("获取值出错:%s" % str(e))
        return

# print('the password is', encode_password('pm988355'))