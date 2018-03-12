# -*- coding:utf-8 -*-

import requests
import time
import json

url = 'http://email.163.com/'

fromData = {   # 需登录传递信息
        'd': 10,
        'domains': "163.com",
        'l': 0,
        'pd': "mail163",
        'pkid': "CvViHzl",
        'pw': "Xca8yR0cYTdBKTOEH77cGUdPXC2HvXGBOboRaCMl5ZzCh49Bjtf5oKNZb9VvyR0AgeiPdGSJr5kj+OM+HluvnAQ10UJyqhjHOWdUVdVAuwHLRRZcyvn/lFtlwq9RFKpmzJkRS02rE9QrDsgEib5OfEevaQ0YoY0UZeOA9afl34Q=",
        'pwdKeyUp': 1,
        't': 1501034716819,
        'tk': "fe35363dfcef6ca6ea00708d3bf666a4",
        'topURL': "http://mail.163.com/",
        'un': "xiongtaozz@163.com"
    }

headers = {
    'Host': 'email.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
cookies = {}
Cookie = 'jsessionid-cpta=6OXT1MMkKcKqnDMngVOq7%2Fe%2BD6oHnrYXS%5CHT6I%2B94gjUCOuQRM0dDHpm6nWhC8j%5Cq7P%5CFpQHEVFdaD4%2BJEUUH4pljLXhJ5tFTLD4jNWeA9WxBcWhqYa0bccrq%5CPGG%2FtaDtXOF0Y1lIRNDQyWQL%2BaWx%5C%2BLPCbikqEGoCDoampoLDR8L%2Bh%3A1501051932694; c98xpt_=30; JSESSIONID-WYTXZDL=TJG%2FvqUVL1%2BvK%5Cu4h%2F702or9U8%2BzwITG0%2FOmWsXV%5CyZLa0BbRA2%5CJvBUkFVEY5jD%5C%2Fi4a7mqyrLUFw8ogDD%2FhnvHmYxR5G440cN%5Ci45UJmm2bBAdR8TKBBLsO0V6kj2aagnq304J%2FSGEfjAG7Mi2m3PNydjNvI06tm35MF2eGB%2FV913%5C%3A1501052112894; _ihtxzdilxldP8_=30; l_s_mail163CvViHzl=2BDA1093FDDA9283AD02B57FFFEC7E0E2484F1A80DE7893751B42F6C10556E5E3DD4EE7F2CD02246E1960210006B5952301FC0660356A299D4F1E15FD74E06587F6C7E127BAABF913EC851B7679D602B4075BF20D6BEE8E36BF1D140F5A65FFE892D6FD48B86B2FDBCB1B550B7F87'
# Cookie2 ='_ntes_nnid=da3ba53c54999346c6d92b592c83aed9,1500862541041; _ntes_nuid=da3ba53c54999346c6d92b592c83aed9; MailMasterPopupTips=1500862541408; Province=028; City=028; NTES_hp_textlink1=old; __s_=1; vjuids=-4959c31c4.15d79068571.0.3339e7d153c9c; __gads=ID=dca657304a708fa8:T=1500974058:S=ALNI_Mav6aa_KltNh5jqX0ADZX5lAZEBIw; vjlast=1500974057.1501032638.13; MailPromotePopup2=1501033636082; __intenal__TPTS=%7B%22t21%22%3A%7B%22c%22%3A1%2C%22t%22%3A1501033641300%7D%7D; NTES_SESS=UCHpw4QHseozhIADZGQU5y_EiJAiCDTYxo5bpNuQUwI9VQXFV_orx5EX5GE1.RsIgSCE2Vr9zve60gTq3_a178kkW9r7K0lnEXPKmrk_ALHqpeNe7HkD5dod8lZQpQK15_tC7VEU3rpENHb2qV.L2_6ElplgGUF8j99e7bjQRAHkPhVinvsrTSqSr; S_INFO=1501039187|0|2&90##|xiongtaozz; P_INFO=xiongtaozz@163.com|1501039187|0|mail163|00&99|sic&1500969485&mail163#sic&510100#10#0#0|187679&0|mail163|xiongtaozz@163.com; nts_mail_user=xiongtaozz:-1:1; df=mail163_letter; mail_upx=t10hz.mail.163.com|t11hz.mail.163.com|t12hz.mail.163.com|t13hz.mail.163.com|t1hz.mail.163.com|t2hz.mail.163.com|t3hz.mail.163.com|t4hz.mail.163.com|t5hz.mail.163.com|t6hz.mail.163.com|t7hz.mail.163.com|t8hz.mail.163.com|t1bj.mail.163.com|t2bj.mail.163.com|t3bj.mail.163.com|t4bj.mail.163.com; mail_upx_nf=; mail_idc=; Coremail=1501039187574%RCGGROCaxCurcNLkrKaavJkRTihuXQLC%g1a108.mail.163.com; MAIL_MISC=xiongtaozz; cm_last_info=dT14aW9uZ3Rhb3p6JTQwMTYzLmNvbSZkPWh0dHAlM0ElMkYlMkZtYWlsLjE2My5jb20lMkZqczYlMkZtYWluLmpzcCUzRnNpZCUzRFJDR0dST0NheEN1cmNOTGtyS2FhdkprUlRpaHVYUUxDJnM9UkNHR1JPQ2F4Q3VyY05Ma3JLYWF2SmtSVGlodVhRTEMmaD1odHRwJTNBJTJGJTJGbWFpbC4xNjMuY29tJTJGanM2JTJGbWFpbi5qc3AlM0ZzaWQlM0RSQ0dHUk9DYXhDdXJjTkxrckthYXZKa1JUaWh1WFFMQyZ3PW1haWwuMTYzLmNvbSZsPS0xJnQ9LTEmYXM9ZmFsc2Umbj10; MAIL_SESS=UCHpw4QHseozhIADZGQU5y_EiJAiCDTYxo5bpNuQUwI9VQXFV_orx5EX5GE1.RsIgSCE2Vr9zve60gTq3_a178kkW9r7K0lnEXPKmrk_ALHqpeNe7HkD5dod8lZQpQK15_tC7VEU3rpENHb2qV.L2_6ElplgGUF8j99e7bjQRAHkPhVinvsrTSqSr; MAIL_SINFO=1501039187|0|2&90##|xiongtaozz; MAIL_PINFO=xiongtaozz@163.com|1501039187|0|mail163|00&99|sic&1500969485&mail163#sic&510100#10#0#0|187679&0|mail163|xiongtaozz@163.com; secu_info=1; mail_entry_sess=7c336132bc9af0bc8ab24283321ad15529c7dba1b2538cf9b46a9e031c6817e725830e98ed475a9b2a473559aea3818e37e94ad19b4e25785da9652cf625f7a5b4a6cb6abe562c112ea22f734cb3dd149bd9cb9fb30a46e125a08d584c02899a392da63b661eb1fe556ad9d0cbd201e61d022e74f39a657efc21feb1467e3d510f83e594f1db6e991142218788ba4d4fb500cec13e72cd595459b8ec89fb390a5074f715ae79e7f971d886377ecd6c74d12ca2765baa80d97cf9afea82f474bc; locale=; Coremail.sid=RCGGROCaxCurcNLkrKaavJkRTihuXQLC; mail_style=js6; mail_uid=xiongtaozz@163.com; mail_host=mail.163.com; JSESSIONID=8CE3B55871BDE2DBFB380E703203C544; starttime=; logType='
Cookie2 = 'T_INFO=8075967017E39A4FD5A14EAA5607FBE6; _ntes_nnid=da3ba53c54999346c6d92b592c83aed9,1500862541041; _ntes_nuid=da3ba53c54999346c6d92b592c83aed9; Province=028; City=028; NTES_hp_textlink1=old; __s_=1; vjuids=-4959c31c4.15d79068571.0.3339e7d153c9c; __gads=ID=dca657304a708fa8:T=1500974058:S=ALNI_Mav6aa_KltNh5jqX0ADZX5lAZEBIw; vjlast=1500974057.1501032638.13; webzjcookiecheck=1; l_s_163MODXOXd=5B4AE6BFF238CE247A553C01A50AC3902A2EA2CC068CDB7423FDC6885D45B5253E43EB2549DC3F810A83F048E6A71CE88D2D43A1B0336C671FE3C565C05F6BF33D884626201B23AE0CCC4404E5722A1D6DCD0C22078961624474E89F2DF78492; SID=8fe269b0-829d-479e-9617-f70d7231e93d; NTES_SESS=UCHpw4QHseozhIADZGQU5y_EiJAiCDTYxo5bpNuQUwI9VQXFV_orx5EX5GE1.RsIgSCE2Vr9zve60gTq3_a178kkW9r7K0lnEXPKmrk_ALHqpeNe7HkD5dod8lZQpQK15_tC7VEU3rpENHb2qV.L2_6ElplgGUF8j99e7bjQRAHkPhVinvsrTSqSr; S_INFO=1501039187|0|2&90##|xiongtaozz; P_INFO=xiongtaozz@163.com|1501039187|0|mail163|00&99|sic&1500969485&mail163#sic&510100#10#0#0|187679&0|mail163|xiongtaozz@163.com; THE_LAST_LOGIN=xiongtaozz@163.com; l_s_mail163CvViHzl=2BDA1093FDDA9283AD02B57FFFEC7E0E2484F1A80DE7893751B42F6C10556E5E3DD4EE7F2CD02246E1960210006B5952B098E89AE3BAB97FDE515ECD54CF94A4D2D0286A1C76E43DBBC5D1A641BB0CA912991BFEA10D88F62C50D543D2BE59AAE1AC864CAC2C9F9995BE186B93873C6F; JSESSIONID-WYTXZDL=w%2B%2B01gXHq5lGwULK5tybW1%2B7S%5CnkeqZFgX%2B%2BoqnuRHPsnMcij0Usvg8EqwS4aLghcnl%2FSDevp6V%2BFIYYYXYzVHqG3d7yl%2BpooY4IRa8yf%2BY8lAtb3%5CFnUAeBj5ySAVEffmvPkY%5CkDFlwEE3rQcwBoKBQLBLd6zSF0zpE8beOGSuJFYI1%3A1501056875768; _ihtxzdilxldP8_=30; jsessionid-cpta=QL6LLU6IPMjVgKWQtb9d3e%2B6ZrLAUd%2FMMt9WvS%2Fh7FpdGmnNp0z1W%2Byf2OmUGOnEwdvNAC%2F7yZn6ImdgnfmMwM4oWPj8F7pTyEtBvlpZgv%2Fa4KnJ%5C7HbTIAyvfBgqWRYKTvrS38fOJkyCk5pWQrCuovdqbk%5CqTd5tfBCDIZLKYxvzR9w%3A1501057411840; c98xpt_=30'
headers['Cookie'] = Cookie
for line in Cookie.split(';'):
  key, value = line.split('=', 1)  # 1代表只分一次，得到两个数据
  cookies[key] = value

# print(cookies)
s_url = 'http://dl.reg.163.com/ini?pd=mail163&pkid=CvViHzl&pkht=mail.163.com&nocache='+str(int(time.time()*1000))
tk_url = 'http://dl.reg.163.com/gt?un=%s&pkid=CvViHzl&pd=mail163&nocache=%s' % ('xiongtaozz@163.com', int(time.time()*1000))
# print(tk_url)
# print(s_url)
# con = requests.get(s_url, headers)
# # con = requests.get(url=tk_url, headers=headers, cookies=cookies)
# print(con.status_code)
# print(con.content)
# print(con.cookies)
# print(con.cookies)
# headers['Cookie'] = Cookie2
# # time.sleep(2)
# tk_con = requests.get(tk_url, headers)
# print(tk_con.status_code)
# print(tk_con.content)
# print(tk_con.cookies)

rq_session = requests.session()
# rq_session.headers = headers
# rq_session.get(url)
# rq_session.cookies = cookies
print(s_url)
con = rq_session.get(s_url)
print(con.status_code)
# print(con.cookies)
# cookies = requests.utils.dict_from_cookiejar(con.cookies)
# print(cookies)
tk_con = rq_session.get(tk_url)
print(tk_con.status_code)
print(con.content)
# print(json.loads(con.content))