# coding:utf-8

from io import BytesIO
from string import digits, ascii_letters

from PIL import Image
from piltesseract import get_text_from_image
from pytesseract import image_to_string


def img2str(captcha_body):
    captcha_char_whitelist = digits
    with Image.open(captcha_body) as img:
        new_img = img.convert('L')  # 转换为RGBA
        pix = new_img.load()  # 转换为像素

        # # 处理上下黑边框，size[0]即图片长度
        # for x in range(new_img.size[0]):
        #     pix[x, 0] = pix[x, new_img.size[1] - 1] = 255

        # # 处理左右黑边框，size[1]即图片高度
        # for y in range(new_img.size[1]):
        #     pix[0, y] = pix[new_img.size[0] - 1, y] = 255

        # 二值化处理，这个阈值为140比较合适
        threshold = 180  # 阈值  # 201
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        new_img = new_img.point(table, '1')
        # 保存图片下来方便后面训练
        # new_img.save("captcha/" + str(int(time())) + ".jpg")
        # 识别图片上的值
        text = get_text_from_image(new_img, psm=7,
                                   tessedit_char_whitelist=captcha_char_whitelist).replace(' ', '')

        new_img.close()

        return text

if __name__ == '__main__':
    captcha_body = 'D:\workbase\ws_sc\\vcode.jpg'
    print(img2str(captcha_body))
