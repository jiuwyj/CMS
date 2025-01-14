<template>
    <div class="content">
      <div
        ref="ip"
        id = 'ip'
        class = 'ip'
      ></div>
    </div>
</template>

<script>
import * as echarts from "echarts";
import api from '@/api/index'
import { useRoute } from 'vue-router'
import { onMounted,reactive,toRefs,watch,ref } from 'vue';  

export default {
    props:{
        count:{
            type:Object,
            default:'',
        },
    },
    setup(props){
        const count = toRefs(props).count;
        const data = [];
        const data1= [];
        const timer = ref([])
        for (let i = 0; i < 5; ++i) {
            data.push(0);
        }
        watch(
            ()=>count.value,
            (val,preVal)=>{
                data1.push(count.value.shodan_total);
                data1.push(count.value.hunter_total);
                data1.push(count.value.quake_total);
                data1.push(count.value.zoomeye_total);
                data1.push(count.value.fofa_total);
            },
            {
                deep:true,
            }
        )
        onMounted(async () => {
            let Chart = echarts.init(document.getElementById("ip"));
            let options = {
                xAxis: {
                    max: 'dataMax'
                },
                yAxis: {
                    type: 'category',
                    data: ['Shodan','Hunter', 'Quake', 'Zoomeye','FOFA'],
                    inverse: true,
                    animationDuration: 300,
                    animationDurationUpdate: 300,
                    max: 4 // only the largest 3 bars will be displayed
                },
                
                series: [
                    {
                    realtimeSort: true,
                    name: '数据数量',
                    type: 'bar',
                    data: data,
                    itemStyle: {
                        //这里是颜色
                        color: function(params) {
                            //注意，如果颜色太少的话，后面颜色不会自动循环，最好多定义几个颜色
                            var colorList = ['#ffdc60','#91cc75', '#5470c6', '#7eD3f4', '#ff7070','#749f83', '#ca8622'];
                            return colorList[params.dataIndex]
                        }
                    },
                    label: {
                        show: true,
                        position: 'right',
                        valueAnimation: true
                    }
                    }
                ],
                legend: {
                    show: true
                },
                animationDuration: 0,
                animationDurationUpdate: 3000,
                animationEasing: 'linear',
                animationEasingUpdate: 'linear'
                };
            timer.value.push(setTimeout(() => {
                run(Chart,options);
            }, 0))
            timer.value.push(setInterval(() => {
                run(Chart,options);
            }, 1000))
        });
        function run(Chart,options) {
            for (var i = 0; i < data.length; ++i) {
                if (data1[i] - data[i] > 10000000) {
                data[i] += 10000000;
                } else if (data1[i] - data[i] > 1000000) {
                data[i] += 1000000;
                } else if (data1[i] - data[i] > 100000) {
                data[i] += 100000;
                } else if (data1[i] - data[i] > 10000) {
                data[i] += 10000;
                } else if (data1[i] - data[i] > 1000) {
                data[i] += 1000;
                } else if (data1[i] - data[i] > 100) {
                data[i] += 100;
                } else if (data1[i] - data[i] > 10) {
                data[i] += 10;
                } else if (data1[i] - data[i] > 0) {
                data[i] += 1;
                }
            }
            Chart.setOption(options);
        }

    }
}


</script>

<style scoped>
.ip{
    width:650px;
    height: 400px;
}
</style>
