import base64
import requests
import json
from . import zhtoen

"""
函数传入的参数：fields: 列表，['title'，'city']
            query: 字符串，"ip=1.1.1.1"
函数返回的内容：quake_data:[total,{'title':'hahah','city':'taipei'}]
zoomeye能返回的参数：ip, port, url, protocol, base_protocol, status_code, as_org, country, province, city, isp,title, update_time
数据条数改变参数：page
time:2024/4/6
"""


def hunter_return(query, flag):
    print(query)
    # if query.split("=")[0] =='ip.city':
    #     query ='ip.city = '+zhtoen.translate_en_to_zh(query.split("=")[1])
    # print(query)
    fan={'"Taipei"':'台北','"taipei"':'台北'}

    if query.split("=")[0] =='ip.city':
        if query.split("=")[1] in fan:
            query = 'ip.city = ' + fan[query.split("=")[1]]
        else:
            query ='ip.city = '+zhtoen.translate_en_to_zh(query.split("=")[1])

    api_key = r'0dc874538ca26c4101979fc928739615f7c1ae053f083043658505de901f8251'
    search = base64.urlsafe_b64encode(query.encode("utf-8"))
    search_result = str(search, 'utf8')
    page = '1'
    page_size = '1'  # 不能随便改，会报错：页面数据条数不合法
    is_web = '3'
    api = 'https://hunter.qianxin.com/openApi/search?api-key=' + str(api_key) + '&search=' + str(
        search_result) + '&page=' + str(page) + '&page_size=' + str(page_size) + '&is_web=' + str(is_web)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        'Cookie': "next=https%3A//hunter.qianxin.com/api/uLogin; Hm_lvt_64787111d439a06146c3a4be00dda632=1698932731,1700011588,1700036040; wzws_sessionid=gmQ0ZjAxMoFjZTU4YTWAMjQwZTo0Njg6MTIwOjg2Zjo5ZTU6N2RjMzoyZDQwOjM3NmKgZaCFbg==; User-Center=51054de3-4ef3-45b6-85a2-6c9d09a54f3c; __8qcehdE7ZaRq2q6M__=b5d4c9c5cb958b7f73ac315645e4b68a; token=4gw9B%3A36fc64b1-0eaa-4558-a359-260f97dae864; session_id=e354eebc330b1180bb566b16e2b3ee142ca7a1c61d6ecee19f84cc47bb8ae5b6"
        # 这里的cookie要自己填
    }

    try:
        response = requests.get(api, headers)
        hunter_data = []
        rsp = json.loads(response.text)
        # with open("hunter返回的初始内容.txt", "w", encoding='utf-8') as f:
        #     f.write(str(rsp))
        if flag is False:  # 只有在页面二才统计数据条数
            total = rsp['data']['total']  # 数据总条数
            print('hunter', total)
            hunter_data.append({'hunter_total': total})

        if rsp['data']['arr']:
            for arr in rsp['data']['arr']:
                temp = {'search': 'hunter'}
                temp["ip"] = arr['ip']
                temp["port"] = str(arr['port'])
                temp["host"] = arr['url']
                temp["title"] = arr['web_title'][:30]
                temp["protocol"] = arr['protocol']
                temp["base_protocol"] = arr['base_protocol']
                temp["update_time"] = arr['updated_at']
                temp["country"] = arr['country']
                temp["status_code"] = str(arr['status_code'])
                temp["org"] = arr['as_org']
                temp["region"] = arr['province']
                temp["city"] = arr['city']
                temp["isp"] = arr['isp']
                hunter_data.append(temp)
                if flag:
                    break
                # print(temp)
                # with open("../hunter返回的内容.txt", "w", encoding='utf-8') as f:
                #     f.write(str(hunter_data))
    except Exception as e:
        hunter_data=[]
    
    return hunter_data


if __name__ == "__main__":
    print(hunter_return("ip.city=Taipei", False))
