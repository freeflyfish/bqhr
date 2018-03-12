# coding:utf-8

import time
# from datetime import datetime, timedelta
import datetime

s = '2016-05-05'
# 转换成时间数组

# # 转换成时间戳
# print(timeArray)
# timeArray.tm_mon += 2
# print(timeArray)
# timestamp = time.mktime(timeArray)
# print(time.mktime(timeArray))
# timeArray = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
# print(str(datetime.datetime.strptime(s, "%Y-%m-%d") + datetime.timedelta(60))[:-9])

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
fu = datetime.datetime.strptime('2017-12-01 10:01:05', '%Y-%m-%d %H:%M:%S')
now = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '%Y-%m-%d %H:%M:%S')
delta = now - fu
print(delta.days)
print(delta)

from pytz import utc
from pytz import timezone
from datetime import datetime

cst_tz = timezone('Asia/Shanghai')
utc_tz = timezone('UTC')

now = datetime.now().replace(tzinfo=cst_tz)
# local_dt = cst_tz.localize(now, is_dst=None)
utctime = now.astimezone(utc)
print("now   : %s" % now)
print("format: %s" % now.strftime('%Y-%m-%d %H:%M:%S'))
print("utc   : %s" % utctime)
utcnow = datetime.utcnow()
utcnow = utcnow.replace(tzinfo=utc_tz)
china = utcnow.astimezone(cst_tz)
print("utcnow: %s" % utcnow)
print("format: %s" % utcnow.strftime('%Y-%m-%d %H:%M:%S'))
print("china : %s" % china)

