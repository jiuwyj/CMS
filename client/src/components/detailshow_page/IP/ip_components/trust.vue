<template>
    <div class="content">
      <div
        ref="trust"
        id = 'trust'
        class = 'trust'
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
                let num = data.detail_data.truth_sum
                num = 100*num
                num = num.toFixed(3)
                // console.log(typeof(num))
                confident[0].value=num
                init()

            },
            {
                deep:true,
            }
        )

        //初始化函数
        function init() {
            // 基于准备好的dom，初始化echarts实例
            let Chart = echarts.init(document.getElementById("trust"));
            // 绘制图表
            let options = {
                series: [
                    {
                    type: 'gauge',
                    startAngle: 70,
                    endAngle: -240,
                    pointer: {
                        show: false
                    },
                    progress: {
                        show: true,
                        overlap: false,
                        roundCap: true,
                        clip: false,
                        itemStyle: {
                        borderWidth: 1,
                        borderColor: '#73C0DE'
                        }
                    },
                    axisLine: {
                        lineStyle: {
                        width: 30
                        }
                    },
                    splitLine: {
                        show: false,
                        distance: 0,
                        length: 10
                    },
                    axisTick: {
                        show: false
                    },
                    axisLabel: {
                        show: false,
                        distance: 50
                    },
                    data: confident,
                    title: {
                        fontSize: 15
                    },
                    detail: {
                        width: 100,
                        height: 50,
                        fontSize: 30,
                        color: 'inherit',
                        borderColor: 'inherit',
                        borderRadius:80,
                        borderWidth: 0,
                        formatter: '{value}%'
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
.trust{
    width: 300px;
    height: 300px;
    

}
.content{
    display: flex;
    justify-content: center;
}
</style>
