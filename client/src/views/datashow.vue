<script>
import { onMounted,reactive,toRefs } from 'vue';  
import { useRoute,useRouter } from 'vue-router'
import api from '@/api/index'
import headmod from '@/components/datashow_page/headmod.vue';
import WorldMap from '@/components/datashow_page/WorldMap.vue';
import dataList from '@/components/datashow_page/dataList.vue'
import asidemod from '@/components/datashow_page/asidemod.vue'
import ip_p from '@/components/datashow_page/ip_p.vue'
import loading from '@/components/loading.vue'

export default {
    name : "datashow",
    components: { headmod, dataList, WorldMap, asidemod, loading,ip_p },
    setup(){
        const route = useRoute()
        const router = useRouter()
        const data = reactive({
            dataList : {},
            count:{},
            data:[],
            rank:{},
            truth:{},
            mapdata:[],
            isloading:true,
        })
        const search_val=route.query.search_val;

        onMounted(async()=>{
            try{
                await api.getdataList(search_val).then(res =>{
                data.dataList=res.data
                data.count=res.data.count,
                data.data=res.data.data,
                data.rank=res.data.rank,
                data.truth=res.data.truth,
                data.mapdata=data.rank.country
                data.isloading=false
                })
            }catch(error){
                alert("出错啦，请检查输入语句")
                gosearch()
            }
        })

        const gosearch = () => {  
            router.push({
                path: "/",
            });
        };   

        return { 
            ...toRefs(data)
        }; // 返回变量和方法供模板使用  
    },
}
</script>

<template>
    <div>
        <transition name="fade">
            <loading v-if="isloading"></loading>
        </transition>
    </div>
    <div class="all">
        <el-container>
            <el-header class="common-header">
                <headmod></headmod>
            </el-header>
            <el-container>
                <el-aside class="common-aside">
                    <div style="background: #F7F7FC;padding: 10px;font-weight: 700;">IP世界分布</div>
                    <WorldMap :mapdata="mapdata"></WorldMap>
                    <asidemod :count="count" :rank="rank"></asidemod>
                </el-aside>
                <div style="width: 70%; height: 1200px;">
                    <el-main class="common-main" style="display: flex;">
                        <ip_p :count="count"></ip_p>
                        <div class="rank">
                            <div style="padding-bottom: 15px;font-weight: 700;">引擎IP数量</div>
                            <div style="height: 20px; font-size: 15px;margin-bottom: 10px;margin-left: 5px;">
                                FOFA: &nbsp;{{ count.fofa_total }}
                            </div>
                            <div style="height: 20px; font-size: 15px;margin-bottom: 10px;margin-left: 5px;">
                                Shodan: &nbsp;{{ count.shodan_total }}
                            </div>
                            <div style="height: 20px; font-size: 15px;margin-bottom: 10px;margin-left: 5px;">
                                Hunter: &nbsp;{{ count.hunter_total }}
                            </div>
                            <div style="height: 20px; font-size: 15px;margin-bottom: 10px;margin-left: 5px;">
                                Quake: &nbsp;{{ count.quake_total }}
                            </div>
                            <div style="height: 20px; font-size: 15px;margin-bottom: 10px;margin-left: 5px;">
                                Zoomeye: &nbsp;{{ count.zoomeye_total }}
                            </div>
                        </div>
                    </el-main>
                    <el-main class="common-main">
                        <dataList :dataList="data"></dataList>
                    </el-main>
                </div>
            </el-container>
        </el-container>
    </div>
</template>

<style scoped>
.all{
    background: #f5f6fb; 
    min-height: 600px;
    height:auto;
}
.common-header{
    height: 110px;
    margin: 10px;
    display: flex;
    background: #FCFDFE;
    border-radius: 10px;
}
.common-aside{
    width: 30%;
    margin: 10px;
    padding: 10px;
    background: #FCFDFE;
    border-radius: 10px;
}
.common-main{
    width: 96%; 
    margin: 10px;
    padding: 10px;
    background: #FCFDFE;
    border-radius: 10px;
}
.rank{
    height: 200px;
    width: 30%;
    margin-bottom: 10px;
    padding: 10px;
    padding-top: 170px;
    padding-left: 100px;
}
</style>