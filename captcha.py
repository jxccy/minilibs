# -*- coding: utf-8 -*-
import base64
from random import choices

from PIL import Image, ImageDraw, ImageFont

VERIFICATION_FNT_PATH='/Users/mac/Desktop/data-engine/core/static/fonts/FZQKBYSJW/PingFang-SC-Regular.otf'


class Captcha(object):

    @classmethod
    def get_fnt(cls, font=VERIFICATION_FNT_PATH, font_size=17):
        return ImageFont.truetype(font, font_size)

    @classmethod
    def get_code(cls, size=4):
        char_set = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        return ''.join(choices(char_set, k=size))

    @classmethod
    def generate_captcha(cls, the_chars):
        captcha_size = (56, 24)
        font_color = (58, 150, 255)
        # 选择验证码的字体，图片大小，字体大小
        image = Image.new(mode='RGBA', size=captcha_size, color=(240, 242, 244))
        font = cls.get_fnt(font_size=16)
        draw = ImageDraw.Draw(image)
        font_width, font_height = font.getsize(the_chars)
        draw.text(((captcha_size[0] - font_width) / 2, (captcha_size[1] - font_height) / 4), \
                  the_chars, font=font, fill=font_color)  # 填充字符串
        image.show()
        return base64.b64encode(image.tobytes()).decode('utf-8')


if __name__ == '__main__':
    the_chars = ''.join(Captcha.get_code(4))
    Captcha.generate_captcha(the_chars)
