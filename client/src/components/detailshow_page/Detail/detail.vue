<template>
    <div class="url_part">
        <div class="url_message">
            <!-- <p class="title">URL :{{ detail_data.url }}</p> -->
            <p class="title">更新时间：{{ update_time }}</p>
        </div>
        <content_url :detail_data="detail_data"/>
    </div>
</template>

<script>
import content_url from './detail_components/content.vue'
import { reactive,toRefs,watch } from 'vue';  
export default {
    name: 'Detail_part',
    components: {
        content_url
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
            update_time : toRefs(props).detail_data.ip,
        })
        watch(
            ()=>data.detail_data.value,
            (val,preVal)=>{
                data.update_time = data.detail_data.data['update_time']
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
.url_part {
    background-color: #D7D7D7;
    margin: 10px;
    width: 70%;
    height: 95%;
}
.url_message {
    display: flex;
    flex-direction: row;
}
.status_code, .update_time {
    font-size: 20px;
    line-height: 50px;
    margin: 20px;
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
