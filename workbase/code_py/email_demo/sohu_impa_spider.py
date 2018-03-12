# coding:utf-8

import email
import imaplib


# 获得字符编码方法
def get_charset(message, default="ascii"):
    # Get the message charset
    return message.get_charset()


def parseEmail(msg):
    mailContent = None
    contenttype = None
    suffix = None
    for part in msg.walk():
        if not part.is_multipart():
            contenttype = part.get_content_type()
            filename = part.get_filename()
            charset = get_charset(part)
            # 是否有附件
            if filename:
                h = email.header.header(filename)
                dh = email.header.decode_header(h)
                fname = dh[0][0]
                encodeStr = dh[0][1]
                if encodeStr != None:
                    if charset == None:
                        fname = fname.decode(encodeStr, 'gbk')
                    else:
                        fname = fname.decode(encodeStr, charset)
                data = part.get_payload(decode=True)
                print('Attachment : ' + fname)
            else:
                if contenttype in ['text/plain']:
                    suffix = '.txt'
                if contenttype in ['text/html']:
                    suffix = '.htm'
                if charset == None:
                    mailContent = part.get_payload(decode=True)
                else:
                    mailContent = part.get_payload(decode=True).decode(charset)
    return mailContent, suffix


# 字符编码转换方法
# def my_unicode(s, encoding):
#     if encoding:
#         return unicode(s, encoding)
#     else:
#         return unicode(s)

conn = imaplib.IMAP4('imap.139.com', 143)

conn.login('18702898679@139.com', 'scx1123x')

conn.select()
resp, items = conn.search(None, 'Subject', '账单'.encode('utf-8'))

for i in items[0].split():
    resp1, mailData = conn.fetch(i, "(RFC822)")
    mailText = mailData[0][1]
    msg = email.message_from_bytes(mailText)
    # ls = msg['Form'].split(" ")
    mailContent, suffix = parseEmail(msg)
    # print(mailContent.decode('gbk'))
    # print(suffix)
    ls = msg["From"].split(' ')
    strfrom = ''
    if (len(ls) == 2):
        fromname = email.header.decode_header((ls[0]).strip('\"'))
        print(fromname[0][0], fromname[0][1])
        strfrom = bytes.decode(fromname[0][0], fromname[0][1]) + '' + ls[1]
        print(strfrom)
    else:
        strfrom = 'From : ' + msg["From"]
    strdate = msg["Date"]
    subject = email.header.decode_header(msg["Subject"])
    sub = bytes.decode(subject[0][0], subject[0][1])
    strsub = 'Subject : ' + sub
    print(sub)
    ls_to = msg["to"].split(' ')
    print(ls_to)

# for x in conn.list()[1]:
#     print(bytes.decode(x).split(' ')[-1])
#
#     conn.select(bytes.decode(x).split(' ')[-1])
#     type1, data = conn.search(None, 'SUBJECT', '账单'.encode('utf-8'))
#     # print(type1)
#     # print(data)
#     if data[0]:
#         msg_list = bytes.decode(data[0]).split()
#         # print(msg_list)
#         for x in msg_list:
#             tpy, dat = conn.fetch(x, "(RFC822)")
#             # print(tpy)
#             # print(dat)
#             msges = email.message_from_string(bytes.decode(dat[0][1]))
#             print(msges["From"])
#             print(msges["Subject"])
#             print(msges["Date"])
#             print(msges["BODY"])
#             for part in msges.walk():
#                 if not part.is_multipart():
#                     content_type = part.get_content_type()
#                     filename = part.get_filename()
#                     print(filename, content_type)
