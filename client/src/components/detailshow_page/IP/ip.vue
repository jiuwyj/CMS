<template>
    <div class="ip">
        <!-- {{ detail_data.truth_sum }} -->
        <p class="title">{{'IP :' + ip }}</p>
        <p class="title">{{'Port :' + port }}</p>
        <div style="padding: 10px;font-weight: 700;">可信数据来源</div>
        <datafrom :detail_data="detail_data"></datafrom>
        <div style="padding: 10px;font-weight: 700;">数据可信度</div>
        <trust :detail_data="detail_data"></trust>   
        <!-- <smap :smapdata="smapdata"/> -->
        <!-- <Other_part :detail_data="detail_data"/> -->
    </div>
</template>

<script>
import Other_part from "./ip_components/Other.vue";
import smap from "./ip_components/smap.vue";
import trust from "./ip_components/trust.vue";
import datafrom from "./ip_components/datafrom.vue";
import { toRefs,watch,ref,reactive } from 'vue';  
export default {
    name: 'IP_part',
    components: {
        Other_part,
        smap,
        trust,
        datafrom
    },
    props:{
        detail_data:{
            type:Object,
            default:{},
        },
    },
    setup(props){
        const data = reactive({
            detail_data : toRefs(props).detail_data,
            ip : toRefs(props).detail_data.ip,
            port : toRefs(props).detail_data.port,
            truth_sum : toRefs(props).detail_data.truth_sum
        })
        let smapdata = ref([])
        watch(
            ()=>data.detail_data.value,
            (val,preVal)=>{
                data.ip = data.detail_data.data['ip']
                data.port = data.detail_data.data['port']
            },
            {
                deep:true,
            }
        )
        return{
            ...toRefs(data),smapdata
        }
    }
}
</script>

<style scoped>
.ip {
    width: 30%;
    background-color: #D7D7D7;
    margin: 10px;
    /* border-radius: 5%; */
    line-height: auto;
    height: 95%;
    padding: 1px;
}

.title {
    text-align: left;
    margin: 20px;
    font-size: 30px;
    line-height: 50px;
    font-weight: bolder;
    /* width: 50%; */
    /* background-color: antiquewhite; */
}

</style>
