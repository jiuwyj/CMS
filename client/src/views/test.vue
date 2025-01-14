<template>
    <div class="content">
      <div
        ref="port"
        id = 'port'
        class = 'port'
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
        let Chart = echarts.init(document.getElementById("port"));
        // 绘制图表
        let options = {
            legend: {
                data: ['80','443', '8443', '8008','8080']
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
                }
            ]
            };
        // 渲染图表
        Chart.setOption(options);
    }
</script>

<style scoped>
.port{
    width:300px;
    height: 300px;
}
</style>
