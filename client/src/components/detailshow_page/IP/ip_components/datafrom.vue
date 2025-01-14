<template>
    <div class="content">
      <div
        ref="from"
        id = 'from'
        class = 'from'
      ></div>
    </div>
</template>

<script>
import * as echarts from "echarts";
import api from '@/api/index'
import { onMounted,reactive,toRefs,watch } from 'vue';  

export default {
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

        let confident = [
                {
                    value: 0,
                    name: 'Confidence lever',
                    title: {
                    offsetCenter: ['0%', '-30%']
                    },
                    detail: {
                    valueAnimation: true,
                    offsetCenter: ['0%', '10%']
                    }
                },
            ]

        watch(
            ()=>data.detail_data.value,
            (val,preVal)=>{
                let datafrom = data.detail_data.datafrom[0]
                // console.log(datafrom)
                init(datafrom)
            },
            {
                deep:true,
            }
        )
        
        //初始化函数
        function init(datafrom) {
            // 基于准备好的dom，初始化echarts实例
            let Chart = echarts.init(document.getElementById("from"));
            // 绘制图表
            let options = {
                legend: {
                    data: ['Shodan','Hunter', 'Quake', 'Zoomeye','FOFA'],
                },
                tooltip: {
                    // trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                },
                series: [
                    {
                    name: '可信数据来源',
                    type: 'pie',
                    radius: '65%',
                    center: ['50%', '50%'],
                    selectedMode: 'single',
                    data: datafrom,
                    emphasis: {
                        itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                    }
                ]
                };

            // 渲染图表
            Chart.setOption(options);
        }
        return{
            ...toRefs(data)
        }
    }
}
</script>

<style scoped>
.from{
    width: 400px;
    height: 400px;
}
.content{
    display: flex;
    justify-content: center;
}
</style>
