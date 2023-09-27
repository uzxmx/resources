#/usr/bin/env python

from PIL import Image
from io import BytesIO
from pytesseract import image_to_string

NOISE_RGB_LIST = [117, 140, 112]    # 噪点像素值列表
OPERATE_LIST = ['+', 'x', 'X',  '-', '—']

# 去除噪点
def del_point(img):
    pix = img.load()
    width = img.size[0]
    height = img.size[1]
    for x in range(width):
        for y in range(height):
            r, g, b = pix[x, y]
            # print(r, g, b)
            if r in NOISE_RGB_LIST:
                pix[x, y] = 255, 255, 255
    return img


# 数字识别
def data_ident(data_str):
    num = None
    if data_str == 'q':
        num = 9
    elif data_str == 'z' or data_str == 'Z':
        num = 2
    elif data_str == 'G':
        num = 6
    else:
        try:
            num = int(data_str)
        except Exception as e:
            print("can't identify:" + data_str)
    return num


# 计算结果
def deal_img_str(img_str):
    # str_list = img_str.split(' ')
    # print(str_list)
    calculate_result = None
    try:
        data_str = img_str[:img_str.rindex('=')]
    except Exception as e:
        print(img_str)
        return

    # print(data_str)
    for operate in OPERATE_LIST:
        if operate in data_str:     # 判断操作符
            data_list = data_str.split(operate)
            if len(data_list) == 2:  # 正确分割时的处理
                data_left = data_ident(data_list[0])
                data_right = data_ident(data_list[1])
                if data_left and data_right:
                    if operate == '+':
                        calculate_result = data_left + data_right
                    elif operate == 'x' or operate == 'X':
                        calculate_result = data_left * data_right
                    else:
                        calculate_result = data_left - data_right
        if calculate_result != None:
            break

    return calculate_result


def img_to_captcha_code(img_content):

    image_data = BytesIO(img_content)
    im = Image.open(image_data)
    im = del_point(im)

    str_img = image_to_string(im, lang='fontyp', config='-psm 70')

    result = deal_img_str(str_img)

    return result


if __name__ == "__main__":
    im = Image.open("b.jpg")
    # im = del_point(im)
    # im.save('b_no.jpg')
    str_img = image_to_string(im, config='--psm 13')
    print('识别为：%s' % str_img)
