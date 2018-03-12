# coding: utf-8

import re
from lxml import etree

question_pattern = re.compile('<p>问题<span>(.*?)</span>', re.S)
question_options_pattern = re.compile('<p>.*?<input class="radio_type1".*?<span>(.*?)</sp', re.S)


def us_gbk(value):
    if value >= '\u4e00' and value[:-1] <= '\u9fa5':
        value = value.encode('gb2312', 'replace')
    return value
result = dict()
n = 0
with open('dati.html', 'r', encoding='utf-8') as f:
    html = f.read()

    # items_questions = question_pattern.findall(html)
    # print(items_questions)
    # items_options_questions = question_options_pattern.findall(html)
    # print([x.strip() for x in items_options_questions])
    # for item in range(len(items_questions)):
    #     result[items_questions[item]] = items_options_questions[n:n+5]
    #     n +=5
    # print(result)
    # datas = dict()
    # x = etree.HTML(html)
    # inps = x.xpath('//div[@class="qustion"]/ul/input')
    # n = 0
    # count = int(len(inps)/5)
    # for i in range(1, 6):
    #     inp = inps[(i-1) * count:i * count-1]
    #     datas.update({
    #         'kbaList['+str(n)+'].derivativecode': us_gbk(inp[0].xpath('@value')[0]),
    #         'kbaList['+str(n)+'].businesstype': us_gbk(inp[1].xpath('@value')[0]),
    #         'kbaList['+str(n)+'].questionno': us_gbk(inp[2].xpath('@value')[0]),
    #         'kbaList['+str(n)+'].kbanum': us_gbk(inp[3].xpath('@value')[0]),
    #         'kbaList['+str(n)+'].question': inp[4].xpath('@value')[0].encode('gb2312', 'replace'),
    #         'kbaList['+str(n)+'].options1': us_gbk(inp[5].xpath('@value')[0]),
    #         'kbaList['+str(n)+'].options2': us_gbk(inp[6].xpath('@value')[0]),
    #         'kbaList['+str(n)+'].options3': us_gbk(inp[7].xpath('@value')[0]),
    #         'kbaList['+str(n)+'].options4': us_gbk(inp[8].xpath('@value')[0]),
    #         'kbaList['+str(n)+'].options5': us_gbk(inp[9].xpath('@value')[0]),
    #         'kbaList['+str(n)+'].answerresult': '',
    #         'kbaList['+str(n)+'].options': '',
    #     })
    #     n +=1
    # print(datas)

