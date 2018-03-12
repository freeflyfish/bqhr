# coidng:utf-8
from bs4 import BeautifulSoup
import re


def parse_ccb_credit_email_html(html_string):
    bs_obj = BeautifulSoup(html_string, "lxml")
    result = {'bill_info': {}, 'bill_detail': []}
    if bs_obj.find('font', text=re.compile('账单周期')).getText()[6:]:
        result['bill_info']['bill_cycle'] = bs_obj.find('font', text=re.compile('账单周期')).getText()[6:]
        card_info_table = bs_obj.find('font', text='账单日').findParents()[3]
        info = []
        for div in card_info_table.find_all('td'):
            if div.find('font'):
                info.append(div.find('font').getText().strip())
        result['bill_info']['bill_date'] = info[1]
        result['bill_info']['due_date'] = info[3]
        result['bill_info']['credit_limit'] = info[5]
        result['bill_info']['cash_limit'] = info[7]

        card_value_table2 = bs_obj.find('font', text='信用卡卡号').findParents()[2]
        if len(card_value_table2.findAll('tr')) > 1:
            tr = card_value_table2.findAll('tr')[1]
            tds = tr.findAll('td')
            result['bill_info']['card_num'] = tds[0].getText()
            result['bill_info']['currency'] = tds[1].getText()
            result['bill_info']['repayment'] = tds[2].getText()
            result['bill_info']['min_repayment'] = tds[3].getText()
        card_info_value_table = bs_obj.find('font', text=re.compile('交易明细')).findParents()[2]
        info_values = card_info_value_table.findAll('tr')[4:-1]
        for info_tr in info_values:
            record = info_tr.findAll('td')
            record_dict = {}
            record_dict['trade_date'] = record[0].getText().strip()
            record_dict['book_date'] = record[1].getText().strip()
            record_dict['card_num'] = record[2].getText().strip()
            record_dict['trade_summary'] = record[3].getText().strip()
            record_dict['trade_amount'] = record[4].getText().strip()
            record_dict['record_amount'] = record[5].getText().strip()
            result['bill_detail'].append(record_dict)
        return result
    else:
        payment_table_bs = bs_obj.find('font', text=re.compile('账单周期')).findParents()[1].findAll('b')
        if len(payment_table_bs) == 3:
            result['bill_info']['bill_cycle'] =payment_table_bs[0].getText()
            result['bill_info']['due_date'] = payment_table_bs[2].getText()
        credit_card_table_fonts = bs_obj.find('font', text=re.compile('本期账单日')).findParents()[3].findAll('font')
        if len(credit_card_table_fonts) == 18:
            result['bill_info']['bill_date'] = credit_card_table_fonts[2].getText()
            result['bill_info']['credit_limit'] = credit_card_table_fonts[5].find('a').getText().strip()
            result['bill_info']['cash_limit'] = credit_card_table_fonts[8].getText()
            result['bill_info']['avaliable_limit'] = credit_card_table_fonts[12].getText()
        try:
            due_table_fonts = bs_obj.find('font', text=re.compile('最低还款额')).findParents()[2].findChildren('tr')[12].findAll('font')
        except Exception:
            due_table_fonts = bs_obj.find('font', text=re.compile('最低还款额')).findParents()[2].findChildren('tr')[10].findAll('font')
        if len(due_table_fonts) ==5:
            result['bill_info']['currency'] = due_table_fonts[0].getText()
            result['bill_info']['repayment'] = due_table_fonts[2].find('b').getText()
            result['bill_info']['min_repayment'] = due_table_fonts[3].getText()

        card_info_value_table = bs_obj.find('font', text=re.compile('交易明细')).findParents()[2]
        info_values = card_info_value_table.findAll('tr')[4:-1]
        for info_tr in info_values:
            record = info_tr.findAll('td')
            record_dict = {}
            record_dict['trade_date'] = record[0].getText().strip()
            record_dict['book_date'] = record[1].getText().strip()
            record_dict['card_num'] = record[2].getText().strip()
            record_dict['trade_summary'] = record[3].getText().strip()
            record_dict['currency'] = record[4].getText().strip()
            record_dict['trade_amount'] = record[5].getText().strip()
            result['bill_detail'].append(record_dict)
        return result

import json

with open('html5.html', 'r') as f:
    # html_js = json.loads(f.read())
    # print(html_js['data']['body'])
    # print(parse_ccb_credit_email_html(html_js['data']['body']))
    s = 'https://v4.passport.sohu.com/i/captcha/picture?pagetoken=1515032957453&random=passport403_sdk1515032957453'
    print(s.split('?')[1].split('=')[1].split('&')[0])