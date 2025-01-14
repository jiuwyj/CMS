"""
email 和 apikey 会过期，账户可能无效
"""
# -*- coding: utf-8 -*-
from pythonfofa import Client

fofa_email = '2016260114@lut.edu.cn'
fofa_apikey = 'M8PMcemmd5L8BuAq'
fields = ['ip', 'port', 'protocol', 'country_name', 'region', 'city', 'latitude', 'longitude',
          'as_number', 'as_organization', 'host', 'domain', 'os', 'server', 'icp',
          'title', 'jarm', 'header', 'banner', 'cert', 'base_protocol', 'link', 'certs_issuer_org',
          'certs_issuer_cn', 'certs_subject_org', 'certs_subject_cn', 'tls_ja3s', 'tls_version',
          'product', 'product_category', 'version', 'lastupdatetime', 'cname']


def mapping(one_item):
    item = {
        'search': 'fofa',
        'ip': one_item[0],
        'port': str(one_item[1]),
        'protocol': str(one_item[2]),
        'country': one_item[3],
        'region': one_item[4],
        'city': one_item[5],
        'latitude': str(one_item[6]),
        'longitude': str(one_item[7]),
        'asn': one_item[8],
        'org': one_item[9],
        'host': one_item[10],
        'domain': one_item[11],
        'os': one_item[12],
        'server': one_item[13],
        'icp': one_item[14],
        'title': one_item[15],
        'jarm': one_item[16],
        'header': one_item[17],
        'banner': one_item[18],
        'cert': one_item[19],
        'base_protocol': one_item[20],
        'link': one_item[21],
        'certs_issuer_org': one_item[22],
        'certs_issuer_cn': one_item[23],
        'certs_subject_org': one_item[24],
        'certs_subject_cn': one_item[25],
        'ja3s': one_item[26],
        'tls_version': one_item[27],
        'product': one_item[28],
        'product_category': one_item[29],
        'version': one_item[30],
        'update_time': one_item[31],
        'cname': one_item[32]
    }
    return item


def fofa_return(query, flag=False):
    client = Client(fofa_email, fofa_apikey)
    response = client.search(query, fields, page=1, size=10)
    results = []
    if flag is False:
        total = response['size']
        print("fofa", total)
        results.append({'fofa_total': total})

    if response['error'] is True:
        print("ERROR", response['errmsg'])
    else:
        # print(response)
        # with open("fofa返回数据.txt", "w", encoding="gbk") as f:
        for item in response['results']:
            tmp = mapping(item)
            results.append(tmp)
            if flag:
                break
                # f.write(str(tmp)+"\r")
                # print(tmp)
    return results


if __name__ == "__main__":
    search = 'city="taipei"'
    data = fofa_return(search)
    print(data)
