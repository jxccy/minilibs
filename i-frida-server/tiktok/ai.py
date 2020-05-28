# -*- coding: utf-8 -*-

from flask import Blueprint, request, jsonify

from tiktok.AwemeUtil import AwemeUtil

app_topspeed = Blueprint("topspeed", __name__)

topspeed_rpc = None

au = AwemeUtil()

def setTopspeed203Rpc(rpc):
    global topspeed_rpc
    topspeed_rpc = rpc


@app_topspeed.route("/getmas")
def getmas():
    try:
        device_id = request.args.get('device_id')
        i = request.args.get('i')
        url = request.args.get('url')
        body = request.args.get("body")
    except Exception as e:
        return "异常情况"
    else:
        return topspeed_rpc.getmas(i, url, body, device_id)
