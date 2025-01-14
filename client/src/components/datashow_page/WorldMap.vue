<template>
    <div class="content">
      <div
        ref="map"
        id = 'map'
        class = 'map'
      ></div>
    </div>
</template>

<script>
    import { onMounted, toRefs,watch,ref } from 'vue'
    import * as echarts from 'echarts'
    import world from '@/assets/world.json'
    export default {
        props:{
            mapdata:{
                type:Array,
                default:'',
            },
        },
        setup (props) {
            onMounted(() => {
                init();
            })
            const mapdata= toRefs(props).mapdata
            const init = () => {
                const myChart = echarts.init(document.getElementById('map'))
                option.value.series[0].data=mapdata.value
                echarts.registerMap('world', world)
                myChart.setOption(option.value, true);
            }
            watch(
                ()=>mapdata.value,
                (val,preVal)=>{
                    echarts.dispose(document.getElementById('map'))
                    init()
                },
                {
                    deep:true,
                }
            )
            let option = ref({
                    backgroundColor: '#F7F7FC ',// 背景颜色
                    tooltip: {
                        triggerOn: 'mousemove',
                        formatter: function (p) {
                            if (p?.data) {
                                var a = `<span style="color:rgba(23, 240, 204)">国家名称：${p.data.name}</span></br>`
                                var b = `<span style="color:rgba(23, 240, 204)">IP数量：${p.data.count}</span></br>`
                                return [a, b].join('')
                            }else{

                            }
                        },
                        backgroundColor: 'rgba(29, 38, 71)',
                        // 额外附加的阴影
                        extraCssText: 'box-shadow:0 0 4px rgba(11, 19, 43,0.8);',
                    },
                    geo: {// 地图配置
                        name: 'worldmap',
                        map: 'world',
                        roam: true,
                        label: {// 通常状态下文本的样式
                            
                            show: false,
                            color: '#fff'
                        },
                        itemStyle: {
                            borderColor: '#5089EC',
                            borderWidth: 1,
                            areaColor: { //地图区域的颜色
                                type: 'radial', // 径向渐变
                                x: 0.5, // 圆心
                                y: 0.5,// 圆心
                                r: 0.8,// 半径
                                colorStops: [
                                { // 0% 处的颜色
                                    offset: 0,
                                    color: 'rgba(0, 102, 154, 0)'
                                },
                                { // 100% 处的颜色
                                    offset: 1,
                                    color: 'rgba(0, 102, 154, .4)'
                                }
                                ]
                            }
                        },
                        emphasis:{//高亮情况下
                            label: { // 图形上的文本标签
                                show : false,
                                color: '#000'
                            },
                            itemStyle: {// 地图区域的样式设置
                                areaColor: '#F8F9F9 ',
                                borderWidth: 0
                            }
                        },
                    },
                    series: [
                        {
                            name: '启动次数', // 浮动框的标题
                            type: 'map',
                            map : 'worldmap',
                            geoIndex: 0,
                            data: []
                        }
                    ]
                })
        }
    }
</script>
<style scoped>
.map{
    width:100%;
    height: 270px;
    background-color: #F8F9F9 ;
}
</style>
