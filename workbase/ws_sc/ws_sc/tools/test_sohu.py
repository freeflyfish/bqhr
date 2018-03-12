import hashlib
import requests
from time import time
headers = dict()
headers['Cookie'] = 'a=123; reqtype=pc; gidinf=x099980109ee0d33f68844c69000fd9cabbd76e760f7;jv=18778a4f502330e1dcfe66d4dc200d72-lroXojqZ1515661856001'

data = {
    'userid': 'xiongtaozt@sohu.com',
    'password': hashlib.md5('scx1123'.encode('utf-8')).hexdigest(),
    'appid': '101305',
    'callback': 'passport403_cb%s' % int(time() * 1E3)
}
res = requests.post('https://v4.passport.sohu.com/i/login/101305', data=data, headers=headers, verify=False)
print(res.text)