# -*- coding: utf-8 -*-
'''
作用：统计返回的数据来自哪些国家，在每个国家有多少条数据，（页面二 地图的数据来源）
输入数据：页面二搜索返回的结果
返回数据格式：
{'China': 2, 'Japan': 1}
Time:2024/1/13
'''

from . import zhtoen
import time


def areas_count(datas):
    def is_chinese(char):  # 判断是否为中文名
        if '\u4e00' <= char <= '\u9fff':
            return True
        else:
            return False

    count_areas = {}
    I_love_China = ["Taiwan", "Hong Kong", "Macao"]  # 港澳台地区
    warehouse = {}
    for item in datas:
        # print(item['country'])
        if is_chinese(item['country'][0]):  # 国家名中文翻译成英文
            # print(item['country'])

            if item['country'] in warehouse.keys():  # 该数据的国家，在列表中已经存在，不用再进行翻译了，减少翻译API的条用次数
                item['country'] = warehouse[item['country']]
            else:
                warehouse[item['country']] = zhtoen.tanslate(item['country'])
                time.sleep(2)  # 太快的话翻译api,会出问题
                item['country'] = warehouse[item['country']]
            # item['country']=zhtoen.tanslate(item['country'])

        if item['country'] in I_love_China:  # 处理国外网站的港澳台问题
            item['country'] = "China"

        if item['country'] not in count_areas:
            count_areas[item['country']] = 1
        else:
            count_areas[item['country']] += 1

    return count_areas


if __name__ == "__main__":
    a = [{'ip': '1.161.97.145', 'port': '8291', 'country': 'China', 'city': 'Taipei', 'protocol': ''}, {'ip': '1.162.95.222', 'port': '80', 'country': 'China', 'city': 'Taipei', 'protocol': ''}, {'ip': '101.3.108.25', 'port': '5357', 'protocol': 'http', 'country': 'China', 'city': 'Taipei City'}, {'ip': '103.169.213.71', 'port': '1935', 'country': 'China', 'city': 'Taipei', 'protocol': ''}, {'ip': '103.59.110.245', 'port': '9305', 'country': 'China', 'city': 'Taipei', 'protocol': 'unknown/ssl'}, {'ip': '111.241.5.3', 'port': '505', 'protocol': 'mailbox-lm', 'country': 'China', 'city': 'New Taipei City'}, {'ip': '111.249.193.249', 'port': '21', 'country': 'China', 'city': 'Taipei', 'protocol': 'ftp'}, {'ip': '112.104.54.232', 'port': '81', 'protocol': 'http', 'country': 'China', 'city': 'Taipei City'}, {'ip': '113.196.137.75', 'port': '5555', 'protocol': 'http', 'country': 'China', 'city': 'Taipei City'}, {'ip': '118.163.197.188', 'port': '1723', 'country': 'China', 'city': 'Taipei', 'protocol': ''}, {'ip': '118.163.68.115', 'port': '1041', 'protocol': 'danf-ak2', 'country': 'China', 'city': 'New Taipei City'}, {'ip': '118.163.69.80', 'port': '443', 'country': 'China', 'city': 'Taipei', 'protocol': 'unknown/ssl'}, {'ip': '118.165.198.149', 'port': '1041', 'protocol': 'danf-ak2', 'country': 'China', 'city': 'Taipei City'}, {'ip': '120.97.121.94', 'port': '443', 'country': 'China', 'city': 'New', 'protocol': 'http/ssl'}, {'ip': '124.218.218.125', 'port': '6699', 'protocol': 'http', 'country': 'China', 'city': 'New Taipei City'}, {'ip': '124.9.9.241', 'port': '80', 'country': 'China', 'city': 'New', 'protocol': 'http'}, {'ip': '154.19.161.67', 'port': '443', 'country': 'China', 'city': 'Taipei', 'protocol': 'http/ssl'}, {'ip': '172.217.163.51', 'port': '443', 'country': 'China', 'city': 'Taipei', 'protocol': 'http/ssl'}, {'ip': '175.99.135.210', 'port': '443', 'country': 'China', 'city': 'Taipei', 'protocol': 'http/ssl'}, {'ip': '175.99.199.63', 'port': '49152', 'country': 'China', 'city': 'Taipei', 'protocol': ''}, {'ip': '202.132.16.187', 'port': '6379', 'protocol': 'redis', 'country': 'China', 'city': 'Taipei City'}, {'ip': '202.153.175.7', 'port': '6998', 'protocol': 'smtp', 'country': 'China', 'city': 'Taipei City'}, {'ip': '210.71.227.163', 'port': '80', 'country': 'China', 'city': 'Taipei', 'protocol': ''}, {'ip': '211.75.189.176', 'port': '80', 'country': 'China', 'city': 'Taipei', 'protocol': ''}, {'ip': '218.32.92.30', 'port': '443', 'country': 'China', 'city': 'Taipei', 'protocol': 'http/ssl'}, {'ip': '220.228.6.176', 'port': '80', 'country': 'China', 'city': 'Taipei', 'protocol': 'http'}, {'ip': '34.80.144.40', 'port': '9091', 'protocol': 'telnet', 'country': 'China', 'city': 'Taipei City'}, {'ip': '34.80.154.249', 'port': '9091', 'protocol': 'http', 'country': 'China', 'city': 'Taipei City'}, {'ip': '34.80.207.215', 'port': '9091', 'protocol': 'http', 'country': 'China', 'city': 'Taipei City'}, {'ip': '34.80.87.232', 'port': '9091', 'protocol': 'http', 'country': 'China', 'city': 'Taipei City'}, {'ip': '34.81.136.15', 'port': '9091', 'protocol': 'telnet', 'country': 'China', 'city': 'Taipei City'}, {'ip': '34.81.178.44', 'port': '9091', 'protocol': 'http', 'country': 'China', 'city': 'Taipei City'}, {'ip': '34.81.182.11', 'port': '9091', 'protocol': 'telnet', 'country': 'China', 'city': 'Taipei City'}, {'ip': '34.81.192.208', 'port': '9091', 'protocol': 'http', 'country': 'China', 'city': 'Taipei City'}, {'ip': '34.81.4.9', 'port': '9091', 'protocol': 'http', 'country': 'China', 'city': 'Taipei City'}, {'ip': '34.81.63.247', 'port': '9091', 'protocol': 'http', 'country': 'China', 'city': 'Taipei City'}, {'ip': '36.224.192.209', 'port': '16923', 'protocol': 'https', 'country': 'China', 'city': 'Taipei City'}, {'ip': '36.225.0.169', 'port': '80', 'country': 'China', 'city': 'Taipei', 'protocol': ''}, {'ip': '45.223.132.108', 'port': '2082', 'country': 'China', 'city': 'Taipei', 'protocol': ''}, {'ip': '61.64.60.206', 'port': '80', 'country': 'China', 'city': 'Taipei', 'protocol': ''}]
    print(areas_count(a))
    # print(a[0].keys())
