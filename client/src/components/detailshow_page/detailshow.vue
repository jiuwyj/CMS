<template>
    <el-container class = 'all'>
      <el-header class="el-header">万维聚真</el-header>
      <el-container>
        <el-main>
          <IP_part :detail_data="detail_data" class="IP_part"></IP_part>
          <Detail_part :detail_data="detail_data" class="Detail_part"/>
        </el-main>
      </el-container>
    </el-container>
</template>


<script>
import IP_part from './IP/ip.vue'
import Detail_part from './Detail/detail.vue'
import { reactive,toRefs } from 'vue';  

export default {
  name: 'detailshow',
  components: {IP_part ,Detail_part },
  props:{
    detail_data:{
        type:Object,
        default:{},
    },
  },
  setup(props){
    const data = reactive({
      detail_data : toRefs(props).detail_data,
    })
    return{
      ...toRefs(data)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.all {
  height: 90%;
  background-color: #f5f6fb;
  min-height: 800px;
}

.el-header {
  height: 50px;
  margin: 10px 10px 0 10px;
  display: flex;
  background: #FCFDFE;
  border-radius: 10px;
  font-size: 24px;
  font-weight: bold;
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
}

.el-main {
  display: flex;
  overflow: hidden;
  /* line-height: auto; */
}
.IP_part {
  width: 30%;
  margin: 10px;
  padding: 10px;
  background: #ffffff;
  border-radius: 10px;
}
.Detail_part{
  width: 1100px;
  margin: 10px;
  padding: 10px;
  background: #FCFDFE;
  border-radius: 10px;
}

</style>
