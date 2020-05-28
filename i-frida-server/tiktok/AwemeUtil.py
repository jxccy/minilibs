#!/usr/bin/python3
# encoding: utf-8

import hashlib


class AwemeUtil(object):
    HEX_CHARS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    def __init__(self):
        pass

    @classmethod
    def str2md5_hex_str(cls, string):
        if string:
            m2 = hashlib.md5()
            m2.update(string.encode('UTF-8'))
            string_md5 = m2.hexdigest()
            return string_md5
        return None

    @classmethod
    def format_url(cls, url):
        index = url.index("?") if "?" in url else -1
        index_2 = url.index("#") if "#" in url else -1
        if index == -1:
            return None
        if index_2 == -1:
            return url[index + 1:]
        if index_2 < index:
            return None
        return url[index + 1: index_2]

    @classmethod
    def format_session_id(cls, cookie):
        for str2 in cookie.replace(" ", "").split(","):
            index = str2.index("sessionid=") if 'sessionid=' in str2 else -1
            if index != -1:
                return str2[index + 10:]
        return None

    @classmethod
    def init_gorgon(cls, url, headers):
        format_url = cls.format_url(url)
        str2 = None
        a2 = cls.str2md5_hex_str(format_url) if format_url else None
        str3 = None
        str4 = None
        for k, v in headers.items():
            if "X-SS-STUB" in k.upper():
                str2 = v
            if "COOKIE" in k.upper():
                if v:
                    str3 = cls.str2md5_hex_str(v)
                    format_session_id = cls.format_session_id(v)
                    str4 = cls.str2md5_hex_str(format_session_id) if format_session_id else None

        a2 = a2 if a2 else "00000000000000000000000000000000"
        str2 = str2 if str2 else "00000000000000000000000000000000"
        st3 = str3 if str3 else "00000000000000000000000000000000"
        st4 = str4 if str4 else "00000000000000000000000000000000"

        result_sb = a2 + str2 + st3 + st4
        return result_sb.lower()
