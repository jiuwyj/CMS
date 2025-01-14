# -*- coding: utf-8 -*-
"""
为树状图(页面4)进行数据处理
输入数据：页面三搜索返回的数据
输入的数据格式为
[
{"search":"fofa","ip":"127.0.0.1","port":"443","country":"China"},
{"search":"shodan","ip":"127.0.0.1","port":"443","country":"China"},
{"search":"hunter","ip":"127.0.0.1","port":"443","country":"China"},
{"search":"quake","ip":"127.0.0.1","port":"443","country":"China"},
{"search":"zoomeye","ip":"127.0.0.1","port":"443","country":"China"},
]
返回的数据格式：
 {"name":"127.0.1.1+443","children":[{"name":"city","childen":[{"name":"fofa","value":"Taipei"},{"name":"hunter","value":"Taipei"},{"name":"zoomeye","value":"Taipei"},{"name":"shodan","value":"Taipei"},{"name":"quake","value":"Taipei"}]}}
 Time:2024/4/6
"""
import copy


def process_data_for_page4(data_list):
    DATA=copy.deepcopy(data_list)
    fofa_data = {}
    quake_data = {}
    shodan_data = {}
    hunter_data = {}
    zoomeye_data = {}
    tree = {'name': DATA[0]['ip'] + ":" + DATA[0]['port']}  # 返回的内容

    data = {  # 格式化后每一条数据的样式
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
        'is_ipv6': ''
    }

    if len(DATA) != 5:  # 存在有的引擎不存在数据的情况,填充使data_list包含五个引擎

        engine = {"fofa": 0, "shodan": 0, "quake": 0, "zoomeye": 0, "hunter": 0}
        for item in DATA:
            engine[item["search"]] += 1
        for i in engine:
            if engine[i] == 0:  # 对data_list进行数据填充
                tree[i]=''
                DATA.append({"search": i})
                print(i + '数据为空')
            else:
                tree[i]=DATA[0]['ip'] + ":" + DATA[0]['port']
    else:
        engine = {"fofa": 0, "shodan": 0, "quake": 0, "zoomeye": 0, "hunter": 0}
        for i in engine:
            tree[i]=DATA[0]['ip'] + ":" + DATA[0]['port']

    tree['children']=[]


    for item in DATA:
        if item["search"] == 'fofa':
            fofa_data = item
            continue
        elif item["search"] == 'quake':
            quake_data = item
            continue
        elif item["search"] == 'shodan':
            shodan_data = item
            continue
        elif item["search"] == 'hunter':
            hunter_data = item
            continue
        else:
            zoomeye_data = item

    for key in data:
        t = {'name': key,}
        t['fofa']=fofa_data.get(key, " ")
        t['hunter']=hunter_data.get(key, " ")
        t['shodan']=shodan_data.get(key, " ")
        t['zoomeye']=zoomeye_data.get(key, " ")
        t['quake']=quake_data.get(key, " ")
        # t['children'].append({'name': 'fofa', 'value': fofa_data.get(key, " ")})
        # t['children'].append({'name': 'hunter', 'value': hunter_data.get(key, " ")})
        # t['children'].append({'name': 'zoomeye', 'value': zoomeye_data.get(key, " ")})
        # t['children'].append({'name': 'shodan', 'value': shodan_data.get(key, " ")})
        # t['children'].append({'name': 'quake', 'value': quake_data.get(key, " ")})
        tree['children'].append(t)

    # for i in tree:
    #     print(i)
    return tree


