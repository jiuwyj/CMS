<template>
    <div class="web">
        <p class="title_2">开放Web服务</p>
        <ol class="ports">
            <!-- <div v-for="(item, index) in paginatedData" :key="index">
                <el-button class="port">21</el-button>
            </div> -->
            <el-button class="port">{{ detail_data.port }}</el-button>
        </ol>
    </div>
</template>

<script>
import { reactive,toRefs } from 'vue';  
export default {
    name: 'Web_part',
    props:{
        detail_data:{
            type:Object,
            default:{},
        },
    },
    setup(props){
        const data = reactive({
            detail_data : toRefs(props).detail_data
        })
        return{
            ...toRefs(data)
        }
    }
}
</script>

<style scoped>
.web {
    background-color: #F2F2F2;
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

.ports {
    text-align: left;
    margin-top: 10px;
    margin-left: 10px;
    margin-right: 10px;
    margin-bottom: 10px;
    line-height: 50px;
    width: auto;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    /* background-color: rgb(48, 125, 148); */
    /* list-style: none; */

}

.port {
    margin: 5px;
}
</style>
