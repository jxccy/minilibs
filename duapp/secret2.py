# -*- coding: utf-8 -*-
from copy import deepcopy
from hashlib import md5
import json
import time
import urllib
import urllib2

# import requests

# UUID = '47e122719530a8fb'
UUID = '47e122719530a8fb'
LOGINTOKEN = 'c3617d9b|71354952|9a792158aa7b730d'
# LOGINTOKEN = ''
COOKIE = 'duToken=b6ad1582%7C71354952%7C1566007923%7Cd30cab02b84f60eb'
DUIMEI = '865291027268324'
SHUMEIID = '20190809184612376b65d6946c9325778fad1f880057b901b8ffb9c2d54166'


import base64
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

class AESCipher:

    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        # iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt( raw ) )


class DuSpider(object):
    param_dict = {
        'uuid': UUID,
        'platform': 'android',
        'v': '4.9.0',
        'loginToken': LOGINTOKEN
    }

    du_headers = {
        # 'Cookie': COOKIE,
        'duuuid': param_dict['uuid'],
        # 'duimei': DUIMEI,
        'duplatform': 'android',
        'duchannel': 'xiaomi',
        'duv': param_dict['v'],
        'dulogintoken': param_dict['loginToken'],
        'dudevicetrait': 'MI+4W',
        # 'shumeiid': SHUMEIID,
        'user-agent': 'duapp/4.9.0(android;6.0.1)'

    }

    cipher = AESCipher('b46afc89e13025d7')

    def get_new_sign(self, url, timestamp):
        param_dict = deepcopy(self.param_dict)
        param_dict['timestamp'] = timestamp
        if "?" in url:
            params = url.split("?", 1)[-1]
            for param in params.split("&"):
                try:
                    key, value = param.split('=', 1)
                except ValueError as e:
                    continue
                if key in ['sign', 'newSign']:
                    continue
                else:
                    key = key.replace('[]', '')
                    param_dict[key] = value
        print(param_dict)

        # uuid、platform、v、loginToken 以及请求参数 排序
        # [('catId', '0'), ('hideAddProduct', '0'), ('limit', '20'), ('loginToken', 'c3617d9b|71354952|9a792158aa7b730d'), ('page', '0'), ('platform', 'android'), ('showHot', '1'), ('sortMode', '0'), ('sortType', '0'), ('timestamp', '1566182703058'), ('title', 'rtyuio'), ('typeId', '0'), ('uuid', '47e122719530a8fb'), ('v', '4.9.0')]
        lst = sorted(param_dict.items(), key=lambda x: x[0])


        # 排序后转为字符串
        # catId0hideAddProduct0limit20loginTokenc3617d9b|71354952|9a792158aa7b730dpage0platformandroidshowHot1sortMode0sortType0timestamp1566182703058titlertyuiotypeId0uuid47e122719530a8fbv4.9.0
        source_text = ''.join(map(lambda x: ''.join(x), lst))


        # 获取ase 加密后的密文
        # 加密算法为 AES加密模式ECB 填充方式pkcs5padding 数据块128位 b46afc89e13025d7
        # TODO 密钥b46afc89e13025d7
        ciphertext = self.cipher.encrypt(source_text)
        result = md5(ciphertext.encode('utf-8')).hexdigest()
        print('md5【%s】' % result)
        return result

    def du_get_sign(self):
        param_dict = {
            'uuid': UUID,
            'platform': 'android',
            'v': '4.9.0',
            'loginToken': ''
        }

        lst = sorted(param_dict.items(), key=lambda x: x[0])
        source_text = ''.join(map(lambda x: ''.join(x), lst))
        source_text = source_text + '3542e676b4c80983f6131cdfe577ac9b'
        ciphertext = self.cipher.encrypt(source_text)
        print(ciphertext)
        sign = md5(ciphertext.encode('utf-8')).hexdigest()
        print('sign 【%s】' % sign)
        return sign


    def du_get(self, url):
        timestamp = str(int(time.time() * 1000) - 3000)
        # timestamp = '1566266510060'
        values = {'userName': '17190184997',
                  'password': 'bedcc63d0ab1dbd23b1d62bedc7f0096',
                  'type': 'pwd',
                  'sourcePage': '',
                  'countryCode': '86',
                  'sign': self.du_get_sign()
                  }

        pdata = urllib.urlencode(values)

        newsign = self.get_new_sign(url + pdata, timestamp)
        self.du_headers['timestamp'] = timestamp
        link = "%s&newSign=%s" % (url, newsign)
        # link = "%s&sign=%s" % (url, newsign)
        print(url, timestamp, newsign)
        # quit() 'userName=17190184997&password=bedcc63d0ab1dbd23b1d62bedc7f0096&type=pwd&sourcePage=&countryCode=86'


        req = urllib2.Request(link, pdata, headers=self.du_headers)
        response = urllib2.urlopen(req)
        print(response.headers)
        print(response.read())


if __name__ == '__main__':
    spider = DuSpider()
    spider.du_get('https://m.poizon.com/users/unionLogin?')
    # spider.du_get('https://app.poizon.com/api/v1/app/index/ice/flow/product/detail?productId=39628&isChest=0')



