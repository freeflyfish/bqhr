# coding:utf-8

try:
    import pytesseract
    from PIL import Image
except ImportError:
    print('导入模块有错误,请使用pip安装,pytesseract')
    raise SystemExit

image = Image.open('vcode.png')
v_code = pytesseract.image_to_string(image)
print(v_code)
