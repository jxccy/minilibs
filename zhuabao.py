# -*- coding:utf-8 -*-

from io import BytesIO
import json
from os import getenv
import time

from flask import Flask, request, jsonify, Response
import requests
from PIL import Image




def get_capture_code(data, url='http://localhost:6600/verify'):
    files = {'image_file': data}
    res = requests.post(url, files=files)
    return res.json().get('value')


def response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app = Flask(__name__)


@app.route('/verify', methods=['POST'])
def up_image():
    if request.method == 'POST' and request.files.get('txt'):
        start_time = time.time()
        timec = str(time.time()).replace(".", "")
        file = request.files.get('txt')
        file.save('zhuabao/%s.txt' % (time.time() * 1000))
        print(file.stream.read())
        return jsonify({})

if __name__ == '__main__':
    app.run(port=6600, host='0.0.0.0')
