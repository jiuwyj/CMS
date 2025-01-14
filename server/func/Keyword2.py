#对应引擎:FOFA,Hunter,360Quake,Shodan,ZoomEye
kword = {
    1: ['domain=', 'domain=', 'domain:', ' ', ' '],
    3: ['ip=', 'ip=', 'ip:', 'ip:', 'ip:'],
    5: ['icp=', 'icp.number=', ' ', ' ', ' '],
    7: [' ', 'icp.name=', ' ', ' ', ' '],
    8: [' ', 'icp.type=', ' ', ' ', ' '],
    9: [' ', 'icp.web_name=', ' ', ' ', ' '],
    11: [' ', 'ip.isp=', 'isp=', 'isp:', 'isp:'],
    12: ['is_ipv6=', ' ', 'is_ipv6=', 'has_ipv6:', ' '],
    13: ['region=', ' ', ' ', 'region:', 'subdivisions:'],
    14: ['host=', ' ', ' ', 'hostname:', 'hostname:'],
    16: ['org=', 'as.org=', 'org:', 'org:', 'org:'],
    17: ['os=', 'ip.os=', 'os:', 'os:', 'os:'],
    18: ['fid=', ' ', ' ', 'ssl.cert.fingerprint=', 'ssl.cert.fingerprint:'],#修改2024/4/5
    21: ['asn=', 'as.number=', 'asn:', 'asn:', 'asn:'],
    22: [' ', 'as.name=', ' ', ' ', ' '],
    24: ['port=', 'ip.port=', 'port:', 'port:', 'port:'],
    27: ['protocol=', 'protocol=', ' ', ' ', 'service:'],
    28: [' ', 'ip.province=', 'province=', ' ', ' '],#修改2024/4/5
    30: ['city=', 'ip.city=', 'city:', 'city:', 'city:'],#quake语法问题已修改
    31: ['country=', 'ip.country=', 'country:', 'country:', 'country:'],
    36: ['cert=', 'cert=', 'cert:', 'ssl:', 'ssl:'],
    37: ['cert.issuer=', 'cert.issuer=', ' ', 'ssl.cert.issuer.cn:', 'ssl.cert.issuer.cn:'],
    39: [' ', 'cert.serial_number=', ' ', 'ssl.cert.serial:', 'ssl.cert.serial:'],
    40: ['cert.subject=', 'cert.subject=', ' ', 'ssl.cert.subject.cn:', 'ssl.cert.subject.cn:'],
    41: ['cloud_name=', ' ', ' ', 'cloud.provider:', ' '],
    42: ['status_code=', 'header.status_code=', ' ', 'http.status:', ' '],
    44: ['title=', 'web.title=', ' ', 'http.title:', 'title:'],#修改2024/4/5
    45: ['base_protocol=', 'protocol.transport=', 'transport=', ' ', ' '],
    49: ['js_md5=', ' ', ' ', ' ', ' '],
    50: ['js_name=', ' ', ' ', ' ', ' ']
}
