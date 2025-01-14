<template>
    <div class="content_all">
        <div class="content_buttons">
            <el-button type="info" class="content_button" @click="gotree(detail_data)" plain>数据展示</el-button>
            <el-button type="info" class="content_button" @click="goother(detail_data)" plain>数据详情</el-button>           
        </div>
        <div class="content_box">
            <router-view/>
        </div>
    </div>
</template>

<script>
import { toRefs, watch } from 'vue'; 
import { useRouter } from 'vue-router' 
export default {
    name: 'content_url',
    props:{
        detail_data:{
            type:Object,
            default:{},
        },
    },
    setup(props){
        const router = useRouter()
        const detail_data = toRefs(props).detail_data
        const goother = (thisdata) => {  
            const params = JSON.stringify(thisdata)
            router.push({
                name: "otherdetail",
                query: {
                    ip : thisdata.data.ip,
                    port : thisdata.data.port,
                },
                state: {params}
            });
        }
        const gotree = (thisdata) => {  
            const params = JSON.stringify(thisdata)
            router.push({
                name: "tree",
                query: {
                    ip : thisdata.data.ip,
                    port : thisdata.data.port
                },
                state: {params}
            });
        };
        watch(
                ()=>detail_data.value,
                (val,preVal)=>{
                    //val为修改后的值,preVal为修改前的值
                    // console.log("message",val,preVal)
                    gotree(detail_data.value)
                },
                {
                    deep:true,
                }
            )
        return{
            detail_data,goother,gotree,
        }
    }
}
</script>


<style scoped>
.content_all {
    display: flex;
    background-color: #F7F8FC;
    flex-direction: row;
    margin-left: 10px;
    margin-right: 10px;
    height: 800px;
    /* border-radius: 5%; */

}

.content_buttons {
    display: flex;
    flex-direction: column;
    width: 15%;
    justify-content: flex-start;
    margin: 10px;
    height: 95%;
    /* background-color: #D3E3FD; */
}

.content_button {
    margin: 10px;
    background-color: #D3E3FD;
}

.content_box {
    background-color: #FFFFFF;
    width: 85%;
    height: 95%;
    margin: 10px;
    /* border-radius: 5%; */

}
</style>

