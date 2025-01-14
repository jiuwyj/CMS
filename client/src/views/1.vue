<template>
    <div class="content">
      <div
        ref="port"
        id = 'port'
        class = 'port'
      ></div>
    </div>
</template>

<script>
import * as echarts from "echarts";
import { onMounted,reactive,toRefs,watch,ref } from 'vue';  

export default {
    props:{
        rank:{
            type:Object,
            default:'',
        },
    },
    setup(props){
        const rank = toRefs(props).rank;
        const data1 = [
        ];
        const data2 = [
        ];
        watch(
            ()=>rank.value,
            (val,preVal)=>{
                // console.log(rank)
                data1.push({value: 100, name: rank.value.port[0].name});
                data1.push({value: 80, name: rank.value.port[1].name});
                data1.push({value: 60, name: rank.value.port[2].name});
                data1.push({value: 40, name: rank.value.port[3].name});
                data1.push({value: 20, name: rank.value.port[4].name});

                data2.push(rank.value.port[0].name);
                data2.push(rank.value.port[1].name);
                data2.push(rank.value.port[2].name);
                data2.push(rank.value.port[3].name);
                data2.push(rank.value.port[4].name);
                console.log(data1)
                console.log(data2)
                init()
            },
            {
                deep:true,
            }
        )
        //声明周期函数，自动执行初始化
        onMounted(() => {
            init();
        });
        //初始化函数
        function init() {
            // 基于准备好的dom，初始化echarts实例
            let Chart = echarts.init(document.getElementById("port"));
            // 绘制图表
            let options = {
                legend: {
                    data: data2
                },
                series: [
                    {
                    name: '排行',
                    type: 'funnel',
                    left: '10%',
                    top: 60,
                    bottom: 60,
                    width: '80%',
                    min: 0,
                    max: 100,
                    minSize: '0%',
                    maxSize: '100%',
                    sort: 'descending',
                    gap: 2,
                    // label: {
                    //     show: true,
                    //     position: 'inside'
                    // },
                    labelLine: {
                        length: 10,
                        lineStyle: {
                        width: 1,
                        type: 'solid'
                        }
                    },
                    itemStyle: {
                        borderColor: '#fff',
                        borderWidth: 1
                    },
                    emphasis: {
                        label: {
                        fontSize: 20
                        }
                    },
                    data: [
                    { value: 100, name: '80',},
                    { value: 80, name: '443' },
                    { value: 60, name: '8443' },
                    { value: 40, name: '8008' },
                    { value: 20, name: '8080' }
                    ],
                    // data: data1
                    }
                ]
                };
            // 渲染图表
            Chart.setOption(options);
        }
    }
}


</script>

<style scoped>
.content{
    width:300px;
    height: 300px;
}
</style>
