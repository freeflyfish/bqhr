# coding:utf-8

from lxml import etree

with open('jd_ds.html', 'r', encoding='utf-8') as f:
    html = f.read()

    htmlx = etree.HTML(html)
    lis = htmlx.xpath('//li[@class="gl-item"]/div[@class="gl-i-wrap"]')

    for l in lis:
        print(l.xpath('div[1]/a/@title'))
        print(l.xpath('div[2]/strong/i/text()'))
        print(l.xpath('div[3]/a/em/text()')[0])
        print('*' * 50)