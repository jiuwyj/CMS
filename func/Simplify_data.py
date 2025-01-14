# -*- coding: utf-8 -*-
"""
作用：对返回的数据进行简化，挑选几个常见的字段，面向页面二（搜索结果列表页面）的数据返回
挑选的数据：['ip','port','city','country','protocol']
输入的数据：页面二搜索返回的数据
返回的数据格式：
[
{'ip': '123', 'port': '22', 'city': 'xiangtan', 'country': 'China', 'protocol': 'htttp'},
{'ip': '133', 'port': '22', 'city': 'xiangtan', 'country': 'China', 'protocol': 'htttp'},
{'ip': '143', 'port': '22', 'city': 'xiangtan', 'country': 'China', 'protocol': 'htttp'}
]
Time:2024/1/13
"""
import time

from . import zhtoen

warehouse={}
country_name={'美国':"United States",'德国':'Germany','日本':'Japan'}
I_love_China=["Taiwan","Hong Kong","Macao","中国台湾省",'中国香港特别行政区']#港澳台地区
def is_chinese(char):  # 判断是否为中文名
    if '\u4e00' <= char <= '\u9fff':
        return True
    else:
        return False
def process_for_region(name):
    if name in I_love_China:
        name="China"
        return name
    if is_chinese(name[0]):#为中文字符

        if name in country_name:
            name=country_name[name]
        else:
            warehouse[name]=zhtoen.tanslate(name)
            time.sleep(1)
            name=warehouse[name]

    return name

def same_country_sum(datas):#把相同国家的内容进行求和
    ok=[]
    t=[]
    for item in datas:
        if item['name'] not in ok:
            ok.append(item['name'])
            t.append(item)
        else:
            for ii in t:
                if ii['name'] == item['name']:
                    ii['count']+=item['count']

    return t

def simplify_data(datas):
    Simplified_datas = []
    flag=['ip','port','city','country','protocol','banner']
    for item in datas:
        tmp={}
        for thing in item:
            if thing in flag:
                if thing == "country":#统一国家格式
                    tmp[thing]=process_for_region(item[thing])
                else:
                    tmp[thing]=item[thing]
        Simplified_datas.append(tmp)
    # print(Simplified_datas)
    return Simplified_datas

def process_data_page_3(datas):
    for item in datas:
        item['country']=process_for_region(item['country'])
    return datas

def process_data_for_rank(datas):
    for item in datas['country']:
        item['name']=process_for_region(item['name'])

    datas['country']=same_country_sum(datas['country'])



    return datas


