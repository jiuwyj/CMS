<template>
    <div class="smap" id="container"></div>
</template>

<script>
import { ref, onMounted, toRefs } from 'vue';
import AMapLoader from '@amap/amap-jsapi-loader';
export default {
    props:{
            smapdata:{
                type:Array,
                default:[],
            },
        },
    setup(props) {
        const mapInstance = ref(null);
        const marker = ref(null);
        const smapdata = toRefs(props).smapdata
        async function loadAMapScript() {
            const AMap = await AMapLoader.load({
                key: '804743ebf785ec6b202d4275c8c3026f',
                version: '2.0',
                plugins: ['AMap.Marker'],
            });

            return AMap;
        }

        async function initMap() {
            const AMap = await loadAMapScript();
            console.log(smapdata.value)
            mapInstance.value = new AMap.Map('container', {
                zoom: 9,//初始缩放程度
                center: smapdata.value,
                // center: [112.9, 27.85],
                // [longitude,latitude]
            });

            marker.value = new AMap.Marker({
                position: mapInstance.value.getCenter(),
                draggable: true,
            });

            marker.value.setMap(mapInstance.value);
        }
        onMounted(async () => {
            await initMap();
        });

        return {};
    },
};
</script>

<style scoped>
.smap{
    background-color: #f2f2f2;
    margin: 10px;                     
    line-height: auto;
    height: auto;
    padding: 1px;
    width: 450px; 
    height: 400px
}

</style>