<template>
    <div class="loading"></div>
</template>

<script>
import { useRoute,useRouter } from 'vue-router'
export default {
    name: 'Loading', // 定义的组件名称 使用时写法：loading
    created(){
        const router = useRouter()
        const route = useRoute()
        let search_val = route.query.search_val;
        setTimeout(function(){
            router.push("/datashow?search_val="+search_val)
        },500)
    }
}
</script>

<style scoped>
.loading {
    position: fixed;
    left: 0;
    top: 0;
    background: url('~@/assets/three-dots.svg') center center no-repeat #F5F6FB;
    width: 100vw;
    height: 100vh;
    z-index: 9000;
}
</style>
