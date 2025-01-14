<script>  
import { onMounted,ref, computed,reactive,toRefs } from 'vue';  
import { ElPagination,ElInput } from 'element-plus';
import { useRoute ,useRouter } from 'vue-router'
import api from '@/api/index'
import { Search, View } from '@element-plus/icons-vue';
import WorldMap from '../datashow_page/WorldMap.vue';
import trust_p from '../datashow_page/trust_p.vue';
import port_rank from '../datashow_page/port_rank.vue';
export default {  
    components: { ElPagination, ElInput, View, WorldMap,trust_p,port_rank },  
    props:{
            count:{
                type:Object,
                default:'',
            },
            rank:{
                type:Object,
                default:'',
            }
        },
    setup(props) {  

        const data = reactive({
            count : toRefs(props).count,
            rank : toRefs(props).rank,
        })
        
        onMounted(()=>{
        })

        return { 
            ...toRefs(data) ,
        }; // 返回变量和方法供模板使用  
    },  
};  
</script>

<template>
    <div class="countrycount">
        <div style="padding-bottom: 15px;font-weight: 700;">国家排名</div>
        <div v-for="(item, index) in rank.country" :key="index" style="height: 20px; font-size: 15px;margin-bottom: 10px;margin-left: 5px;">
            {{ item.name }}&nbsp;:&nbsp;{{ item.count }}
        </div>
    </div>

    <!-- <div class="ipcount">
        <div style="padding: 10px;font-weight: 700;">引擎IP数量</div>
        <div style="height: 40px;display: flex; position: relative;">
            <div style="position: absolute;  left: 5%;text-align: left;font-size: 15px;">FOFA: {{ count.fofa_total }}</div>
            <div style="position: absolute;  left: 55%;font-size: 15px;">Shodan: {{ count.shodan_total }}</div>
        </div>
        <div style="height: 40px;display: flex; position: relative;">
            <div style="position: absolute;  left: 5%;font-size: 15px;">Hunter: {{ count.hunter_total }}</div>
            <div style="position: absolute;  left: 55%;font-size: 15px;">Quake: {{ count.quake_total }}</div>
            <div style="position: absolute;  right: 5%;font-size: 15px;">ALL: 900</div> -->
        <!-- </div>
        <div style="height: 40px;display: flex; position: relative;">
            <div style="position: absolute;  left: 5%;font-size: 15px;">Zoomeye: {{ count.zoomeye_total }}</div>
        </div>
    </div> -->

    <div class="trust">
        <div style="padding: 10px;font-weight: 700;">引擎可信度</div>
        <div class="trust_p">
            <trust_p></trust_p>
        </div>
        <div style="height: 40px;display: flex; position: relative;">
            <div style="position: absolute;  left: 5%;text-align: left;font-size: 15px;">FOFA: 0.925473</div>
            <div style="position: absolute;  left: 55%;font-size: 15px;">Shodan: 0.973800</div>
        </div>
        <div style="height: 40px;display: flex; position: relative;">
            <div style="position: absolute;  left: 5%;font-size: 15px;">Hunter: 0.998256</div>
            <div style="position: absolute;  left: 55%;font-size: 15px;">Quake: 0.961443</div>
            <!-- <div style="position: absolute;  right: 5%;font-size: 15px;">ALL: 900</div> -->
        </div>
        <div style="height: 40px;display: flex; position: relative;">
            <div style="position: absolute;  left: 5%;font-size: 15px;">Zoomeye: 0.981560</div>
        </div>
    </div>

    <div class="rank_port">
        <div style="padding-bottom: 15px;font-weight: 700;">端口排行</div>
        <div class="port_rank">
            <port_rank :rank="rank"></port_rank>
        </div>
        <div v-for="(item, index) in rank.port" :key="index" style="height: 20px; font-size: 15px;margin-bottom: 10px;margin-left: 5px;">
            Port&nbsp;{{ item.name }}&nbsp;:&nbsp;{{ item.count }}
        </div>
    </div>
    <div class="rank">
        <div style="padding-bottom: 15px;font-weight: 700;">协议排行</div>
        <div v-for="(item, index) in rank.protocol" :key="index" style="height: 20px; font-size: 15px;margin-bottom: 10px;margin-left: 5px;">
            Protocol&nbsp;{{ item.name }}&nbsp;:&nbsp;{{ item.count }}
        </div>
    </div>
    <div class="rank">
        <div style="padding-bottom: 15px;font-weight: 700;">服务排行</div>
        <div v-for="(item, index) in rank.server" :key="index" style="height: 20px; font-size: 15px;margin-bottom: 10px;margin-left: 5px;">
            Server&nbsp;{{ item.name }}&nbsp;:&nbsp;{{ item.count }}
        </div>
    </div>
</template>

<style scoped>
    .ipcount{
        background-color: #F7F7FC ;
        margin-bottom: 10px;
        position: relative;
    }
    .rank{
        height: 180px;
        background-color: #F7F7FC ;
        margin-bottom: 10px;
        padding: 10px;
    }
    .rank_port{
        /* height: 180px; */
        background-color: #F7F7FC ;
        margin-bottom: 10px;
        padding: 10px;
    }
    .countrycount{
        /* height: 180px; */
        background-color: #F7F7FC ;
        margin-bottom: 10px;
        padding: 10px;
    }
    .trust_p{
        height: 450px;
        background-color: #F7F7FC ;
    }
    .port_rank{
        height: 300px;
        background-color: #F7F7FC ;
    }
    .trust_g{
        height: 100px;
        padding-left: 10px;
        font-size: 15px;
        color:rgba(0, 0, 0, 0.75);
        background-color: #F7F7FC ;
        position: absolute;
        right: 0; 
    }
    .trust{
        background-color: #F7F7FC ;
        margin-bottom: 10px;
        position: relative;
    }
</style>