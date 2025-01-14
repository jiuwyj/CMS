# -*- coding: utf-8 -*-
import zoomeye.sdk as zoomeye

"""
函数传入的参数：fields: 列表，['title'，'city']
            query: 字符串，"ip=1.1.1.1"
函数返回的内容：quake_data:[total,{'title':'hahah','city':'taipei'}]
zoomeye能返回的参数：ip,port,service,country,city,app,version,device,asn,zoomeye_update_time;
数据条数改变参数：page
"""


def zoomeye_return(query, flag=False):
    zm = zoomeye.ZoomEye()
    # zm.api_key = "0F8DE247-1E86-C5Ff6-E489-aAb17233c77"
    zm.api_key = "0D0377f1-c8da-83746-f133-694179b9a77"

    keyword = query
    page = 1
    datass = []
    back_content = []
    zoomeye_data = []

    begin_content = zm.multi_page_search(keyword, page)

    if flag is False:
        total = begin_content[0]["total"]
        print("zoomeye", total)
        zoomeye_data.append({'zoomeye_total': total})

    for item in begin_content[0]['matches']:
        temp = {}
        temp['search'] = 'zoomeye'
        temp["ip"] = item['ip']
        temp["port"] = item['portinfo']['port']
        temp["continent"] = item['geoinfo']['continent']['names']['en']
        temp["country"] = item["geoinfo"]["country"]['names']['en']
        temp["city"] = item["geoinfo"]["city"]['names']['en']
        temp['longitude'] = item['geoinfo']['location']['lon']
        temp['latitude'] = item['geoinfo']['location']['lat']
        temp['asn'] = item['geoinfo']['asn']
        temp['host'] = item['portinfo']['hostname']
        temp['os'] = item['portinfo']['os']
        try:
            temp['title'] = item['portinfo']['title']
        except KeyError:
            temp['title'] = ''
        try:
            temp['jarm'] = item['jarm']
        except KeyError:
            temp['jarm'] = ''
        temp['banner'] = item['portinfo']['banner']
        temp['base_protocol'] = item['protocol']['transport']
        temp['version'] = item['portinfo']['version']
        temp['update_time'] = item['timestamp']
        try:
            temp['isp'] = item['geoinfo']['isp']
        except KeyError:
            temp['isp'] = ''
        temp['app'] = item['portinfo']['app']
        temp['device'] = item['portinfo']['device']
        temp['scene_en'] = item['geoinfo']['scene']['en']
        temp['organization'] = item['geoinfo']['organization']
        temp['protocol'] = item['protocol']['application']

        zoomeye_data.append(temp)
        if flag:
            break
    return zoomeye_data

    # with open('zoomeye返回的结果.txt', 'w', encoding='utf-8') as f:
    #     f.write(str(zoomeye_data))


if __name__ == "__main__":
    print(zoomeye_return("city:Taipei", False))
