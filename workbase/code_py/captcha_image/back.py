# coding: utf-8

import pygame
from pygame.locals import *
from sys import exit
import time
from PIL import Image

pygame.init()
screen_size = (1000, 1000)

screen = pygame.display.set_mode(screen_size, 0, 32)
# 初始化屏幕，大小1280*800，不使用特殊，32色。
font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []
# 调用系统字体，获取行高的数值，建立一个列表用来存放事件
temp = []
num = 1000

img = Image.open("1.png")

while num:
    num -= 1
    event = pygame.event.wait()
    if (str(event)[7] == '4'):
        event_dirt = eval(str(event)[21:-2])
        i = list((event_dirt['pos']))[0]
        j = list((event_dirt['pos']))[1]
        img.putpixel((i, j), (255, 255, 255))
        img.putpixel((i, j), (0, 0, 0))
        img.putpixel((i + 1, j), (0, 0, 0))
        img.putpixel((i + 1, j + 1), (0, 0, 0))
        temp.append(list((event_dirt['pos'])))

    if event.type == QUIT:
        exit()
    screen.fill((0, 0, 0))
    # 设置背景色，0,0,0就是全黑
print(temp)
img.save('end.png')
