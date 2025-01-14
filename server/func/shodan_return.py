import shodan.exception
from shodan import Shodan
import warnings

warnings.filterwarnings('ignore')
api_key = "SQJZniSw8bt7BORJt3uHOCG2IOdbkwTI"


def mapping(one_item):
    item = {'search': 'shodan'}
    try:
        item['ip'] = one_item['ip_str']
    except:
        item['ip'] = ""

    try:
        item['port'] = str(one_item['port'])
    except:
        item['port'] = ""

    try:
        item['country'] = one_item['location']['country_name']
    except:
        item['country'] = ""

    try:
        item['region'] = one_item['_shodan']['region']
    except:
        item['region'] = ""

    try:
        item['city'] = one_item['location']['city']
    except:
        item['city'] = ""

    try:
        item['latitude'] = str(one_item['location']['latitude'])
    except:
        item['latitude'] = ""

    try:
        item['longitude'] = str(one_item['location']['longitude'])
    except:
        item['longitude'] = ""

    try:
        item['asn'] = one_item['asn']
    except:
        item['asn'] = ""

    try:
        item['org'] = one_item['org']
    except:
        item['org'] = ""

    try:
        item['host'] = one_item['http']['host']
    except:
        item['host'] = ""

    try:
        item['domain'] = one_item['domains'][0]
    except:
        item['domain'] = ""

    try:
        item['os'] = one_item['os']
    except:
        item['os'] = ""

    try:
        item['product'] = one_item['product']
    except:
        item['product'] = ""

    try:
        item['update_time'] = one_item['timestamp']
    except:
        item['update_time'] = ""

    try:
        item['base_protocol'] = one_item['transport']
    except:
        item['base_protocol'] = ""

    try:
        item['isp'] = one_item['isp']
    except:
        item['isp'] = ""

    try:
        mac = one_item['mac']
        for key in mac:
            item['mac'] = key
            break
    except:
        item['mac'] = ""

    try:
        item['cpe'] = one_item['cpe'][0]
    except:
        item['cpe'] = ""

    try:
        item['cpe23'] = one_item['cpe23'][0]
    except:
        item['cpe23'] = ""

    try:
        item['crawler'] = one_item['_shodan']['crawler']
    except:
        item['crawler'] = ""

    try:
        item['fingerprint'] = one_item['ssl']['cert']['fingerprint']
    except:
        item['fingerprint'] = ""

    try:
        item['chain'] = one_item['ssl']['chain'][0]
    except:
        item['chain'] = ""

    try:
        vulns_d = one_item['vulns']
        value = ""
        for key in vulns_d:
            value += key + " "
        item['vulns'] = value
    except:
        item['vulns'] = ""

    # item = {
    # 'ip': one_item['ip_str'],
    # 'port': str(one_item['port']),
    # 'country': one_item['location']['country_name'],
    # 'region': one_item['_shodan']['region'],
    # 'city': one_item['location']['city'],
    # 'latitude': str(one_item['location']['latitude']),
    # 'longitude': str(one_item['location']['longitude']),
    # 'asn': one_item['asn'],
    # 'org': one_item['org'],
    # 'host': one_item['http']['host'],
    # 'domain': one_item['domains'][0],
    # 'os': one_item['os'],
    # 'product': one_item['product'],
    # 'lastupdatetime': one_item['timestamp'],
    # 'transport': one_item['transport'],
    # 'isp': one_item['isp'],
    # 'area_code': one_item['location']['area_code'],
    # 'hash': one_item['hash']
    # }
    return item


def shodan_return(query, flag=False):
    try:
        results = []
        client = Shodan(api_key)
        ret = client.search(query=query, page=1, limit=10)
        # print(ret)
        if flag is False:
            total = ret['total']
            print("shodan", total)
            results.append({'shodan_total': total})

        for item in ret['matches']:
            # print(item)
            tmp = mapping(item)
            for key in tmp:
                if tmp[key] is None:
                    tmp[key] = ' '
                if type(tmp[key]) is int:
                    tmp[key] = str(tmp[key])
            results.append(tmp)
            if flag:
                break
                # f.write(str(tmp) + "\r")
    except Exception as e:
        print(e)
        results = []
    return results


if __name__ == "__main__":
    search = 'ip:"101.3.121.197" port:1025'
    data = shodan_return(search)
    print(data)
