import requests
import json

"""
函数传入的参数：fields: 列表，['title'，'city']
            query: 字符串，"ip=1.1.1.1"
函数返回的内容：quake_data:[{'quake_total':total},{'title':'hahah','city':'taipei'}]
quake能返回的参数：ip,port,transport,asn,quake_update_time,org,is_ipv6,title,country,city_quake,isp,scene_en, hostname,protocol,status_code；
数据条数改变参数：data.size
"""


def quake_return(fields, flag=False):
    quake_data = []
    string = fields
    # print("quake搜索内容为：" + string + '\n')

    headers = {
        "X-QuakeToken": "e99f57d1-1f21-4af3-84c9-855adb15b19a"
    }
    data = {
        "query": string,  # 查询语句
        "start": 0,
        "size": 10
    }
    response = requests.post(url="https://quake.360.cn/api/v3/search/quake_service", headers=headers, json=data)

    rsp = json.loads(response.text)

    if flag is False:  # 只有页面二添加数据条数
        total = rsp['meta']['pagination']['total']
        print("quake", total)
        quake_data.append({'quake_total': total})

    # with open("quake返回的初始数据.txt",'w',encoding='utf-8')as f:
    #     f.write(str(rsp))

    for j in range(len(rsp['data'])):
        for j in range(len(rsp['data'])):
            temp = {'search': 'quake'}
            temp['ip'] = rsp['data'][j]['ip']
            # ip = 'ip:' + rsp['data'][j]['ip']
            temp['port'] = str(rsp['data'][j]['port'])
            # port = 'port:' + str(rsp['data'][j]['port'])
            temp['base_protocol'] = rsp['data'][j]['transport']
            # transport = 'transport:' + rsp['data'][j]['transport']
            temp['asn'] = str(rsp['data'][j]['asn'])
            # asn = 'ASN:' + str(rsp['data'][j]['asn'])
            temp['update_time'] = str(rsp['data'][j]['time']).split('T')[0]
            # update_time = 'update_time(360quake):' + str(rsp['data'][j]['time']).split('T')[0]
            temp['org'] = rsp['data'][j]['org']
            # org = 'org:' + rsp['data'][j]['org']
            temp['is_ipv6'] = str(rsp['data'][j]['is_ipv6'])
            # is_ipv6 = 'is_ipv6:' + str(rsp['data'][j]['is_ipv6'])
            try:
                temp['title'] = rsp['data'][j]['service']['http']['title'].strip().replace(' ', '').replace('|', '')[
                                :25]
                # title = 'title:' + rsp['data'][j]['service']['http']['title'].strip().replace(' ', '').replace('|', '')[:25]
            except KeyError:
                temp['title'] = ''
                # title = 'title:'
            temp['country'] = rsp['data'][j]['location']['country_cn']
            # country = 'country:' + rsp['data'][j]['location']['country_cn']
            temp['city'] = str(rsp['data'][j]['location']['city_en']).split(' ')[0]
            # city = 'city_360quake:' + str(rsp['data'][j]['location']['city_en']).split(' ')[0]
            temp['isp'] = rsp['data'][j]['location']['isp']
            # isp = 'isp:' + rsp['data'][j]['location']['isp']
            try:
                temp['scene_en'] = rsp['data'][j]['location']['scene_en']
                # scene_en = 'scene_en:' + rsp['data'][j]['location']['scene_en']
            except KeyError:
                temp['scene_en'] = ""
                # scene_en = 'scene_en:'
            try:
                temp['host'] = rsp['data'][j]['domain']
                # hostname = 'hostname:' + rsp['data'][j]['domain']
            except KeyError:
                temp['host'] = rsp['data'][j]['hostname']
                # hostname = 'hostname:' + rsp['data'][j]['hostname']
            temp['protocol'] = rsp['data'][j]['service']['name']
            # protocol = 'protocol:' + rsp['data'][j]['service']['name']
            try:
                temp['status_code'] = str(rsp['data'][j]['service']['http']['status_code'])
                # status_code = 'status_code:' + str(rsp['data'][j]['service']['http']['status_code'])
            except KeyError:
                temp['status_code'] = ''
                # status_code = 'status_code:'
            quake_data.append(temp)
            # print(temp)
            if flag:
                break
        if flag:
            break

    return quake_data


if __name__ == "__main__":
    # print(quake_return("ip:\"1.1.1.1\" and port:\"80\"", True))
    print(quake_return("city:taipei", False))
