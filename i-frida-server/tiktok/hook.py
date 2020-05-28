# -*- coding: utf-8 -*-
import frida
import sys, os, codecs


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


class tksp(object):
    rpc = None

    def __init__(self):
        print(" tksp_203 HOOK 模块初始化 ")
        pass

    def hook_start(self):
        print(" hook_start ")
        try:
            project_path = os.path.dirname(os.path.realpath(__file__))
            rpc_path = os.path.join(project_path, "rpc.js").replace("\\", "/")
            utils_path = os.path.join(project_path[0:project_path.find("tiktok")], "tools/utils.js").replace("\\", "/")

            source = ""

            with codecs.open(rpc_path, 'r', 'utf-8') as f:
                source += f.read()

            with codecs.open(utils_path, 'r', 'utf-8') as f:
                source += f.read()

            process = frida.get_usb_device().attach('com.ss.android.ugc.aweme.lite')
            script = process.create_script(source)
            script.on('message', on_message)
            script.load()
            rpc = script.exports
        except Exception as e:
            print("异常情况!")
        else:
            return rpc
