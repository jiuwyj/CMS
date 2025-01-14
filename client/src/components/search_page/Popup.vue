<template>
    <div v-if="visible" class="popup">
        <!-- 弹窗的内容 -->
        <div class="popup-content">
            <el-table :data="tableData" style="width: 700px" height="500">
                <el-table-column prop="rule" label="语法规则" width="180" />
                <el-table-column prop="example" label="搜索示例" width="180" />
                <el-table-column prop="explain" label="解释" />
            </el-table>
        </div>
        <!-- 关闭按钮 -->
        <img src="@/assets/关闭.svg" @click="closePopup" alt="">
        <!-- <button class="close-button" @click="closePopup">关闭</button> -->
    </div>
</template>
 
<script>
export default {
    props: {
        visible: {
            type: Boolean,
            default: false
        },
        content: {
            type: String,
            default: ''
        }
    },
    data() {
        return {
            tableData : [
                {
                    rule: 'ip',
                    example: 'ip=1.1.1.1',
                    explain: 'No. 189, Grove St, Los Angeles',
                },
                {
                    rule: 'os',
                    example: 'os=Windows',
                    explain: '搜索操作系统为“Windows”的网络资产',
                },
                {
                    rule: 'fid',
                    example: 'fid=sSXXGNUO2FefBTcCLIT/2Q==',
                    explain: '搜索网站指纹“sSXXGNUO2FefBTcCLIT/2Q==”的网络资产',
                },
                {
                    rule: 'icp',
                    example: 'icp=京ICP证030173号',
                    explain: '搜索备案号为“京ICP证030173号”的网络资产',
                },
                {
                    rule: 'asn',
                    example: 'asn=19551',
                    explain: '搜索自治系统号为“19551”的网络资产',
                },
                {
                    rule: 'org',
                    example: 'org=PDR',
                    explain: '搜索所属组织为PDR的网络资产',
                },
                {
                    rule: 'isp',
                    example: 'isp=China Mobile',
                    explain: '搜索网络服务提供商为”China Mobile”网络的资产',
                },
                {
                    rule: 'port',
                    example: 'port=6379',
                    explain: '搜索端口为“6379”的网络资产',
                },
                {
                    rule: 'city',
                    example: 'city=Taipei',
                    explain: '搜索城市为台北的网络资产',
                },
                {
                    rule: 'title',
                    example: 'title=login',
                    explain: '搜索标题为“login”的网络资产',
                },
                {
                    rule: 'domain',
                    example: 'domain=qq.com',
                    explain: '搜索根域名带有qq.com的网络资产',
                },
                {
                    rule: 'js_md5',
                    example: 'js_md5=82ac3f14327a8b7ba49baa208d4eaa15',
                    explain: '搜索js源码为"82ac3f14327a8b7ba49baa208d4eaa15"的网络资产',
                },
                {
                    rule: 'region',
                    example: 'region=Beijing',
                    explain: '搜索行政区为“北京”的资产。',
                },
                {
                    rule: 'js_name',
                    example: 'js_name=js/jquery.js',
                    explain: '搜索网站正文中包含js/jquery.js的网络资产',
                },
                {
                    rule: 'country',
                    example: 'country=China',
                    explain: '搜索国家为“China”的网络资产',
                },
                {
                    rule: 'is_ipv6',
                    example: 'is_ipv6=true',
                    explain: '搜索ipv6的资产',
                },
                {
                    rule: 'icp.name',
                    example: 'icp.name=奇安信',
                    explain: '搜索ICP备案单位名中含有“奇安信”的网络资产',
                },
                {
                    rule: 'icp.type',
                    example: 'icp.type=企业',
                    explain: '搜索ICP备案主体为“企业”的网络资产',
                },
                {
                    rule: 'asn_name',
                    example: 'asn_name=CLOUDFLARENET',
                    explain: '搜索asn名称为CLOUDFLARENET的网络资产',
                },
                {
                    rule: 'hostname',
                    example: 'hostname=.gov.cn',
                    explain: '搜索url中包含”.gov.cn”的网络资产',
                },
                {
                    rule: 'protocol',
                    example: ' protocol=quic',
                    explain: '搜索协议名称为“quic”',
                },
                {
                    rule: 'province',
                    example: 'province=Hunan',
                    explain: '搜索省份为“Hunan”的资产',
                },
                {
                    rule: 'cert_name',
                    example: 'cert_name=baidu',
                    explain: '搜索证书(https或者imaps等)中带有baidu的网络资产',
                },
                {
                    rule: 'cloud_name',
                    example: 'cloud_name=Aliyundun',
                    explain: '通过云服务名称为"Aliyundun"的网络资产',
                },
                {
                    rule: 'cert_issuer',
                    example: 'cert_issuer=DigiCert',
                    explain: '搜索证书颁发者为"DigiCert"的网络资产',
                },
                {
                    rule: 'icp.web_name',
                    example: 'icp.web_name=奇安信',
                    explain: '搜索ICP备案网站名中含有“奇安信”的网络资产',
                },
                {
                    rule: 'status_code ',
                    example: 'status_code=402',
                    explain: '搜索服务器状态为“402”的资产',
                },
                {
                    rule: 'cert_subject',
                    example: 'cert.subject.cn=baidu.com',
                    explain: '搜索证书持有者通用名称为“baidu.com”的网络资产',
                },
                {
                    rule: 'trans_protocol',
                    example: 'trans_protocol=udp',
                    explain: '搜索传输层协议为“udp”的网络资产',
                },
                {
                    rule: 'cert_serial',
                    example: 'cert_serial=18460192207935675900910674501',
                    explain: '搜索证书序列号为18460192207935675900910674501的资产',
                },
            ]
        }
    },
    methods: {
        closePopup() {
            this.$emit('close');
        }
    }
}
</script>
 
<style scoped>
.popup {
    position: fixed;
    z-index: 8000;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

.popup-content {
    background: #f5f6fb;
    padding: 20px;
    border-radius: 5px;
}

.close-button {
    margin-top: 10px;
}
</style>