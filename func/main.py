# -*- coding: utf-8 -*-
from . import keyword_together2
from .Keyword2 import kword
import re
from . import zhtoen
from .Simplify_data import simplify_data
from .Simplify_data import process_data_page_3
from .Simplify_data import process_data_for_rank
from .number_in_areas import areas_count
from .data_for_page4 import process_data_for_page4
from .Multi_threading import multi_thread_get
from .rank_data import get_rank_data
from .truth_for_website import truth_for_website
from .data_for_page4 import process_data_for_page4
import copy
import random

num = 0
search_choose_list = []
new_value = None
old_value = None
init_item = {  # 格式化后每一条数据的样式
    'search': '',
    'ip': '',
    'port': '',
    'protocol': '',
    'country': '',
    'region': '',
    'city': '',
    'latitude': '',
    'longitude': '',
    'asn': '',
    'org': '',
    'host': '',
    'domain': '',
    'os': '',
    'server': '',
    'icp': '',
    'title': '',
    'jarm': '',
    'header': '',
    'banner': '',
    'cert': '',
    'base_protocol': '',
    'link': '',
    'certs_issuer_org': '',
    'certs_issuer_cn': '',
    'certs_subject_org': '',
    'certs_subject_cn': '',
    'ja3s': '',
    'tls_version': '',
    'product': '',
    'product_category': '',
    'version': '',
    'update_time': '',
    'cname': '',
    'status_code': '',
    'isp': '',
    'is_ipv6': '',
    'mac': '',
    'cpe': '',
    'cpe23': '',
    'crawler': '',
    'fingerprint': '',
    'chain': '',
    'vulns': '',
    'app': '',
    'device': '',
    'is_risk': '',
    'url': '',
    'is_risk_protocol': '',
    'component': '',
    'is_web': '',
    'service_response': '',
    'scene_en': '',
    'organization': ''
}


def is_chinese(string):
    """
    判断字符串是否为中文
    """
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    result = pattern.search(string)

    return result is not None


def start_search(query, flag):  # 在五个引擎获取数据的函数

    engine_input = {}
    if not flag:
        if search_choose_list[0] != ' ':  # fofa
            fofa_input = search_choose_list[0] + '\"' + new_value + '\"'
            print("fofa-->" + fofa_input)
            engine_input["fofa"] = fofa_input

        if search_choose_list[1] != ' ':  # hunter
            hunter_input = search_choose_list[1] + '\"' + new_value + '\"'
            if old_value is not None:
                hunter_input = search_choose_list[1] + '\"' + old_value + '\"'
            print("hunter-->" + hunter_input)
            engine_input["hunter"] = hunter_input

        if search_choose_list[2] != ' ':  # quake
            quake_input = search_choose_list[2] + '\"' + new_value + '\"'
            print("quake-->" + quake_input)
            engine_input["quake"] = quake_input

        if search_choose_list[3] != ' ':  # shodan
            shodan_input = search_choose_list[3] + '\"' + new_value + '\"'
            print("shodan-->" + shodan_input)
            engine_input['shodan'] = shodan_input

        if search_choose_list[4] != ' ':  # zoomeye
            zoomeye_input = search_choose_list[4] + '\"' + new_value + '\"'
            print("zoomeye-->" + zoomeye_input)
            engine_input['zoomeye'] = zoomeye_input
    else:
        split_list = query.split("=")
        ip_value = split_list[1].split(" ")[0]

        fofa_input = split_list[0] + '=\"' + ip_value + '\" && port=\"' + split_list[2] + '\"'
        print("fofa-->" + fofa_input)
        engine_input["fofa"] = fofa_input

        # hunter_input = split_list[0] + '=\"' + ip_value + '\" && port=\"' + split_list[2] + '\"'
        # print("hunter-->" + hunter_input)
        # engine_input["hunter"] = hunter_input

        quake_input = split_list[0] + ':\"' + ip_value + '\" and port:\"' + split_list[2] + '\"'
        print("quake-->" + quake_input)
        engine_input["quake"] = quake_input

        shodan_input = split_list[0] + ':\"' + ip_value + '\" port:' + split_list[2]
        print("shodan-->" + shodan_input)
        engine_input['shodan'] = shodan_input

        zoomeye_input = split_list[0] + ':\"' + ip_value + '\" +port:\"' + split_list[2] + '\"'
        print("zoomeye-->" + zoomeye_input)
        engine_input['zoomeye'] = zoomeye_input

    result_all = multi_thread_get(engine_input, flag)  # 多线程获取数据
    return result_all


def get_ct():
    datafrom = [
        {"value": random.randint(1, 4), "name": 'Quake'},
        {"value": random.randint(3, 6), "name": 'Shodan'},
        {"value": random.randint(2, 5), "name": 'Zoomeye'},
        {"value": random.randint(25, 33), "name": 'FOFA'},
        {"value": random.randint(8, 11), "name": 'Hunter'}
    ],
    return datafrom


def get_result(query):
    print(query)
    grammar_message = return_grammar_out(query)
    if grammar_message['validity'] == 'No':
        # print('无错误')
        flag = False
        if ('and' or 'AND') in query:
            # print('多重搜索')
            flag = True
        return start_search(query, flag)
    return []


def formatting(list_init):  # 对每一条数据补充使之都为init_item格式
    for item in list_init:
        for key in init_item:
            if key not in item:
                item[key] = ' '
            if item[key] == '':
                item[key] = ' '
            if not (type(item[key]) is str):
                item[key] = str(item[key])
    return list_init


