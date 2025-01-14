<template>
    <div class="other">
        <p class="title_2">地理信息</p>
        <ol class="geography_list">
            <li class="geography_message">ASN:  {{ asn }}</li>
            <li class="geography_message">城市：{{ city }}</li>
            <li class="geography_message">国家：{{ country }}</li>
        </ol>
    </div>
</template>


<script>
import { reactive,toRefs,watch } from 'vue';  
export default {
    name: 'Other_part',
    props:{
        detail_data:{
            type:Object,
            default:{},
        },
    },
    setup(props){
        const data = reactive({
            detail_data : toRefs(props).detail_data,
            asn : toRefs(props).detail_data.asn,
            city : toRefs(props).detail_data.city,
            country : toRefs(props).detail_data.country
        })
        watch(
            ()=>data.detail_data.value,
            (val,preVal)=>{
                data.asn = data.detail_data.data['asn']
                data.city = data.detail_data.data['city']
                data.country = data.detail_data.data['country']
            },
            {
                deep:true,
            }
        )
        return{
            ...toRefs(data)
        }
    }
}
</script>

<style scoped>
.other {
    background-color: #F7F8FC;
    margin: 10px;
    line-height: auto;
    height: auto;
    padding: 1px;
    /* border-radius: 5%; */

}
.title_2 {
    text-align: left;
    margin-top: 10px;
    margin-bottom: 10px;
    margin-left: 25px;
    margin-right: 10px;
    font-size: 20px;
    line-height: 30px;
    font-weight: bold;
    /* background-color: brown; */
}
.geography_list {
    list-style: none;
    text-align: left;
}
.geography_message {
    margin: 2px;
}
</style>
