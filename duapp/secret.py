# -*- coding: utf-8 -*-
from copy import deepcopy
from hashlib import md5
import time
from urllib.request import urlparse

import requests

UUID = '47e122719530a8fb'
LOGINTOKEN = 'c3617d9b|71354952|9a792158aa7b730d'
COOKIE = 'duToken=b6ad1582%7C71354952%7C1566007923%7Cd30cab02b84f60eb'
DUIMEI = '865291027268324'
SHUMEIID = '20190809184612376b65d6946c9325778fad1f880057b901b8ffb9c2d54166'


class DuSpider(object):
    param_dict = {
        'uuid': UUID,
        'platform': 'android',
        'v': '4.9.0',
        # 'loginToken': LOGINTOKEN
    }

    du_headers = {
        'Cookie': COOKIE,
        'duuuid': param_dict['uuid'],
        'duimei': DUIMEI,
        'duplatform': 'android',
        'duchannel': 'xiaomi',
        'duv': param_dict['v'],
        'dulogintoken': param_dict['loginToken'],
        'dudevicetrait': 'MI+4W',
        'shumeiid': SHUMEIID,
        'user-agent': 'duapp/4.9.0(android;6.0.1)'

    }

    def get_sign(self, url, timestamp):
        param_dict = deepcopy(self.param_dict)
        param_dict['timestamp'] = timestamp
        params = urlparse(url).query
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
        headers = {
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': '*/*',
            'Cache-Control': 'no-cache',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': '__cfduid=d591c8450a4555c2a6a4d81fa83b1dd441566193618; __yjsv3_shitong=1.0_7_9beef12eea585070913d92b9aa480591b483_300_1566193618640_118.194.246.217_07dd5ea3; cf_clearance=2412f1bedc5423640c6d0af5d706ce502a6a668f-1566193631-31536000-250; Hm_lvt_ef483ae9c0f4f800aefdf407e35a21b3=1566193632; Hm_lpvt_ef483ae9c0f4f800aefdf407e35a21b3=1566193632; yjs_id=aHR0cDovL3Rvb2wuY2hhY3VvLm5ldC9jZG4tY2dpL2wvY2hrX2pzY2hsP3M9ODExODBlNWYwZDAxZjc4ODA1MDA5MTBlZWQ2M2M2ZDNlYmEyNzYxMC0xNTY2MTkzNjE4LTE4MDAtQVk4dFFpWjZiN1FEa0RKMXV3eUxYbWw0dUh2SHQlMkJBRm1idndoMzIwRmIzTyUyRjNHRVJNZHFOR0hMekhqbFRJSlglMkZSN25oaEpaM00zeHNVUk5uRTFaUGloJTJGRDBES1RmVkFtWTY0aFNWTVpmendFanFrckQwdjBqbFE5TlElMkJQZ1p3ZXclM0QlM0QmanNjaGxfdmM9MWZkMTE2ZDlkN2VkNDZmYzdkZDk2Y2QyOWRhNzE2NzUmcGFzcz0xNTY2MTkzNjIwLjM2MS1kNzMwSmVTYWFaJmpzY2hsX2Fuc3dlcj0yMi4wNDc4NTEwOTg2fDE1NjYxOTM2MzE5NzU; ctrl_time=1; bdshare_firstime=1566193632026',
            'Connection': 'keep-alive',
            'Referer': 'http://tool.chacuo.net/cryptaes'
        }

        # 获取ase 加密后的密文
        # 加密算法为 AES加密模式ECB 填充方式pkcs5padding 数据块128位 b46afc89e13025d7
        # TODO 密钥b46afc89e13025d7
        jmurl = 'http://tool.chacuo.net/cryptaes'
        pdata = 'data={source_text}&type=aes&arg=m%3Decb_pad%3Dpkcs5_block%3D128_p%3Db46afc89e13025d7_o%3D0_s%3Dgb2312_t%3D0'.format(
            source_text=source_text)
        resp = requests.post(jmurl, data=pdata, headers=headers)
        ciphertext = ''.join(resp.json()['data'])
        print(source_text)
        print(ciphertext)
        result = md5(ciphertext.encode('utf-8')).hexdigest()
        print('md5【%s】' % result)
        return result

    def du_get(self, url):
        # timestamp = str(int(time.time() * 1000) - 3000)
        timestamp = '1566214817436'
        newsign = self.get_sign(url, timestamp)
        quit()

        self.du_headers['timestamp'] = timestamp
        link = "%s&newSign=%s" % (url, newsign)
        # link = "%s&sign=%s" % (url, newsign)
        resp = requests.get(url=link, headers=self.du_headers)
        print(resp.text)
        print(url, timestamp, newsign)

    def single(self):
        headers = {
            'Cookie': 'duToken=b6ad1582%7C71354952%7C1566007923%7Cd30cab02b84f60eb',
            'duuuid': '47e122719530a8fb',
            'duimei': '865291027268324',
            'duplatform': 'android',
            'duchannel': 'xiaomi',
            'duv': '4.9.0',
            'dulogintoken': 'c3617d9b|71354952|9a792158aa7b730d',
            'dudevicetrait': 'MI+4W',
            'timestamp': '1566013355639',
            'shumeiid': '20190809184612376b65d6946c9325778fad1f880057b901b8ffb9c2d54166',
            'user-agent': 'duapp/4.9.0(android;6.0.1)'
        }

        headers = self.du_headers
        headers['timestamp'] = '1566013355639'
        print(headers)
        quit()
        link = 'https://app.poizon.com/api/v1/app/index/ice/shoppingTab?lastId=6&limit=20&tabId=13&newSign=8c398528ad423e50fd3097d9cd508c84'
        resp = requests.get(url=link, headers=headers)
        print(resp.text)

if __name__ == '__main__':
    spider = DuSpider()
    spider.du_get('https://app.poizon.com?userName=17190184997&password=bedcc63d0ab1dbd23b1d62bedc7f0096&type=pwd&sourcePage=&countryCode=86&sign=806832994f57ddd43b4106f219943407')
    # spider.du_get('https://app.poizon.com/api/v1/app/index/ice/flow/product/detail?productId=39628&isChest=0')