def check_grammar(key, value):
    value_return = (value, None)
    try:
        if is_chinese(value):
            value_return = (zhtoen.tanslate(value), value)
    except IndexError:
        return None, value_return

    try:
        tmp = kword.get(key)[0]
        return kword[key], value_return
    except TypeError:
        return None, value_return


def return_grammar_out(query):
    """
    检查搜索语句的语法，并返回相关信息
    仅检测但搜索语句语法
    :param query:
    :return:
    """
    global search_choose_list, new_value, old_value, num
    try:
        value_list = query.split('=')
        front = value_list[0]
        after = value_list[1]
        # print("---拆分----")
        if len(value_list) == 3:  # 多重搜索
            # print("属于多重搜索")
            if value_list[0] == 'ip' and ((' and port' or ' AND port') in value_list[1]) and str.isdigit(
                    value_list[2]) is True:
                # print('多重搜索正常进行')
                return {'validity': 'No', 'error': ''}
            else:
                # print('多重搜索语句语法错误')
                return {'validity': 'Yes', 'error': '多重搜索语法错误或者可能不支持该语法'}
        elif len(value_list) == 2:
            # print('单条件搜索语法检测')
            num = int(keyword_together2.search_symbol(front))
            search_choose_list, (new_value, old_value) = check_grammar(num, after)
            # print(search_choose_list, new_value, old_value)
            if type(search_choose_list) is not list:
                # print('error')
                return {'validity': 'Yes', 'error': search_choose_list}
                # return {'validity': 'Yes', 'error': 'search_choose_list'}
            else:
                # print('continue')
                return {'validity': 'No', 'error': ''}
        else:
            # print('不存在该种语法')
            return {'validity': 'Yes', 'error': '不存在该搜索语句，请再检查'}
    except Exception as e:
        # return {'validity': 'Yes', 'error': e}
        return {'validity': 'Yes', 'error': '不存在该搜索语句，请再检查'}


def together(list_init, truth_dict=None):
    if truth_dict is None:
        truth_dict = truth_for_website()
    list_together = []
    sorted_list = sorted(list_init, key=lambda x: (x['ip'], x['port'], x['search']))
    left = 0
    while left < len(sorted_list):
        right = left + 1
        item = sorted_list[left]
        go_flag = 0
        while right < len(sorted_list):
            while right < len(sorted_list) and item['ip'] == sorted_list[right]['ip'] and item['port'] == \
                    sorted_list[right]['port']:
                go_flag = 1
                for key in item:  # 聚合
                    if sorted_list[right][key] != ' ' and (
                            item[key] == ' ' or truth_dict[item['search']] < truth_dict[sorted_list[right]['search']]):
                        item[key] = sorted_list[right][key]
                right += 1
            if go_flag == 1:
                break
            else:
                right += 1
        if go_flag == 1:
            left = right
        else:
            left += 1
        list_together.append(item)
    return list_together


def search_all_detail(query):
    result_from_5 = get_result(query)
    result_from_5['data'] = formatting(result_from_5['data'])
    if 'count' not in result_from_5:  # 页面三
        page3_data = result_from_5
        return page3_data
    else:  # 页面二
        result_from_5['data'] = together(result_from_5['data'], truth_for_website())
        page2_data = result_from_5
        return page2_data


def search_ip_detail(query):
    return search_all_detail(query)[0]


def cal_detail_truth(data, truth_dict):
    value = 0
    count = len(init_item) - 1
    for key in init_item:
        if key != "search":
            max_truth = 0
            for item in data:
                if item[key] != ' ' and truth_dict[item['search']] > max_truth:
                    max_truth = truth_dict[item['search']]
            if max_truth == 0:
                max_truth = 1
            value += max_truth
    return value / count


def get_page2_data(query):  # 页面二的返回
    page2_data = search_all_detail(query)
    page2_data['data'] = simplify_data(page2_data['data'])
    # page2_data = dict()
    page2_data['rank'] = process_data_for_rank(get_rank_data(query))
    page2_data['truth'] = truth_for_website()
    page2_data['areas_number'] = areas_count(page2_data['data'])
    return page2_data


def get_page3_data(query):  # 页面三的返回
    page3_data = search_all_detail(query)
    page3_data['data'] = process_data_page_3(page3_data['data'])
    copy_data = copy.deepcopy(page3_data['data'])
    page3_data['truth_sum'] = cal_detail_truth(page3_data['data'], truth_for_website())
    page3_data['data'] = together(page3_data['data'])[0]
    page3_data['tree'] = process_data_for_page4(copy_data)
    page3_data["datafrom"] = get_ct()

    return page3_data


def search_geo_message(query):  # 返回地点数量信息
    all_data = areas_count(query)
    # print(all_data)
    return all_data


def search_ip_tree_detail(query):
    result_from_5 = get_result(query)
    formatted_list = formatting(result_from_5)
    return process_data_for_page4(formatted_list)


if __name__ == "__main__":
    # 提示用户输入查询条件
    print("请输入查询条件（例如：city=Taipei 或 ip=101.3.121.197 and port=1025）：")
    user_input = input("查询条件：")

    # 检查用户输入是否为空
    if not user_input:
        print("未输入查询条件，程序结束。")
    else:
        # 页面 2 数据（简化数据展示）
        print("\n正在获取页面 2 数据...\n")
        page_2_data = get_page2_data(user_input)
        print("页面 2 数据：", page_2_data)

        # 页面 3 数据（完整数据展示）
        print("\n正在获取页面 3 数据...\n")
        page_3_data = get_page3_data(user_input)
        print("页面 3 数据：", page_3_data)

        # 输出汇总的可信度
        print("\n页面 3 汇总可信度：", page_3_data['truth_sum'])
