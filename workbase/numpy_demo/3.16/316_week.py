import numpy as np
from datetime import datetime


def dataestr2num(s):
    return datetime.strptime(s, "%d-%m-%Y").date().weekday()

dates, open, high, low, close = np.loadtxt('data.csv', delimiter=',', usecols=(1, 2, 3, 4, 5),
                                           converters={1: dataestr2num}, unpack=True)

close = close[:16]
dates = dates[:16]

first_monday = np.ravel(np.where(dates == 0))[0]
print('The first Monday index is', first_monday)

last_monday = np.ravel(np.where(dates == 4))[-1]
print('The first Monday index is', first_monday)

weeks_indices = np.arange(first_monday, last_monday + 1)
print('Weeks indices initial', weeks_indices)

weeks_indices = np.split(weeks_indices, 3)
print('Weeks indices initial', weeks_indices)


def summarize(a, o, h, l, c):
    monday_open = o[a[0]]
    week_high = np.max(np.take(h, a))
    week_low = np.min(np.take(l, a))
    friday_close = c[a[-1]]
    return("APPL", monday_open, week_high, week_low, friday_close)

weeks_summary = np.apply_along_axis(summarize, 1, weeks_indices, open, high, low, close)
print('Week summary', weeks_summary)

np.savetxt("weeksummart.csv", weeks_summary, delimiter=',', fmt="%s")