if __name__ == "__main__":
    a = [{"search": "fofa", "ip": "172.0.0.1", "port": "443", 'country': 'China', 'region': 'na', 'city': 'Taipei',
          'latitude': '25.04776', 'longitude': '121.53185', 'asn': 'AS4782', 'org': 'Government Service Network (GSN)',
          'host': '', 'domain': 'hinet.net', 'os': None, 'product': '', 'update_time': '2024-01-12T01:06:24.861435',
          'base_protocol': 'tcp', 'isp': 'Data Communication Business Group', 'area_code': None, 'hash': -940471364,
          'protocol': '', 'server': '', 'icp': '', 'title': '', 'jarm': '', 'header': '', 'banner': '', 'cert': '',
          'link': '', 'certs_issuer_org': '', 'certs_issuer_cn': '', 'certs_subject_org': '', 'certs_subject_cn': '',
          'ja3s': '', 'tls_version': '', 'product_category': '', 'version': '', 'cname': '', 'status_code': '',
          'is_ipv6': ''}]
    data_list = [
        {"search": "fofa", "ip": "172.0.0.1", "port": "443", 'country': 'China', 'region': 'na', 'city': 'Taipei',
         'latitude': '25.04776', 'longitude': '121.53185', 'asn': 'AS4782', 'org': 'Government Service Network (GSN)',
         'host': '', 'domain': 'hinet.net', 'os': None, 'product': '', 'update_time': '2024-01-12T01:06:24.861435',
         'base_protocol': 'tcp', 'isp': 'Data Communication Business Group', 'area_code': None, 'hash': -940471364,
         'protocol': '', 'server': '', 'icp': '', 'title': '', 'jarm': '', 'header': '', 'banner': '', 'cert': '',
         'link': '', 'certs_issuer_org': '', 'certs_issuer_cn': '', 'certs_subject_org': '', 'certs_subject_cn': '',
         'ja3s': '', 'tls_version': '', 'product_category': '', 'version': '', 'cname': '', 'status_code': '',
         'is_ipv6': ''},
        {"search": "quake", "ip": "172.0.0.1", "port": "443", 'country': 'China', 'region': 'eu', 'city': 'Taipei',
         'latitude': '25.04776', 'longitude': '121.53185', 'asn': 'AS55303', 'org': 'Netwiz Private Limited',
         'host': None, 'domain': None, 'os': None, 'product': None, 'update_time': '2024-01-12T00:50:44.281383',
         'base_protocol': 'tcp', 'isp': '60 Market Square,P.O. Box 364', 'area_code': None, 'hash': 0, 'protocol': '',
         'server': '', 'icp': '', 'title': '', 'jarm': '', 'header': '', 'banner': '', 'cert': '', 'link': '',
         'certs_issuer_org': '', 'certs_issuer_cn': '', 'certs_subject_org': '', 'certs_subject_cn': '', 'ja3s': '',
         'tls_version': '', 'product_category': '', 'version': '', 'cname': '', 'status_code': '', 'is_ipv6': ''},
        {"search": "shodan", "ip": "172.0.0.1", "port": "443", 'protocol': 'dahua-dvr', 'country': 'China',
         'city': 'Taipei City', 'server': 'Dahua DVR', 'version': '', 'product': '', 'asn': "",
         'update_time': '2024-01-12T08:53:20', 'region': '', 'latitude': '', 'longitude': '', 'org': '', 'host': '',
         'domain': '', 'os': '', 'icp': '', 'title': '', 'jarm': '', 'header': '', 'banner': '', 'cert': '',
         'base_protocol': '', 'link': '', 'certs_issuer_org': '', 'certs_issuer_cn': '', 'certs_subject_org': '',
         'certs_subject_cn': '', 'ja3s': '', 'tls_version': '', 'product_category': '', 'cname': '', 'status_code': '',
         'isp': '', 'is_ipv6': ''},
        {"search": "zoomeye", "ip": "172.0.0.1", "port": "443", 'country': 'China', 'region': 'eu', 'city': 'Taipei',
         'latitude': '25.04776', 'longitude': '121.53185', 'asn': 'AS3462', 'org': 'Chunghwa Telecom Co.,Ltd.',
         'host': '', 'domain': 'hinet.net', 'os': 'Mac OS X', 'product': 'Apple remote desktop vnc',
         'update_time': '2024-01-12T01:06:15.886849', 'base_protocol': 'tcp',
         'isp': 'Data Communication Business Group', 'area_code': "", 'hash': 2117757202, 'protocol': '', 'server': '',
         'icp': '', 'title': '', 'jarm': '', 'header': '', 'banner': '', 'cert': '', 'link': '', 'certs_issuer_org': '',
         'certs_issuer_cn': '', 'certs_subject_org': '', 'certs_subject_cn': '', 'ja3s': '', 'tls_version': '',
         'product_category': '', 'version': '', 'cname': '', 'status_code': '', 'is_ipv6': ''},
        {'search': 'hunter', "ip": "172.0.0.1", "port": "443", 'transport': 'tcp', 'asn': '984',
         'update_time': '2024-01-12', 'org': 'OCTOPUS WEB SOLUTION INC', 'is_ipv6': 'False', 'title': '',
         'country': '中国', 'city_quake': 'Taipei', 'isp': 'OCTOPUS WEB SOLUTION INC', 'scene_en': 'Company',
         'host': '', 'protocol': 'http', 'status_code': '403', 'region': '', 'city': '', 'latitude': '',
         'longitude': '', 'domain': '', 'os': '', 'server': '', 'icp': '', 'jarm': '', 'header': '', 'banner': '',
         'cert': '', 'base_protocol': '', 'link': '', 'certs_issuer_org': '', 'certs_issuer_cn': '',
         'certs_subject_org': '', 'certs_subject_cn': '', 'ja3s': '', 'tls_version': '', 'product': '',
         'product_category': '', 'version': '', 'cname': ''}
    ]
    b = [{'search': 'fofa', 'ip': '1.1.1.1', 'port': '80', 'protocol': 'http', 'country': '', 'region': '', 'city': '',
          'latitude': '0.000000', 'longitude': '0.000000', 'asn': '13335', 'org': 'CLOUDFLARENET', 'url': '1.1.1.1',
          'domain': '', 'os': '', 'server': 'cloudflare', 'icp': '', 'title': '', 'jarm': '', 'header': '',
          'banner': 'HTTP/1.1 301 Moved Permanently\r\nServer: cloudflare\r\nDate: Thu, 11 Jan 2024 08:35:08 GMT\r\nContent-Type: text/html\r\nContent-Length: 167\r\nConnection: keep-alive\r\nLocation: https://1.1.1.1/\r\nCF-RAY: 843bd317e95610aa-HKG',
          'cert': '', 'base_protocol': 'tcp', 'link': 'http://1.1.1.1', 'certs_issuer_org': '', 'certs_issuer_cn': '',
          'certs_subject_org': '', 'certs_subject_cn': '', 'ja3s': '', 'tls_version': '', 'product': 'CLOUDFLARE-产品',
          'product_category': '网站安全监控系统', 'version': '', 'update_time': '2024-01-11 16:00:00', 'cname': '',
          'host': '', 'status_code': '', 'isp': '', 'is_ipv6': ''},
         {'search': 'hunter', 'ip': '1.1.1.1', 'port': '80', 'host': 'http://perfumebranddiscountoutlet.shop',
          'title': 'Angel', 'protocol': 'http', 'base_protocol': 'tcp', 'update_time': '2024-01-07',
          'country': '澳大利亚', 'status_code': '301', 'as_org': 'Cloudflare, Inc.', 'region': '', 'city': '',
          'isp': 'Cloudflare, Inc.', 'latitude': '', 'longitude': '', 'asn': '', 'org': '', 'domain': '', 'os': '',
          'server': '', 'icp': '', 'jarm': '', 'header': '', 'banner': '', 'cert': '', 'link': '',
          'certs_issuer_org': '', 'certs_issuer_cn': '', 'certs_subject_org': '', 'certs_subject_cn': '', 'ja3s': '',
          'tls_version': '', 'product': '', 'product_category': '', 'version': '', 'cname': '', 'is_ipv6': ''},
         {'search': 'quake', 'ip': '1.1.1.1', 'port': '80', 'transport': 'tcp', 'asn': '13335',
          'update_time': '2024-01-10', 'org': 'Cloudflare, Inc.', 'is_ipv6': 'False', 'title': '',
          'country': '澳大利亚', 'city': '', 'isp': 'Cloudflare, Inc.', 'scene_en': 'Used',
          'host': 'ns2.braspayment.com', 'protocol': 'http', 'status_code': '409', 'region': '', 'latitude': '',
          'longitude': '', 'domain': '', 'os': '', 'server': '', 'icp': '', 'jarm': '', 'header': '', 'banner': '',
          'cert': '', 'base_protocol': '', 'link': '', 'certs_issuer_org': '', 'certs_issuer_cn': '',
          'certs_subject_org': '', 'certs_subject_cn': '', 'ja3s': '', 'tls_version': '', 'product': '',
          'product_category': '', 'version': '', 'cname': ''},
         # {'search': 'shodan', 'ip': '1.1.1.1', 'port': '80', 'country': 'United States', 'region': 'na',
         #  'city': 'Los Angeles', 'latitude': '34.0522', 'longitude': '-118.2437', 'asn': 'AS13335',
         #  'org': 'APNIC and Cloudflare DNS Resolver project', 'host': 'seobi.com.au', 'domain': 'one.one', 'os': None,
         #  'product': 'CloudFlare', 'update_time': '2024-01-12T14:45:08.285556', 'base_protocol': 'tcp',
         #  'isp': 'Cloudflare, Inc.', 'area_code': None, 'hash': -891159449, 'protocol': '', 'server': '', 'icp': '',
         #  'title': '', 'jarm': '', 'header': '', 'banner': '', 'cert': '', 'link': '', 'certs_issuer_org': '',
         #  'certs_issuer_cn': '', 'certs_subject_org': '', 'certs_subject_cn': '', 'ja3s': '', 'tls_version': '',
         #  'product_category': '', 'version': '', 'cname': '', 'status_code': '', 'is_ipv6': ''},
         # {'search': 'zoomeye', 'ip': '1.1.1.1', 'port': '80', 'protocol': 'http', 'country': 'Australia', 'city': '',
         #  'server': 'Cloudflare http proxy', 'version': '', 'product': '', 'asn': None,
         #  'update_time': '2023-12-27T15:41:40', 'region': '', 'latitude': '', 'longitude': '', 'org': '', 'host': '',
         #  'domain': '', 'os': '', 'icp': '', 'title': '', 'jarm': '', 'header': '', 'banner': '', 'cert': '',
         #  'base_protocol': '', 'link': '', 'certs_issuer_org': '', 'certs_issuer_cn': '', 'certs_subject_org': '',
         #  'certs_subject_cn': '', 'ja3s': '', 'tls_version': '', 'product_category': '', 'cname': '', 'status_code': '',
         #  'isp': '', 'is_ipv6': ''}
         ]


    print(process_data_for_page4(b))
