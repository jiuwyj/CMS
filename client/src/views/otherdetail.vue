<template>
    <el-scrollbar class="other">
        <span v-for="(value, key) in detail_data.data" :key="key" class="one"><p  v-if="value!=' '"><b>{{ key }}:</b>&nbsp;&nbsp;{{ value }}</p></span>
    </el-scrollbar>
</template>

<script>
    import { reactive,toRefs } from 'vue';  
    export default {
        name: 'detail',
        setup(){
            const data = reactive({
                detail_data : JSON.parse(history.state.params),
            })
            return { 
                ...toRefs(data)
            };
        }
    }
</script>

<style scoped>
.one{
    width:95%;
    height: 15px;
    text-align: left;
    /* padding-left: 5px;  */
    overflow-wrap: break-word; 
}
.other{
    padding-left: 5px;
}
</style>
