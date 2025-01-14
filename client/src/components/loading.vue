<template>
    <div class="loading"><div class="text">数据加载需要较长时间，请耐心等待</div></div>
    <!-- <div class="text">数据加载需要较长时间，请耐心等待</div> -->
</template>

<script>
export default {
    name: 'Loading' // 定义的组件名称 使用时写法：loading
}
</script>

<style scoped>
.loading {
    display: flex;
    justify-content: center; 
    align-items: center;
    position: fixed;
    left: 0;
    top: 0;
    background: url('~@/assets/three-dots.svg') center center no-repeat #F5F6FB;
    width: 100vw;
    height: 100vh;
    z-index: 9000;
}
.text{
    z-index: 9000;
    height: 150px;
    color: #0f7dec;
    /* top: 1000px; */
    /* position: fixed;
    left: 0;
    top: 0; */
}
</style>
