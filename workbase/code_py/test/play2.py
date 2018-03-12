import random

capitals = {'北京市': '北京',  # 省份对应的省城
            '天津市': '天津',
            '上海市': '上海',
            '重庆市': '重庆',
            '广西': '南宁',
            '内蒙': '呼和浩特',
            '西藏': '拉萨',
            '宁夏': '银川',
            '新疆': '乌鲁木齐',
            '香港': '香港',
            '澳门': '澳门',
            '四川': '成都',
            '山东': '济南',
            '江苏': '南京',
            '甘肃': '兰州',
            '陕西': '西安',
            '山西': '太原',
            '浙江': '杭州',
            '湖南': '长沙',
            '湖北': '武汉',
            '河南': '郑州',
            '江西': '南昌',
            '海南': '海口',
            '河北': '石家庄',
            '贵州': '贵阳',
            '云南': '贵阳',
            '黑龙江': '哈尔滨',
            '辽宁': '沈阳',
            '吉林': '长春',
            '青海': '西宁',
            '广东': '广州',
            '福建': '厦门'

            }
stuNum = int(input('你要出几份考卷?    '))  # 出卷数
# 循环并创建测试卷和答案卷
for quizNum in range(stuNum):
    quizFile = open(r'考卷{}.txt'.format(quizNum + 1), 'w', encoding='utf-8')
    answerKeyFile = open(r'答案{}.txt'.format(quizNum + 1), 'w', encoding='utf-8')
    # 把题目and日期and班级写入测试卷
    quizFile.write('名字:\n\n日期:\n\n班级:\n\n')
    # 给测试卷起名，前面空20个空格使标题居中
    quizFile.write((' ' * 20) + '省 配 对 省 份 城 市 测 试 卷{}\n\n'.format(quizNum + 1))
    # 省份是keys，直接提取出来
    provinces = list(capitals.keys())
    # 打乱省份的顺序
    random.shuffle(provinces)

    # 根据省份城市数量创建一张测试卷里面有多少个小题
    for questionNum in range(len(provinces)):
        # 创建正确的省城，从capitals里面正确的省份找到对应正确的省城
        correctAnswer = capitals[provinces[questionNum]]
        # 创建错误的答案池，用values定位出字典列表里面的省城
        # 在capitals里用values定位出所有省城
        wrongAnswer = list(capitals.values())
        # print(wrongAnswer)
        # 省城答案池删掉正确省城就是错误答案池
        wrongAnswer.remove(correctAnswer)
        # del wrongAnswer[wrongAnswer.index(correctAnswer)]
        # 打乱错误答案的顺序，每次选出3个错误答案
        wrongAnswer = random.sample(wrongAnswer, 3)
        # 创建题，一个题是3个错误答案加上1个正确答案
        answersOptions = wrongAnswer + [correctAnswer]
        # 打乱题的顺序
        random.shuffle(answersOptions)
        # 写题写进测试卷里面
        quizFile.write('{}、{}的省会是？  \n'.format(questionNum + 1, provinces[questionNum]))
        print('{}、{}的省会是？  \n '.format(questionNum + 1, provinces[questionNum]))
        # 创建4个选择，ABCD,包含一个正确答案和3个错误答案
        for i in range(4):
            print('%s. %s\n' % ('ABCD'[i], answersOptions[i]))
            quizFile.write('%s. %s\n' % ('ABCD'[i], answersOptions[i]))

        quizFile.write('\n')
        answerKeyFile.write('{}.{}\n\n'.format(questionNum + 1, 'ABCD'[answersOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()
