#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/22 16:09
# @Author  : RookieDay
# @Site    : 
# @File    : 01.py
# @Software: PyCharm Community Edition
from PIL import Image
from os import path

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)
# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    # 灰度值公式将像素的 RGB 值映射到灰度值
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    img = Image.open('test.png')
    W, H = img.size
    img = img.resize((W,H), Image.NEAREST)
    out_png = path.join(path.dirname(__file__), 'out.png')
    print(path.splitext('test.png'))
    print(out_png)

    # print(img.format, img.size, img.mode)

    txt = ''
    for i in range(H):
        for j in range(W):
            txt += get_char(*img.getpixel((j,i)))
        txt += '\n'

    with open(out_png,'w') as f:
        f.write(txt)
