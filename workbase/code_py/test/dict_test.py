# coding:utf-8 

d = {
    "status": 200,
    "data": {
        "totalMail": 28,
        "isUnlimited": False,
        "folders": [
            {
                "total": 21,
                "folder_id": 1,
                "name": "收件箱",
                "hasFilter": False,
                "unread": 18,
                "type": "sys",
                "size": 264796
            },
            {
                "total": 0,
                "folder_id": -5,
                "name": "星标邮件",
                "hasFilter": False,
                "unread": 0,
                "type": "sys",
                "size": 0
            },
            {
                "total": 0,
                "folder_id": 3,
                "name": "已发送",
                "hasFilter": False,
                "unread": 0,
                "type": "sys",
                "size": 0
            },
            {
                "total": 0,
                "folder_id": 4,
                "name": "已删除",
                "hasFilter": False,
                "unread": 0,
                "type": "sys",
                "size": 0
            },
            {
                "total": 2,
                "folder_id": 5,
                "name": "垃圾邮件",
                "hasFilter": False,
                "unread": 2,
                "type": "sys",
                "size": 8933
            },
            {
                "total": 5,
                "folder_id": 17,
                "name": "账单",
                "hasFilter": False,
                "unread": 0,
                "type": "other",
                "size": 232313
            },
            {
                "total": 18,
                "folder_id": -2,
                "name": "未读邮件",
                "hasFilter": False,
                "unread": 18,
                "type": "sys",
                "size": 0
            },
            {
                "total": 0,
                "folder_id": 2,
                "name": "草稿箱",
                "hasFilter": False,
                "unread": 0,
                "type": "sys",
                "size": 0
            }
        ],
        "totalSize": 506042,
        "totalUnread": 18,
        "quotaSize": 2147483648
    },
    "msg": "Success"
}

oth = dict([(x['folder_id'], x['total']) for x in d["data"]["folders"] if x["folder_id"] >16 or x["folder_id"] ==1])
print(oth)
