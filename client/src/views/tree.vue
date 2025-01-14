<template>
    <div class="content">
        <!-- {{ detail_data.tree }} -->
      <div
        ref="main"
        id = 'main'
        class = 'main'
      ></div>
    </div>
</template>

<script>
import * as echarts from "echarts";
import api from '@/api/index'
import { useRoute } from 'vue-router'
import { onMounted,reactive,toRefs,watch } from 'vue';  

export default {
    setup(){
        const route = useRoute()

        onMounted(async () => {
            let treeData = JSON.parse(history.state.params)['tree']
            init(treeData);
        });
        //初始化函数
        function init(treeData) {
            // 基于准备好的dom，初始化echarts实例
            let Chart = echarts.init(document.getElementById("main"));
            // 绘制图表
            let options = {
                tooltip: {
                    trigger: 'item',
                    triggerOn: 'mousemove',
                    formatter:function(params){
                        var tip = ''
                        if(params!=null ){
                            let name = '属性值：'
                            let fofa = 'FOFA: '
                            let hunter = 'Hunter: '
                            let zoomeye = 'Zoomeye: '
                            let quake = 'Quake: '
                            let shodan = 'Shodan: '
                            
                            tip += params.marker + name + params.data.name+'<br/>'
                            tip += params.marker + fofa + params.data.fofa+'<br/>'
                            tip += params.marker + hunter + params.data.hunter+'<br/>'
                            tip += params.marker + zoomeye + params.data.zoomeye+'<br/>'
                            tip += params.marker + quake + params.data.quake+'<br/>'
                            tip += params.marker + shodan + params.data.shodan+'<br/>'
                        }
                        return tip
                    }
                },
                series: [
                    {
                    type: 'tree',
                    data: [treeData],
                    top: '18%',
                    bottom: '14%',
                    layout: 'radial',
                    symbol: 'emptyCircle',
                    symbolSize: 17,
                    initialTreeDepth: 13,
                    animationDurationUpdate: 750,
                    itemStyle: { color: "#7ed3f4" },
                    symbol: "circle",// 实心
                    label: {
                        // position: "top",
                        rotate: 0,
                        verticalAlign: "middle",
                        // align: "right",
                        fontSize: 14,
                    },
                    emphasis: {
                        focus: 'descendant'
                    }
                    }
                ]
            }
            // 渲染图表
            Chart.setOption(options);
        }

    }
}


</script>

<style scoped>
.main{
    width:800px;
    height: 750px;
}
</style>
