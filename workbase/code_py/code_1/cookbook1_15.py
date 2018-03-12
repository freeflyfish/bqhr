# coding:utf-8

from itertools import groupby
from operator import itemgetter
from re import sub
import random
import time
from datetime import datetime

# print(str(random.sample(range(9), 6))[1:-1].replace(',', '').strip())


rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5412 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)