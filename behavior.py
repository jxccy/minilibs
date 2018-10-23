# -*- coding:utf-8 -*-
import json
import random
import time

import requests

get_userid = lambda: str(int(random.random() * 10 ** 6))
get_itemid = lambda: str(int(random.random() * 10 ** 9))
get_score = lambda: str(random.choice(range(10)))


def get_body():
    res = [get_userid(), get_itemid()]
    for i in range(10):
        res.append(get_score())
    res.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    return '|'.join(res)


def request():
    headers = {"h1": "v1", "h2": "v2"}
    data = [{'headers': headers}, {'body': get_body()}]
    url = 'http://192.168.0.161:50000'
    requests.post(url=url, data=json.dumps(data))


if __name__ == '__main__':
    while True:
        request()
        time.sleep(1)
