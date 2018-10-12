# -*- coding:utf-8 -*-
import json
import random
import re

import requests

def get_userid():
    return str(int(random.random()*100000000))

def get_itemid():
    def get_str():
        lst = re.findall('\w', 'qwertyuiopasdfghjklzxcvbnm1234567890')
        return random.choice(lst)
    return ''.join([get_str() for i in range(10)])

def get_score():
    return random.choice(re.findall('\w', '1234567890'))

def get_body():
    userid = get_userid()
    itemid = get_itemid()
    res = [userid, itemid]
    for i in range(10):
        res.append(get_score())
    return '|'.join(res)

def request():
    headers = {"h1": "v1", "h2": "v2"}
    data = [{'headers': headers}, {'body': get_body()}]
    url = 'http://192.168.0.161:50000'
    requests.post(url=url, data=json.dumps(data))

if __name__ == '__main__':
    request()
