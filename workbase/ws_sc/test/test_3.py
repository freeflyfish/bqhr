# coding:utf-8
import re
import json
# s = '6228480128558663877|401|0|156|32706|41'
#
# lis = s.split('|')
# print(lis)
# print(lis[1])
# print(lis[-2])
# print(lis[-1])
# print(lis[2])
# print(lis[-3])
#
# print(input('>'))

s = '''
<script>
      var cardInfo = JSON.parse('[  {    "card_type": "1",    "card_acctType": "401",    "card_no": "6228480128558663877",    "card_name": "借记卡",    "card_show": "1"  },  {    "card_type": "3",    "card_acctType": "",    "card_no": "",    "card_name": "电子账户",    "card_show": "0"  },  {    "card_type": "2",    "card_acctType": "",    "card_no": "",    "card_name": "信用卡",    "card_show": "0"  }]');
      var custName = "彭梅";
      var config = { imgpath: "/EbankSite/NetBank/static/img" };
      var keyForShow = "K宝";
      var vipCustLevelName = "普通客户";
      var vipCustLevel = "00";
      var logonMode = "1";
      var canUseEA = "1";
      var userSec = {
        hasKT: "0",
        ebflag1: "0",
        ebflag2: "1",
        certNo: ""
      };
      var marketCreditInfo = {
        custTypes: "",
        custMaxCredit: "0",
        custMinCredit: "0",
        custCreditValue: ""
      };
    </script>
'''

# items = re.findall(re.compile("var cardInfo = JSON.parse\('(.*?)'\);"), s)
# print(items)
# lis = json.loads(items[0])
# print(lis[0]['card_no'])

import requests
from selenium import webdriver

dr = webdriver.Ie(executable_path='D:\\IEDriverServer_233.exe')
dr.get('https://perbank.abchina.com/EbankSite/startup.do')
print(dr.get_cookies())