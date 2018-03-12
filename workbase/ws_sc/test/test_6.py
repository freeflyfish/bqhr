# coding:utf-8

from lxml import etree
import re

with open('simpleReport.html', 'r') as f:
    html = etree.HTML(f.read())
    # print(html.xpath('//table[@height="155"]/tbody/tr[2]/td[1]/text()'))
    # print(html.xpath('//table[@height="155"]/tbody/tr[2]/td[1]/text()')[0].replace('\n', '').replace('\t', '').
    #       replace('\xa0', ''))
    # print(html.xpath('//table[@height="155"]/tbody/tr[2]/td[2]/text()')[0].replace('\n', '').replace('\t', '').
    #       replace('\xa0', ''))
    # print(html.xpath('//table[@height="155"]/tbody/tr[2]/td[3]/text()')[0].replace('\n', '').replace('\t', '').
    #       replace('\xa0', ''))
    # print(html.xpath('//table[@height="155"]/tbody/tr[2]/td[4]/text()')[0].replace('\n', '').replace('\t', '').
    #       replace('\xa0', ''))
    #
    # print(html.xpath('//table[@height="155"]/tbody/tr[3]/td[1]/text()')[0].replace('\n', '').replace('\t', '').
    #       replace('\xa0', ''))
    # sumer = html.xpath('//table[@height="155"]/tbody/tr')
    # for x in range(1, len(html.xpath('//table[@height="155"]/tbody/tr'))):
    #     print(sumer[x].xpath('td[1]/text()')[0].replace('\n', '').replace('\t', '').replace('\xa0', ''))
    #     print(sumer[x].xpath('td[2]/text()')[0].replace('\n', '').replace('\t', '').replace('\xa0', ''))
    #     print(sumer[x].xpath('td[3]/text()')[0].replace('\n', '').replace('\t', '').replace('\xa0', ''))
    #     print(sumer[x].xpath('td[4]/text()')[0].replace('\n', '').replace('\t', '').replace('\xa0', ''))
    all1 = html.xpath('//table/tr[2]/td/span')
    all2 = html.xpath('//table/tr[2]/td/ol[@class="p olstyle"]')
    # print(all[0].xpath('string(.)').replace('\n', '').replace('\t', '').replace('\xa0', ''))
    # print(html.xpath('//ol[@class="p olstyle"][1]'))
    for x in range(len(all1)):
        print(all1[x].xpath('strong/text()')[0])
        print(re.sub('[\s]+', '', all2[x].xpath('string(.)')))