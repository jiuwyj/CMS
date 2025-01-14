<template>
    <div>
        <transition name="fade">
            <loading v-if="isloading"></loading>
        </transition>
    </div>
    <detailshow :detail_data="detail_data"/>
</template>

<script>
    import detailshow from '../components/detailshow_page/detailshow.vue'
    import loading from '@/components/loading.vue'
    import { onMounted,reactive,toRefs } from 'vue';  
    import { useRoute,useRouter } from 'vue-router'
    import api from '@/api/index'
    export default {
        name: 'detail',
        components: {
            detailshow,loading
        },

        setup(){
            const route = useRoute()
            const router = useRouter()
            const data = reactive({
                ip : route.query.ip,
                port : route.query.port,
                detail_data : {},
                isloading:true,
                // data : {},
                // tree : {},
                // truth_sum : 96
            })
            onMounted(async()=>{
                try{
                    await api.getdetail(data.ip,data.port).then(res =>{
                        data.detail_data=res.data
                        data.isloading=false
                    })
                }catch(error){
                    alert("出错啦，请检查输入语句")
                    gosearch()
                }

            })
            const gosearch = () => {  
                router.push({
                    path: "/",
                });
            };  
            return { 
                ...toRefs(data)
            };
        }
    }
</script>

<style scoped>

</style>
