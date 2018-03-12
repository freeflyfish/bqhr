#coding:utf-8
import requests

def login_lenovo():
    url = 'http://zhongce.lenovo.com.cn/index'
    square_url = 'http://zhongce.lenovo.com.cn/square'
    datas = {
    'lenovoid.action': 'diylogin',
    'lenovoid.realm': 'pcassistant.lenovo.com',
    'lenovoid.ctx': 'urlencodeCtx',
    'lenovoid.lang': 'null',
    'lenovoid.uinfo': 'null',
    'lenovoid.cb': 'http://zhongce.lenovo.com.cn/login/callback',
    'lenovoid.vb':'null',
    'lenovoid.display': 'null',
    'lenovoid.idp':'null',
    'lenovoid.source':'browser:zhongce.lenovo.com.cn',
    'crossRealmDomains':'passport.lenovomm.com,passport.lenovo.com,passport.lenovo.com.cn,passport.thinkworldshop.com.cn,passport.lenovo.cn,passport.lenovomobile.com,passport.motorola.com.cn,passport.thinkworld.com.cn',
    'isNeedPic':0,
    'sUrlRegister':'/wauthen2/wauth/jsp/register.jsp?lenovoid.action=diylogin&lenovoid.realm=pcassistant.lenovo.com&lenovoid.ctx=dXJsZW5jb2RlQ3R4&lenovoid.lang=null&lenovoid.uinfo=null&lenovoid.cb=http://zhongce.lenovo.com.cn/login/callback&lenovoid.vp=null&lenovoid.display=null&lenovoid_idp=null&lenovoid.source=browser:zhongce.lenovo.com.cn&lenovoid.thirdname=null&lenovoid.qrstate=null&lenovoid.idreinfo=null&lenovoid.hidewechat=1&lenovoid.hideqrlogin=1&lenovoid.hideautologin=0&lenovoid.hidelanguage=1&lenovoid.realmImg=null&lenovoid.loginTxt=null&lenovoid.mainColor=null&lenovoid.hideqq=1&lenovoid.hideloginreg=1&lenovoid.hidesina=1&lenovoid.hideregmobile=1&lenovoid.hideregemail=1&lenovoid.hidesmslogin=1&lenovoid.webstate=0&lenovoid.userType=null&lenovoid.uAgreementTxt=null&lenovoid.uAgreementUrl=null&lenovoid.sdk=null&lenovoid.sn=null',
    'path':'/wauthen2',
    'username':'912085065@qq.com',
    'password':'92211Yao',
    'c':'',
    't':'16121843462851061810',
    }
    # 根据抓包信息 构造表单
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'Cookie:invtest=953857cf52fa9141f091e07a5ee7a30c02430b66a905bf5d5c0c4f8e87e23242ab06c545; LPSState=1; LenovoID.UN=13029452117',
    'Host':'zhongce.lenovo.com.cn',
    'Referer':'http://zhongce.lenovo.com.cn/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }

    sessions = requests.session()
    response = sessions.post(url, headers=headers, data=datas)
    print(response.text)
    # res_square = sessions.get(square_url, headers=headers)
    #
    # print(res_square.text)

login_lenovo()