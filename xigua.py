import requests
import base64
import random
import urllib3
import binascii
import re
import json
import execjs
# from selenium.webdriver.chrome.options import Options
urllib3.disable_warnings()
# url = 'https://www.ixigua.com/i6802834612604109324/'
url = 'https://www.ixigua.com/home/50619338036/'
# headers = {
#    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
#    'referer': url
# }


headers = {
    'authority': 'www.ixigua.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Mobile Safari/537.36',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'wafid=e24888de-e1c7-4251-9a23-93a4e4fd1601; wafid.sig=C-Gc_yg4OnVaIDSkQ6tga58E2Y4; ttwid=6805088624469837319; ttwid.sig=B-9Gn1T2EMPntSl7tNQQktkc9Mc; xiguavideopcwebid=6805088624469837319; xiguavideopcwebid.sig=klEVdnqFMs-NBXA2CIxDpUAKe-Q; SLARDAR_WEB_ID=48bc78ce-c522-4202-8e76-b596cd87554a; _ga=GA1.2.1390664465.1584433170; _gid=GA1.2.1693679238.1584433170; s_v_web_id=k7vmlwln_j3foV0Bl_Wh5M_4GAa_Akca_Z8SWZPyghtOY; ixigua-a-s=1; tt_webid=6805183787628234247; OUTFOX_SEARCH_USER_ID_NCOO=1474718756.742217',
}


def get_video():
    response = requests.get(url, headers=headers,  verify=False) #  
    # response = requests.get(url=url, headers=headers)
    print(response)
    html = response.text
    pattern = re.compile('id="SSR_HYDRATED_DATA">(.*?)</script>', re.S)
    with open('test.html', 'wb') as wf:
        wf.write(response.content)
    result = re.findall(pattern, html)
    if result:
        video_detail = json.loads(result[0].replace('window._SSR_HYDRATED_DATA=', ''))
        videoId = video_detail.get("Projection").get("video").get("vid")
        print(videoId)
        
        if videoId:
            video_url = "http://api.huoshan.com/hotsoon/item/video/_playback/?video_id=" + videoId
            video_response = requests.get(video_url, headers, allow_redirects=False)
            print(video_response.headers['location'])
            return video_response.headers['location']

            # r = str(random.random())[2:]
            # # 视频的唯一ID + 随机数 + CRC32校验值
            # video_url_first = '/video/urls/v/1/toutiao/mp4/%s?r=%s' % (videoId, r)
            # b_url = bytes(video_url_first, encoding="utf-8")
            # c = binascii.crc32(b_url)
            # video_url = "http://i.snssdk.com" + video_url_first + "&s=%s" % c  #接口地址
            # print(video_url)
            # video_response = requests.get(video_url, headers)
            # json_video_html = json.loads(video_response.text)
            # main_url = json_video_html.get('data').get('video_list').get('video_1').get('main_url') #取base串
            # if main_url:
            #     bs64 = base64.standard_b64decode(main_url)
            #     down_url = str(bs64, 'utf-8')
            #     print(down_url)

get_video()