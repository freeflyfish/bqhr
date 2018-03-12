# coding: utf-8

from lxml import etree
with open('test2.html', 'r', encoding='utf-8') as f:
    html = f.read()
    htmlx = etree.HTML(html)
    trs = htmlx.xpath('//table/tbody/tr')
    for tr in trs:
        print(tr.xpath('td[1]/text()'))
        print(tr.xpath('td[2]/text()'))
        print(tr.xpath('td[3]/text()'))
        print(tr.xpath('td[4]/text()')[0] if tr.xpath('td[4]/text()') != [] else None)
        print(tr.xpath('td[5]/text()'))
        print(tr.xpath('td[6]/text()'))
        print(tr.xpath('td[7]/text()'))
        print(tr.xpath('td[8]/a/@href')[0] if tr.xpath('td[8]/a/@href') != [] else None)
        print('*' * 50)
    # for tr in trs:
    #     print(tr.xpath('th/text()')[0] if tr.xpath('th/text()') != [] else None, tr.xpath('td/text()')[0] if tr.xpath('td/text()') != [] else None)
    #     print('*' * 50)