if __name__ == "__main__":
    a = [{'ip': '103.169.213.91', 'port': '3088', 'country': 'Taiwan', 'city': 'Taipei', 'protocol': ''},
{'ip': '104.123.220.50', 'port': '80', 'country': 'Taiwan', 'city': 'Taipei', 'protocol': ''},
{'ip': '114.24.34.239', 'port': '111', 'country': 'Taiwan', 'city': 'Taipei', 'protocol': ''},
{'ip': '114.44.132.76', 'port': '8443', 'country': '中国', 'city': 'New', 'protocol': 'http/ssl'},
{'ip': '118.160.157.192', 'port': '53', 'country': '中国', 'city': 'Taipei', 'protocol': 'dns'},
{'ip': '118.165.27.12', 'port': '80', 'protocol': 'http', 'country': '中国台湾省', 'city': 'Taipei'},
{'ip': '119.75.243.223', 'port': '8000', 'country': 'Taiwan', 'city': 'Taipei', 'protocol': ''},
{'ip': '120.102.204.204', 'port': '161', 'protocol': 'snmp', 'country': 'China', 'city': 'New Taipei City'},
{'ip': '120.102.204.230', 'port': '161', 'protocol': 'snmp', 'country': 'China', 'city': 'New Taipei City'},
{'ip': '120.96.248.6', 'port': '161', 'protocol': 'snmp', 'country': 'China', 'city': 'Taipei City'},
{'ip': '125.227.31.252', 'port': '80', 'protocol': 'http', 'country': '中国台湾省', 'city': 'Taipei'},
{'ip': '125.228.204.46', 'port': '80', 'country': 'Taiwan', 'city': 'Taipei', 'protocol': ''},
{'ip': '125.228.236.240', 'port': '443', 'protocol': 'https', 'country': '中国台湾省', 'city': 'Taipei'},
{'ip': '128.1.141.148', 'port': '123', 'protocol': 'ntp', 'country': 'China', 'city': 'Taipei City'},
{'ip': '128.1.141.149', 'port': '123', 'protocol': 'ntp', 'country': 'China', 'city': 'Taipei City'},
{'ip': '128.1.141.157', 'port': '123', 'protocol': 'ntp', 'country': 'China', 'city': 'Taipei City'},
{'ip': '130.211.241.27', 'port': '80', 'protocol': 'http', 'country': '中国台湾省', 'city': 'Taipei'},
{'ip': '150.116.194.205', 'port': '443', 'protocol': 'https', 'country': '中国台湾省', 'city': 'Taipei'},
{'ip': '150.116.43.243', 'port': '443', 'protocol': 'https', 'country': '中国台湾省', 'city': 'Taipei'},
{'ip': '163.21.190.42', 'port': '80', 'country': '中国', 'city': 'Taipei', 'protocol': 'http'},
{'ip': '175.98.113.136', 'port': '80', 'country': '中国', 'city': 'Taipei', 'protocol': 'http'},
{'ip': '175.98.119.200', 'port': '443', 'country': '中国', 'city': 'Taipei', 'protocol': 'http/ssl'},
{'ip': '185.218.221.220', 'port': '443', 'protocol': 'https', 'country': '中国台湾省', 'city': 'Taipei'},
{'ip': '202.168.203.57', 'port': '1337', 'protocol': 'http', 'country': 'China', 'city': 'Taipei City'},
{'ip': '203.66.191.179', 'port': '8888', 'country': '中国', 'city': 'Taipei', 'protocol': 'http/ssl'},
{'ip': '210.59.192.122', 'port': '10001', 'protocol': 'http', 'country': 'China', 'city': 'Taipei City'},
{'ip': '210.59.192.124', 'port': '10001', 'protocol': 'http', 'country': 'China', 'city': 'Taipei City'},
{'ip': '210.59.192.125', 'port': '10001', 'protocol': 'http', 'country': 'China', 'city': 'Taipei City'},
{'ip': '210.61.180.140', 'port': '10001', 'protocol': 'https', 'country': 'China', 'city': 'Taipei City'},
{'ip': '210.61.180.173', 'port': '10001', 'protocol': 'https', 'country': 'China', 'city': 'Taipei City'},
{'ip': '210.61.180.26', 'port': '10001', 'protocol': 'https', 'country': 'China', 'city': 'Taipei City'},
{'ip': '210.61.180.28', 'port': '10001', 'protocol': 'https', 'country': 'China', 'city': 'Taipei City'},
{'ip': '210.61.180.44', 'port': '10001', 'protocol': 'https', 'country': 'China', 'city': 'Taipei City'},
{'ip': '210.61.180.46', 'port': '10001', 'protocol': 'https', 'country': 'China', 'city': 'Taipei City'},
{'ip': '210.61.180.73', 'port': '10001', 'protocol': 'https', 'country': 'China', 'city': 'Taipei City'},
{'ip': '210.63.236.1', 'port': '10001', 'protocol': 'telnet', 'country': 'China', 'city': 'New Taipei City'},
{'ip': '211.75.124.87', 'port': '25', 'country': '中国', 'city': 'Taipei', 'protocol': 'smtp'},
{'ip': '220.228.131.175', 'port': '3306', 'country': '中国', 'city': 'Taipei', 'protocol': 'mysql'},
{'ip': '220.228.6.134', 'port': '3306', 'country': 'Taiwan', 'city': 'Taipei', 'protocol': ''},
{'ip': '36.227.6.62', 'port': '80', 'protocol': 'http', 'country': '中国台湾省', 'city': 'Taipei'},
{'ip': '45.206.37.18', 'port': '8888', 'country': 'Taiwan', 'city': 'Taipei', 'protocol': ''},
{'ip': '59.124.224.229', 'port': '443', 'protocol': 'https', 'country': '中国台湾省', 'city': 'Taipei'},
{'ip': '60.250.81.79', 'port': '80', 'country': 'Taiwan', 'city': 'Taipei', 'protocol': ''},
{'ip': '60.251.156.23', 'port': '53', 'country': 'Taiwan', 'city': 'Taipei', 'protocol': ''},
{'ip': '61.219.4.17', 'port': '443', 'country': '中国', 'city': 'Taipei', 'protocol': 'unknown/ssl'},
{'ip': '61.220.129.174', 'port': '443', 'protocol': 'https', 'country': '中国台湾省', 'city': 'Taipei'},
{'ip': '61.230.220.38', 'port': '1911', 'protocol': 'http', 'country': 'China', 'city': 'New Taipei City'},
{'ip': '61.230.222.80', 'port': '1911', 'protocol': 'http', 'country': 'China', 'city': 'New Taipei City'},
{'ip': '61.61.127.78', 'port': '80', 'country': '中国', 'city': 'Taipei', 'protocol': 'http'},
{'ip': '61.61.97.196', 'port': '993', 'country': 'Taiwan', 'city': 'Taipei', 'protocol': ''}]
    # for i in simplify_data(a):
    #     print(i["country"]+"---"+i["city"])
    # # print(simplify_data(a))
    # print(warehouse)
    ans = {'protocol': [{'count': 137027580, 'name': 'https'},
                        {'count': 73568398, 'name': 'http'},
                        {'count': 8854695, 'name': 'tls'},
                        {'count': 4102512, 'name': 'kubernetes(https)'},
                        {'count': 1244534, 'name': 'unknown'}],
           'server': [{'count': 193217370, 'name': 'nginx'},
                      {'count': 173610749, 'name': 'cloudflare'},
                      {'count': 155418137, 'name': 'Apache'},
                      {'count': 104087681, 'name': 'CloudFront'}],
           'port': [{'count': 1105682216, 'name': '443'}],
           'country': [{'name': '美国', 'count': 549848486},
                       {'name': '德国', 'count': 95344536},
                       {'name': '中国香港特别行政区', 'count': 44639988},
                       {'name': '中国', 'count': 36930948},
                       {'name': '日本', 'count': 30358585}]}
    print(process_data_for_rank(ans))
    for item in process_data_for_rank(ans):
        print(item)
        print(ans[item])