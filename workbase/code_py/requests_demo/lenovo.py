# coding:utf-8
import requests
import json
from lxml import etree


def login_lenovo():
    url = 'http://zhongce.lenovo.com.cn/index'
    login_div = 'http://passport.lenovo.com.cn/wauthen2/wauth/jsp/ilogin.jsp?lenovoid.action=diylogin&lenovoid.realm=pcassistant.lenovo.com&lenovoid.action=uilogin&lenovoid.ctx=urlencodeCtx&lenovoid.lang=null&lenovoid.cb=http://zhongce.lenovo.com.cn/login/callback&lenovoid.source=browser:zhongce.lenovo.com.cn&lenovoid.hidewechat=1&lenovoid.hidesina=1&lenovoid.hideqq=1&lenovoid.hideautologin=0&lenovoid.hideqrlogin=1&lenovoid.hidesmslogin=1&lenovoid.hidecommonlogin=1&lenovoid.hideregemail=1&lenovoid.hideregmobile=1'
    square_url = 'http://zhongce.lenovo.com.cn/square'
    login_url = 'http://passport.lenovo.com.cn/wauthen2/ajaxUserLogin'

    # 根据抓包信息 构造表单
    headers = {
        'Referer': 'http://zhongce.lenovo.com.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }

    headers2 = {
        'Host': 'zhongce.lenovo.com.cn',
        'Connection': 'keep - alive',
        'Upgrade - Insecure - Requests': '1',
        'User-Agent': 'Mozilla/5.0(Windows NT 6.1;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome / 61.0.3163.100Safari / 537.36',
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        'Referer': 'http://zhongce.lenovo.com.cn/index',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh - CN, zh;q = 0.8',
    }

    sessions = requests.session()
    sessions.get(url, headers=headers)
    index = sessions.get(login_div)
    index_html = etree.HTML(index.text)
    datas = {
        'lenovoid.action': index_html.xpath('//input[@name="lenovoid.action"]/@value')[0],
        'lenovoid.realm': index_html.xpath('//input[@name="lenovoid.realm"]/@value')[0],
        'lenovoid.ctx': index_html.xpath('//input[@name="lenovoid.ctx"]/@value')[0],
        'lenovoid.lang': index_html.xpath('//input[@name="lenovoid.lang"]/@value')[0],
        'lenovoid.uinfo': index_html.xpath('//input[@name="lenovoid.uinfo"]/@value')[0],
        'lenovoid.cb': index_html.xpath('//input[@name="lenovoid.cb"]/@value')[0],
        'lenovoid.vb': index_html.xpath('//input[@name="lenovoid.vb"]/@value')[0],
        'lenovoid.display': index_html.xpath('//input[@name="lenovoid.display"]/@value')[0],
        'lenovoid.idp': index_html.xpath('//input[@name="lenovoid.idp"]/@value')[0],
        'lenovoid.source': index_html.xpath('//input[@name="lenovoid.source"]/@value')[0],
        'crossRealmDomains': index_html.xpath('//input[@name="crossRealmDomains"]/@value')[0],
        'isNeedPic': index_html.xpath('//input[@name="isNeedPic"]/@value')[0],
        'sUrlRegister': index_html.xpath('//input[@name="sUrlRegister"]/@value')[0],
        'path': index_html.xpath('//input[@name="path"]/@value')[0],
        'username': '13029452117',
        'password': '92211Yao',
        'c': '',
        't': '16121843462851061810',
    }
    response = sessions.post(login_url, data=datas, verify=False)
    conn = json.loads(response.text)
    print(sessions.cookies.get_dict())
    lov_url = 'http://zhongce.lenovo.com.cn/api/lenovo/login'
    files = {'ticket': (None, conn['lpsust']),
             "realm": (None, 'pcassistant.lenovo.com')
    }
    headers['Content-Type'] = 'multipart/form-data; boundary=----WebKitFormBoundarynWWmgz9xtv7SrWJ4'

    t = sessions.post(lov_url, files=files, headers=headers)
    print(t.text)
    # headers2['Cookie'] = 'invtest=953857cf52fa9141f091e07a5ee7a30c02430b66a905bf5d5c0c4f8e87e23242ab06c545'
    # res_square = requests.get(square_url, cookies=sessions.cookies.get_dict(), headers=headers2, verify=False)
    # print(res_square.text)


login_lenovo()
