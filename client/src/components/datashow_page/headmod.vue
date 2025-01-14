<script>  
import { reactive, toRefs } from 'vue';  
import { ElPagination,ElInput } from 'element-plus';  
import { useRouter } from 'vue-router'
import Popup from "../search_page/Popup.vue"
import api from '@/api/index'

export default {  
    components: { ElPagination,ElInput,Popup },  
    setup() {  
        const data=reactive({
            search_val:'',
            popupVisible: false,
            popupContent: '这是一个弹窗',//弹窗内容            
        })
        const router = useRouter()
        const checkstring= async()=>{
            var result = {}
            await api.getcheck(data.search_val).then(res =>{
                result=res.data
            })
            return result
        }
        const godatashow = () => {  
            router.push({
                path: "/loading",
                query: {
                    search_val: data.search_val,
                },
            });        
        };   
        // 搜索
        const get_search= async()=> {
            const result = await checkstring(data.search_val);
            // console.log(result['validity'])
            if (data.search_val == '') {
                alert('输入内容为空')
            } else if(result['validity']=='Yes'){
                alert(result['error'])
            }else {
                godatashow()
            }
        }

        const showPopup=()=> {//打开弹窗
            data.popupVisible = true;
        }
        const closePopup=()=> {//关闭弹窗
            data.popupVisible = false;
        }
        const show_rule=()=>{//展示语法规则
            data.popupContent = '规则如下：';
            showPopup();
        }

        return { 
            ...toRefs(data),checkstring,get_search,showPopup,show_rule,closePopup
        }; // 返回变量和方法供模板使用  
    },  

};  
</script>

<template>
    <div class="logobox">
        <img class="logo" src="../../assets/logo.jpg" alt="">
        <h1 class="title">万维聚真</h1>
    </div> 
    <div class="searchbox">
        <div>
            <input class="input" type="text" placeholder="  输入查询语句" v-model.lazy="search_val"/>
        </div>
        <div style="padding-left: 10px;padding-top: 8px">
        <!-- <div style="padding-left: 10px"> -->
            <!-- <el-button @click="get_search" size="large"  color="#03A9F4" circle>
                <Search style="width: 2em; height: 2em;"></Search>
            </el-button> -->
            <img style="height: 40px;" src="@/assets/搜索.svg" @click="get_search">
        </div>
    </div>
    <div class="linkbox">
        <el-menu
            class="filebox"
        >
            <el-sub-menu index="1">
                <template #title>相关文档</template>
                <el-menu-item index="2-1" @click="show_rule" type="primary" round>查询语法</el-menu-item>
            </el-sub-menu>
        </el-menu>
    </div>
    <div>
        <!-- <button @click="showPopup">显示弹窗</button> -->
        <Popup :visible="popupVisible" :content="popupContent" @close="closePopup" />
    </div>  
</template>

<style scoped>
    .logo{
        height: 100px;
    }
    .title{
        /* width:50px; */
        height: max-content;
        color: rgb(0, 0, 0);
        
    }
    .input {  
        /* width: 500px!important; */
        width: 600px;
        height: 50px;
        /* background-color: red; */
        font-size: 20px;
        border-radius: 20px;
    }  
    .logobox{
        width: 30%;
        height: 100px;
        display: flex; 
        align-items: center;
    }
    .searchbox{
        width: 70px;
        height: 100px;
        padding-left: 10px;
        /* 弹性盒子模型 */
        display: flex;
        /* 子盒子在父盒子中垂直居中 */
        align-items: center;
        /* 子盒子在父盒子中水平居中 */
        justify-content: flex-start;
    }
    .linkbox{
        height: 100px;
        margin-left: auto;
        display: flex;
        align-items: center;
    }
    .filebox{
        /* 子盒子在父盒子中垂直居中 */
        height: 50px;
    }
</style>