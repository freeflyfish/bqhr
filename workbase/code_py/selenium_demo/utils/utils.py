# coding:utf-8

from base64 import b64decode
from io import BytesIO
from PIL import Image


def driver_screenshot_2_bytes(photo_base64, crop_box, img_format="PNG"):
    with BytesIO(b64decode(photo_base64)) as buffer, \
            Image.open(buffer) as img, BytesIO() as temp:
        im = img.crop(crop_box)
        im.save(temp, img_format)
        img_bytes = temp.getvalue()
        im.close()
        return img_bytes
