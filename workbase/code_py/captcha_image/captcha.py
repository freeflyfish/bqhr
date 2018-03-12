# coding: utf-8

from PIL import Image

img = Image.open("jietu_1.png")
img2 = Image.open("jietu_2.png")
# 切除前60列，不会出现在此
for i in range(0, 60):
    for j in range(img.height):
        img.putpixel((i, j), (255, 255, 255, 255))

# 一列列扫描，放大差异点，相同点置白
for i in range(60, img.width):
    for j in range(img.height):
        r, g, b, a = img.getpixel((i, j))
        r2, g2, b2, a2 = img2.getpixel((i, j))
        sum = r + g + b
        sum2 = r2 + g2 + b2
        if abs(sum2 - sum) > 15:
            print('chayi: ', abs(sum2 - sum))
            abs_num = abs(sum2 - sum) * 5 % 255  # 我也不知道什么用,代码本天成，妙手自可得
            img.putpixel((i, j), (abs_num, abs_num, abs_num, 255))
        else:
            img.putpixel((i, j), (255, 255, 255, 255))
# 扫描首次与最后一次遇到大量深色区域的i坐标 分别赋值给i1,i2
num = 0
i1 = 0
i2 = 0
for i in range(img.width):
    sum = 0
    for j in range(img.height):
        r, g, b, a = img.getpixel((i, j))
        if (r + g + b) != 255 + 255 + 255:
            sum += 1
    if (sum > 20):
        if num == 0:
            num += 1
            i1 = i
        else:
            i2 = i

print("首次遇到大量黑色点i1: ", i1, )
print("最后遇到大量黑色点i2: ", i2, )
chazhi = i2 - i1
sum1 = 0
sum2 = 0
# 以差值大于50做为切割点，判断哪一边是干扰点
if chazhi > 50:
    for i in range(i1, chazhi / 2 + i1):
        for j in range(img.height):
            r, g, b, a = img.getpixel((i, j))
            sum1 = sum1 + r + g + b
    for i in range(chazhi / 2 + i1, i2):
        for j in range(img.height):
            r, g, b, a = img.getpixel((i, j))
            sum2 = sum2 + r + g + b

if sum1 > sum2:
    print(i2 - 22)
else:
    print(i1 + 22)
img.save('end.png')
