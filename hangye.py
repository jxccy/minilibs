# -*- coding: utf-8 -*-
import os
from random import choices, random
from time import sleep

import requests
import pandas as pd
from pandas import DataFrame, Series
from PIL import Image, ImageDraw, ImageFont

VERIFICATION_FNT_PATH = 'fonts/思源黑/Source Han Sans CN/SourceHanSansCN-Medium.otf'


class HangYe(object):
    file = 'handlelogo.csv'
    df = pd.read_csv(file, encoding='utf-8', sep='	')[['简称', '全称', '官网', '成立时间', '分支机构数','区域', '省份', '城市', '最终logo阿里云版']]
    color_dict = {
        # nan
        '华东': (180, 199, 231),
        '东北': (157, 122, 115),  # 9d7a73
        '华中': (176, 123, 179),  # b07bb3
        '华北': (247, 201, 97),  # f7c961
        '西北': (223, 111, 112),  # df6f70
        '西南': (243, 156, 71),  # f39c47
        '华南': (157, 203, 93),  # 9dcb5d'''
    }

    @classmethod
    def down_logo(cls, logo_='最终logo'):
        headers = {
            "USER_AGENT": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
            "Accept": "*/*; q=0.01",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "http://www.sougou.com/",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        df = cls.df
        for index in df.index:
            url = df.loc[index][logo_]
            suffix = url.rsplit('.', 1)[-1].replace('@!f_200x200', '') if isinstance(url, str) else 'http'
            est_time = df.loc[index]['成立时间']
            if isinstance(est_time, str):
                est_time = est_time.replace('/', '-')
            name = '%s-%s-%s.%s' % (df.loc[index]['分支机构数'], df.loc[index]['简称'], est_time, suffix)
            file_path = 'logo1208/%s/%s/%s' % (df.loc[index]['区域'], df.loc[index]['省份'], df.loc[index]['城市'])

            if not os.path.exists(file_path):
                os.makedirs(file_path)
            file_name = os.path.join(file_path, name)
            # # 存在logo pass
            if os.path.exists(file_name):
                continue
            #     if url.startswith('http://img.027cgb.com'):
            #         # os.remove(file_name)
            #         print('成功删除%s' % file_name)
            #     continue
            try:
                res = requests.get(url, headers=headers, proxies={'http': 'http://pp2.iops.cc:20151'}, timeout=30)
            except:
                continue
            with open(file_name, 'wb') as wf:
                wf.write(res.content)
            if os.path.exists(file_name):
                try:
                    image = Image.open(file_name)
                    width, height = image.size
                    rate = width / height
                    if rate > 0.7 and rate <= 1.3:
                        Captcha.merge_logo(file_name)
                except:
                    os.remove(file_name)
                    print('成功删除%s' % file_name)
                    cls.make_logo(file_name, df.loc[index]['区域'])

    @classmethod
    def count_make_logo(cls):
        curdir = os.path.abspath(os.path.curdir)
        lst = ['华南', '西北', 'nan', '华东', '西南', '华北', '东北', '华中']
        all_log = []
        for addr in lst:
            addr_path = os.path.join(curdir, addr)
            for pro in os.walk(addr_path):
                all_log.extend(pro[-1])
        exist_ = filter(lambda x: '-' in x, all_log)
        logo_df = DataFrame(list(exist_))
        l_df = logo_df[0].str.split('-', expand=True)

        res = cls.df.merge(l_df[[1]], how='outer', left_on='简称', right_on=1)
        return res[res[1].isnull()].dropna(how='all')

    @classmethod
    def make_logo(cls, file_name, addr):
        # 简称
        abbreviation = file_name.rsplit('/', 1)[-1].split('-')[1]
        suffix = file_name.rsplit('.')[-1]
        file_name = file_name.replace('.%s' % suffix, 'zz.%s' % suffix)

        color = cls.color_dict.get(addr, (180, 199, 231))
        if len(abbreviation) == 4:
            Captcha.make_logo(abbreviation, file_name, color=color)
        else:
            Captcha.make_other_logo(abbreviation, file_name, color=color)

    @classmethod
    def add_logo(cls):
        df = cls.df
        for index in df.index:
            date = '%s' % df.loc[index]['成立时间']
            name = '%s-%s-%s.%s' % (df.loc[index]['分支机构数'], df.loc[index]['简称'], date.replace('/', '-'), 'png')
            file_path = '绘制/%s/%s/%s' % (df.loc[index]['区域'], df.loc[index]['省份'], df.loc[index]['城市'])
            curdir = os.path.abspath(os.path.curdir)
            file_path = os.path.join(curdir, file_path)

            if not os.path.exists(file_path):
                os.makedirs(file_path)
            file_name = os.path.join(file_path, name)

            abbreviation = df.loc[index]['简称']
            color = cls.color_dict.get(df.loc[index]['区域'], (180, 199, 231))
            if len(abbreviation) == 4:
                Captcha.make_logo(abbreviation, file_name, color=color)
            else:
                Captcha.make_other_logo(abbreviation, file_name, color=color)
            print(file_name)


class Captcha(object):

    @classmethod
    def get_fnt(cls, font=VERIFICATION_FNT_PATH, font_size=17):
        return ImageFont.truetype(font, font_size)

    @classmethod
    def get_code(cls, size=4):
        char_set = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        return ''.join(choices(char_set, k=size))

    @classmethod
    def get_number_code(cls, size=6):
        char_set = '1234567890'
        return ''.join(choices(char_set, k=size))

    # @classmethod
    # def generate_captcha(cls, the_chars):
    #     # 选择验证码的字体，图片大小，字体大小
    #     font_color = (255, 255, 255)
    #     font = cls.get_fnt(font_size=50)
    #     font_width, font_height = font.getsize(the_chars[:len(the_chars) // 2])
    #     print('字体大小 %s %s' % (font_width, font_height))
    #
    #     captcha_size = (int(font_width * 1.5), int(font_height * 2.5))
    #     image = Image.new(mode='RGBA', size=captcha_size, color=(180, 199, 231))
    #     draw = ImageDraw.Draw(image)
    #
    #     draw.text((int(font_width * 0.25), int(font_height * 0.3)), \
    #               the_chars[:len(the_chars) // 2], font=font, fill=font_color)  # 填充字符串
    #     draw.text((int(font_width * 0.25), int(font_height * 1.2)), \
    #               the_chars[len(the_chars) // 2:], font=font, fill=font_color)  # 填充字符串
    #
    #     rad = captcha_size[0] // 5  # 设置半径
    #     circle = Image.new('L', (rad * 2, rad * 2), 0)
    #     alpha = Image.new('L', captcha_size, 255)
    #     draw = ImageDraw.Draw(circle)
    #     draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    #     w, h = captcha_size
    #     alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    #     alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    #     alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    #     alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    #     image.putalpha(alpha)
    #     image = image.resize(captcha_size, Image.ANTIALIAS)
    #     image.save('%s.png' % the_chars)

    @classmethod
    def make_logo(cls, the_chars, filename=None, color=(180, 199, 231)):
        # 选择验证码的字体，图片大小，字体大小
        font_color = (255, 255, 255)
        font = cls.get_fnt(font_size=500)
        the_char = the_chars[0] + '' + the_chars[1] + '\n\n' + the_chars[2] + '' + the_chars[3]
        font_width, font_height = font.getsize(the_char)
        d_size = int(max(font_width, font_height) * 1.1 // 2)
        print(font_width, font_height, d_size)

        captcha_size = (d_size, d_size)
        image = Image.new(mode='RGBA', size=captcha_size, color=color)
        draw = ImageDraw.Draw(image)
        draw.text((d_size // 12, d_size // 12.5), the_chars[0] + '' + the_chars[1], font=font,
                  fill=font_color, align="center", )

        draw.text((d_size // 12, int(d_size // 10 + d_size // 2.4)), the_chars[2] + '' + the_chars[3], font=font,
                  fill=font_color, align="center")
        # draw.text((d_size // 8, d_size // 14), the_char, font=font,
        #           fill=font_color, align="center", )

        rad = captcha_size[0] // 6  # 设置半径
        circle = Image.new('L', (rad * 2, rad * 2), 0)
        alpha = Image.new('L', captcha_size, 255)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
        w, h = captcha_size
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
        image.putalpha(alpha)
        image = image.resize(captcha_size, Image.ANTIALIAS)
        filename = '%s.png' % the_chars if not filename else filename
        image.save(filename, format='PNG')

    @classmethod
    def make_other_logo(cls, the_chars, filename=None, color=(180, 199, 231)):
        font_color = (255, 255, 255)
        font = cls.get_fnt(font_size=500)
        the_char = ' '.join(list(the_chars))
        font_width, font_height = font.getsize(the_char)
        captcha_size = (int(font_width * 1 * 1.2), int(font_height * 1.4))
        image = Image.new(mode='RGBA', size=captcha_size, color=color)
        draw = ImageDraw.Draw(image)
        draw.text((font_width * 0.1, font_height * 0.15), the_char, font=font,
                  fill=font_color, align="center", )  # 填充字符串
        rad = captcha_size[0] // 25  # 设置半径
        circle = Image.new('L', (rad * 2, rad * 2), 0)
        alpha = Image.new('L', captcha_size, 255)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
        w, h = captcha_size
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
        image.putalpha(alpha)
        image = image.resize(captcha_size, Image.ANTIALIAS)
        filename = '%s.png' % the_chars if not filename else filename
        image.save(filename, format='PNG')

    @classmethod
    def merge_logo(cls, log_path):
        suffix = log_path.rsplit('.')[-1]
        filename = log_path.replace('.%s' % suffix, 'pj.%s' % suffix)
        the_chars = log_path.rsplit('/', 1)[-1].split('-')[1]
        path = os.path.dirname(filename)
        if not os.path.exists(path):
            os.makedirs(path)
        cls.handle_logo(the_chars, logo_img=log_path, filename=filename)

    @classmethod
    def handle_logo(cls, the_chars, logo_img='', filename=None, color=(255, 255, 255)):
        pre_logo = Image.open(logo_img)
        pre_width, pre_height = pre_logo.size

        font_color = (50, 50, 50)
        font = cls.get_fnt(font_size=500)
        the_char = ''.join(list(the_chars))
        font_width, font_height = font.getsize(the_char)
        # 原logo
        new_width = int(font_height * 2 / pre_height * pre_width)
        pre_logo = pre_logo.resize((new_width, int(font_height * 2)), Image.ANTIALIAS)

        captcha_size = (int(font_width * 1.1) + new_width, int(font_height * 2))
        image = Image.new(mode='RGBA', size=captcha_size, color=color)
        draw = ImageDraw.Draw(image)
        draw.text((new_width, font_height * 0.43), the_char, font=font,
                  fill=font_color, align="center", )  # 填充字符串
        w, h = captcha_size
        image.paste(pre_logo, (0, 0))
        filename = '%s.png' % the_chars if not filename else filename
        image.save(filename, format='PNG')
        print('handle_logo %s'% filename)


if __name__ == '__main__':
    HangYe.down_logo(logo_='最终logo阿里云版')
    # HangYe.down_logo(logo_='无水印logo')
    # HangYe.down_logo(logo_='有水印logo')
    # res = HangYe.count_exist_logo()
    # print(len(res))
    # Captcha.generate_captcha('强贲资产')
    # # """['克拉财富', '星怡资本', '桥水财富', '中盟金控', '大唐汇金', '星沃财富', '纳觅财富', '信利同门', '引力财商', '中合控股', '砺臻至善', '德盈金控', '高通基金', '渝信财富', nan]"""
    # Captcha.make_logo('汇荣投资')
    # Captcha.make_other_logo('民创大健康')
    # print(HangYe.count_make_logo())
    # HangYe.add_logo()
    # with open('tt.png', 'w') as wf:
    #     wf.write('fdasf')
    # HangYe()
