import requests

headers = dict()
d = {'LT': '1515644997', 'tgc': 'TGT-Mjc2NTk3NTE1MA==-1515644997-gz-AA7749970C20407603E7631579A7D620-1', 'SRF': '1515644998', 'SRT': 'D.QqHBJZ4qPQBePrMbPFYGSPH1isSZdObuW!uwTebHNEYdP4kSi-PpMERt4EP1RcsrAcPJdEWkTsVuObPldZE-VFyqOOY4WGPqPG9ZW!uPPrSQi4kTNbHtOGWs*B.vAflW-P9Rc0lR-ykZDvnJqiQVbiRVPBtS!r3JZPQVqbgVdWiMZ4siOzu4DbmKPWQ5PiKIdHfiDE6N4zn4qBnSFolVqSZi49ndDPIJcYPSrnlMcywObi6IOMOJCsn4rjsJcM1OFyHM4HJ5mkoODmkS4oCIZHJ5mkoODEfI4oCNrsJ5mkiOmHIO4noNqHJ5mkoODmpJ!noTDPr', 'SCF': 'AoL6GVcikdn4t7ugk7-ayxEyTnBtbuiHXANBiQmQx993YbpGBAC41R6GQRc7vzLuNLe-OevdNZ0RhKzaRbpp9p0.', 'SUB': '_2A253UpgWDeThGeRJ7VcY9yvNzjyIHXVUKY7erDV8PUJbmtBeLXWmkW9NUnZ1vposM8TtusTzcvNUWFW5KZJRxLwu', 'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WWySN-bh41oIB0S0pdlns6c5JpX5K2hUgL.FozNSo-4S0-pSK52dJLoIEBLxKqL1-eLB.2LxKqL1h-LBKMLxKMLBKML1K2LxKqL122L1h5t', 'ULOGIN_IMG': 'gz-a418f1729fb6097456a363d2744b5362bf51', 'U_TRS1': '000000db.e0842d66.5a56e83d.0de601c0', 'U_TRS2': '000000db.e08c2d66.5a56e83d.27730c6c', 'sso_info': 'v02m6alo5qztKWRk5yljpOQpZCToKWRk5iljoOgpZCjnLKNs5i1jpOctYyTlLCJp5WpmYO0so2zmLWOk5y1jJOUsA==', 'ALF': '1518236998', 'SSOLoginState': '1515644998', 'SUHB': '0ft4J2d8GcW66V', 'SWEBAPPSESSID': '8d9a2f6f2dcec0bb65fb7276b25ba1766', 'WEB2': '0f1563e729ff4ee30d30c0fb13e8bbce', 'login': '1d143a736fdf93d35dc1b24d4482f559'}
ds = ''
for x in d.items():
    ds += x[0] + '=' + x[1] +';'
print(ds)
headers['Cookie'] = ds
# headers[
#     'Cookie'] = 'U_TRS1=000000db.12c1e86.5a56d25e.e81a74d2; ' \
#                 'U_TRS2=000000db.12cee86.5a56d25e.ab1a3f53; ' \
#                 'SCF=AkozfcOpR6I4PF1CzqvHeZ63t0vcrlwqtZtzZu242-v2aeW-zrWepit5gOPVmEc2y2r9sMrkloqGlCixenfeYQk.; ' \
#                 'UOR=m1.mail.sina.com.cn,www.sina.com.cn,; ' \
#                 'SUB=_2A253UqZADeThGeRJ7VcY9yvNzjyIHXVUKZCIrDV_PUJbm9BeLXHykW9NUnZ1vnS0UM44-bP8dKrza4hKVsMysRWz; ' \
#                 'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWySN-bh41oIB0S0pdlns6c5NHD95QES0qf1KMfeK-7Ws4Dqcj.i--ciKLhi-iWi--ciKnfi-2Ni--Ni-2NiK.pi--ciKyWiKn7; ' \
#                 'sso_info=v02m6alo5qztKWRk5yljpOQpZCToKWRk5iljoOgpZCjnLKNs5i1jpOctYyTlLCJp5WpmYO0so2zmLWOk5y1jJOUsA==; ' \
#                 'SWEBAPPSESSID=8957118fd64f838f1d1731d256aa3be6'

data_form = {
    'act': 'findmail',
    'fid[]': '',
    'order': 'htime',
    'sorttype': 'desc',
    'flag': '',
    'pageno': '1',
    'fol': 'allfolder',
    'phrase': '账单',
    'attlimit': '2',
    'timelimit': '0',
    'starttime': '1505750400000',
    'endtime': '1505750400000',
    'contlimit[]': ['3', '2', '1'],
    'readflag': '2',
    'searchType': '1',
    'tag': '-1',
    'webmail': '1',
}

res = requests.post('https://m1.mail.sina.com.cn/classic/findmail.php', headers=headers, data=data_form, verify=False)
print(res.text)
print(res.cookies.get_dict())
