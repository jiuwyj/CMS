<script>  
import { onMounted,ref, computed,reactive,toRefs } from 'vue';  
import { ElPagination,ElInput } from 'element-plus';
import { useRoute ,useRouter } from 'vue-router'
import api from '@/api/index'
import { Search, View } from '@element-plus/icons-vue';
export default {  
    components: { ElPagination, ElInput, View },  
    props:{
        dataList:{
            type:Array,
            default:'',
        },
    },
    setup(props) {  
        const route = useRoute()
        const router = useRouter()
        const data = reactive({
            pageSize : 5, // 每页条目数  
            currentPage : 1, // 当前页码  
            totalItems : 10000, // 总条目数（示例中固定为50）
            dataList : toRefs(props).dataList,
            // banner:'GET / HTTP/1.1\n'+
            //         'Host: hackr.jp\n'+
            //         'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:13.0) Gecko/20100101 Firefox/13.0\n'+
            //         'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*; q=0.8\n'+
            //         'Accept-Language: ja,en-us;q=0.7,en;q=0.3\n'+
            //         'Accept-Encoding: gzip, deflate DNT: 1\n'+
            //         'Connection: keep-alive\n'+
            //         'If-Modified-Since: Fri, 31 Aug 2007 02:02:20 GMT\n'+
            //         'If-None-Match: "45bae1-16a-46d776ac"\n'+
            //         'Cache-Control: max-age=0\n'
        })
        const search_val=route.query.search_val;
        
        onMounted(()=>{
            // console.log(data.dataList)
        })
         
        const paginatedData = computed(() => {  // 根据当前页码和每页条目数计算要显示的数据列表
            let start = (data.currentPage - 1) * data.pageSize;
            let end = start + data.pageSize; 
            if(end > data.totalItems){
                end = data.totalItems;
            } 
            return data.dataList.slice(start, end);   
        });  
        const handleSizeChange = (newPageSize) => {  // 处理每页条目数改变事件 
            data.pageSize = newPageSize; // 更新每页条目数 
        };  
        const handleCurrentChange = (newPage) => {  // 处理当前页码改变事件
            data.currentPage = newPage; // 更新当前页码
        }; 
        
        const godetail = (thisip,thisport) => {  
            router.push({
                path: "/detail",
                query: {
                    ip : thisip,
                    port : thisport
                },
            });
        };   

        return { 
            ...toRefs(data),godetail,search_val, paginatedData, handleSizeChange, handleCurrentChange 
        }; // 返回变量和方法供模板使用  
    },  
};  
</script>

<template>
    <div v-for="(item, index) in paginatedData" :key="index" class="onedata">
        <div class="ip" style="display: flex;">
            <!-- <el-button @click="godetail(item.ip,item.port)" color="#03A9F4" circle>
                <Search style="width: 1em; height: 1em;"></Search>
            </el-button> -->
            <div style="padding-left: 10px;padding-top: 15px">
                <img style="height: 30px;" src="@/assets/搜索.svg" @click="godetail(item.ip,item.port)">
            </div>
            <h3>{{ item.ip + ' ' }}</h3>
        </div>
        <div class="data">
            <div class="fivedata">
                <el-descriptions :column = "2">
                    <el-descriptions-item label="Port">{{ item.port }}</el-descriptions-item>
                    <el-descriptions-item label="City">{{ item.city }}</el-descriptions-item>
                    <el-descriptions-item label="Country">{{ item.country }}</el-descriptions-item>
                    <el-descriptions-item label="Procotcl">
                    <el-tag size="small">{{ item.protocol }}</el-tag>
                    </el-descriptions-item>  
                </el-descriptions>
            </div>
            <div class="banner">
                <div style="font-size: 20px;color:rgba(0, 0, 0, 0.75);
                font-weight: 600;background: #f7f7fc;padding: 10px;">Banner</div>
                <div v-text="item.banner" class="text"></div>
            </div>
        </div>
    </div>  
    <el-pagination  
    @size-change="handleSizeChange"  
    @current-change="handleCurrentChange"  
    :current-page="currentPage"  
    :page-sizes="[5, 10, 15]"  
    :page-size="pageSize"  
    layout="total, sizes, prev, pager, next, jumper"  
    :total="dataList.length"  
    ></el-pagination>
</template>

<style scoped>
    h3 {  
        display: inline-block; 
        padding-left: 10px; 
    }  
    el-descriptions {
        background: #fcfcfc;
    }
    .ip{
        width: 100%;
    }
    .data{
        display: flex;
    }
    .onedata{
        /* display: flex;  */
        border: 2px solid #f5f6fb;  
        /* background: #ffffff; */
        border-radius: 10px 10px 10px 10px;
        margin-bottom: 20px;
        padding-left: 10px;
        height: 276px;
    }
    .fivedata{
        width:40%;
    }
    .banner{
        width:50%;
        /* height: 200px; */
        border-radius: 10px 10px 10px 10px;
        padding-left: 10px;
        /* background: #f7f7fc; */
    }
    .text{
        color: rgba(0, 0, 0, 0.5);
        height: 130px;
        overflow: auto;
        white-space: pre-wrap; /* 保持文本换行，可选，根据需要添加 */
        background: #f7f7fc;
        padding: 10px;
    }
</style>