# -*- coding: utf-8 -*-
import requests
import random
import json
from hashlib import md5
def tanslate(a):#中文转英文
    appid = '20230607001704035'
    appkey = '0VU2_HBILTHfeB3h5Hxk'
    from_lang = 'zh'
    to_lang =  'en'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    query = a
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    result_text = result['trans_result'][0]['dst']
    return  result_text

def translate_en_to_zh(a):#英文转中文
    appid = '20230607001704035'
    appkey = '0VU2_HBILTHfeB3h5Hxk'
    from_lang = 'en'
    to_lang = 'zh'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    query = a

    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    result_text = result['trans_result'][0]['dst']
    return result_text

if __name__ == "__main__":
    print(translate_en_to_zh("Taipei"))