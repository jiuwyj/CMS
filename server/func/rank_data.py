from pythonfofa import Client

fofa_email = '2087946138@qq.com'
fofa_apikey = 'M8PMcemmd5L8BuAq'


def get_rank_data(query, field=None):
    query_list = query.split('=')
    fofa_search = query_list[0]+'=\"'+query_list[1]+'\"'
    if field is None:
        field = ['protocol', 'server', 'port', 'country']
    client = Client(fofa_email, fofa_apikey)
    response = client.search_stats(fofa_search, field=field)
    if response['error'] is False:
        try:
            result = save_rank_dic(response['aggs'])
            return result
        except Exception as e:
            print(e)
    else:
        print("ERROR!")


def save_rank_dic(msg):
    result = {}
    field_except_c = ['protocol', 'server', 'port']
    for item in field_except_c:
        if item in msg:
            result[item] = msg[item]
    if 'countries' in msg:
        result['country'] = []
        for country in msg['countries']:
            result['country'].append({'name': country['name'], 'count': country['count']})

    return result


if __name__ == "__main__":
    # search = 'city="Taipei"'
    search = 'port=443'
    ans = get_rank_data(search)
    print(ans)
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
