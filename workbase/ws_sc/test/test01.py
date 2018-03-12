# coding:utf-8


import re
# url ='http://mail.163.com/js6/main.jsp?sid=FBryFjdtFjmCmoBiSyttqASbfGlPUeoy&df=mail163_letter#module=mbox.ListModule%7C%7B%22fid%22%3A1%2C%22order%22%3A%22date%22%2C%22desc%22%3Atrue%7D'
#
# print(url.split('?')[1].split('&')[0])
from lxml import etree

with open('test.xml', 'r', encoding='utf-8') as f:
    all = f.read()
    xml =etree.XML(all)
    objs = xml.xpath('//object')
    # print(objs[1].xpath('string(.)'))
    for x in range(len(objs)):
        id = objs[x].xpath('string[@name="id"]/text()')
        subject = objs[x].xpath('string[@name="subject"]/text()')
        if subject:
            if 'Py' in subject[0]:
                print(id[0])
                print(subject[0])
                print('*'*30)
    print(objs[0].xpath('string[@name="subject"]/text()') and 'Python_web' in 'Re:����ѧPython_web����ʦѧϰ�ƻ����ű�')
    # html = etree.HTML(all)
    # print(html.xpath('//table[@width="875"]/tr[2]/td[1]/font/text()')[0].replace('\xa0', ''))
    # print(html.xpath('//table[@width="875"]/tr[2]/td[3]/font/text()')[0].replace('\xa0', ''))
    # print(html.xpath('//table[@width="875"]/tr[2]/td[4]/font/text()')[0].replace('\xa0', ''))
    # # print(html.xpath('//table[@width="875"]')[1].xpath('string(.)'))
    # # print(html.xpath('//table[@width="875"]/tr[5:]/td[4]/font/text()')[0])
    # sumer = html.xpath('//table[@width="875"]/tr')
    # price_lis = []
    # # ''.replace('&nbsp;', '')
    # for x in range(6, len(sumer) - 1):
    #     price_lis.append({
    #         'id': sumer[x].xpath('td[1]/font/text()')[0].replace('\xa0', ''),
    #         't_date': sumer[x].xpath('td[2]/font/text()')[0].replace('\xa0', ''),
    #         'p_date': sumer[x].xpath('td[3]/font/text()')[0].replace('\xa0', ''),
    #         'description': sumer[x].xpath('td[4]/font/text()')[0].replace('\xa0', ''),
    #         'curr_price': sumer[x].xpath('td[6]/font/text()')[0].replace('\xa0', ''),
    #     })
    # print(price_lis)

