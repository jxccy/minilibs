# -*- coding:utf-8 -*-
import json
import random
import time

import requests

get_userid = lambda: str(int(random.random() * 10 ** 6))
get_itemid = lambda: str(int(random.random() * 10 ** 9))
get_scores = lambda x: random.choices(range(10), k=x)


def get_body():
    res = [get_userid(), get_itemid()]
    res.extend(map(lambda x: str(x), get_scores(10)))
    res.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    return '|'.join(res)


def request():
    headers = {"h1": "v1", "h2": "v2"}
    data = [{'headers': headers, 'body': get_body()}]
    url = 'http://192.168.0.161:50000'
    res = requests.post(url=url, data=json.dumps(data))

if __name__ == '__main__':
    while True:
        request()
        time.sleep(1)
