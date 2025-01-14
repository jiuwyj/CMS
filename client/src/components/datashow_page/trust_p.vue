<template>
    <div class="content">
      <div
        ref="main"
        id = 'main'
        class = 'main'
      ></div>
    </div>
</template>

<script setup>
    import * as echarts from "echarts";
    import { onMounted } from "vue";

    //声明周期函数，自动执行初始化
    onMounted(() => {
        init();
    });
    //初始化函数
    function init() {
        // 基于准备好的dom，初始化echarts实例
        let Chart = echarts.init(document.getElementById("main"));
        // 绘制图表
        let options = {
        legend: {
            data: ['confidence level']
        },
        radar: {
            // shape: 'circle',
            indicator: [
            { name: 'FOFA', max: 100 },
            { name: 'ShuDan', max: 100 },
            { name: 'Zoomeye', max: 100 },
            { name: 'Hunter', max: 100 },
            { name: 'Quake', max: 100 },
            ],
            splitArea : {
            show : true,   
            areaStyle : {
                // color: ['#7ED3F4']  
                // 图表背景网格的颜色
            }
        },
        },
        series: [
            {
            name: 'confidence level',
            type: 'radar',
            data: [
                {
                value: [92, 97, 98, 99, 96],
                name: 'confidence level',
                itemStyle: { //该数值区域样式设置
                        color: 'rgba(26,165,255,0.3)', //背景颜色，还需设置areaStyle
                        lineStyle: {
                            color: 'rgba(255,225,0,.3)', //边框颜色
                        },
                    },
                    label: {  //显示value中具体的数值
                        show: true,
                        color:'blue'
                    }, 
                    areaStyle: { //设置区域背景颜色透明度
                        width: 1,
                        opacity: 1,
                    },     
                },
            ]
            }
        ]
        };
        // 渲染图表
        Chart.setOption(options);
    }
</script>

<style scoped>
.main{
    width:400px;
    height: 450px;
}
</style>
