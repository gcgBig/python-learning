# -*- coding: utf-8 -*-
# 生成缩略图
from PIL import Image

im = Image.open('test.jpg')
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')