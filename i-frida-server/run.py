from flask import Flask

from tiktok.ai import app_topspeed, setTopspeed203Rpc
from tiktok.hook import tksp

app = Flask(__name__)

app.register_blueprint(app_topspeed)

@app.route("/test")
def test():
    return "test"


if __name__ == '__main__':
    try:
        tksp_203_rpc = tksp().hook_start()
        setTopspeed203Rpc(tksp_203_rpc)
    except Exception as e:
        print("异常情况")
    else:
        app.run(host='0.0.0.0', port=5001);