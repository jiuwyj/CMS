<template>
    <div class="all">
        <div class="logo">
            <h1>万维聚真</h1>
        </div>

        <div class="search">
            <div>
                <input class="in" type="text" placeholder="  输入查询语句" v-model.lazy="search_val"/>
            </div>
            <div style="padding-left: 0px;padding-top: 8px">
            <!-- <div style="padding-left: 10px"> -->
                <!-- <el-button @click="get_search" size="large"  color="#03A9F4" circle>
                    <Search style="width: 2em; height: 2em;"></Search>
                </el-button> -->
                <img class="icon-large" src="@/assets/搜索.svg" @click="get_search">
            </div>
        </div>
    
        <div class="rule">
        <div class="son-rule">
            <!-- <h2 @click="show_rule">搜索语法</h2> -->
            <el-button  @click="show_rule" type="primary" round>查询语法</el-button>
        </div>
        </div>
        
        <div class="hot-search">
        <div class="hot-reasch-title">
            <div><p>搜索历史:</p></div>
            <div class="icon-rubbish"><img src="../assets/垃圾桶.svg" alt="删除历史记录"  @click="empty"></div>
        </div>
        <div class="hot-reasch-content">
            <ul>
                <li v-for="(item, index) in historyList" :key="index" >{{ item }}</li>
            </ul>
        </div>
        <div>
            <!-- <button @click="showPopup">显示弹窗</button> -->
            <Popup :visible="popupVisible" :content="popupContent" @close="closePopup" />
        </div>  
        </div>
    </div>
    
</template>  

<script>
import Popup from "@/components/search_page/Popup.vue"
import api from '@/api/index'
import { Search } from '@element-plus/icons-vue';
export default {
    components: {
        Popup,
    },
    data() {
        return {
            search_val: '', //搜索的内容
            historyList: [] ,//历史搜索记录，存本地
            popupVisible: false,
            popupContent: '这是一个弹窗',//弹窗内容
            result:{}
        }
    },
    mounted() {
        //如果本地存储的数据historyList有值，直接赋值给data中的historyList
        if (JSON.parse(localStorage.getItem("historyList"))) {
            this.historyList = JSON.parse(localStorage.getItem("historyList"));
        }
    },
    methods: {
        async checkstring(search_val){
            var result = {}
            await api.getcheck(search_val).then(res =>{
                result=res.data
                // console.log(result['validity'])

            })
            // console.log(result)
            return result
        },

        // 搜索
        async get_search() {
            const result = await this.checkstring(this.search_val);
            // console.log(result['validity'])
            if (this.search_val == '') {
                // this.$toast('请输入搜索内容');
                // this.popupContent= '输入内容为空！！';
                // this.showPopup();
                alert("输入内容为空！！")
            } else if(result['validity']=='Yes'){
                alert(result['error'])
            }else {
                // 没有搜索记录，把搜索值push进数组首位，存入本地
                if (!this.historyList.includes(this.search_val)) {
                this.historyList.unshift(this.search_val);
                localStorage.setItem("historyList", JSON.stringify(this.historyList));
                } else {
                //有搜索记录，删除之前的旧记录，将新搜索值重新push到数组首位
                let i = this.historyList.indexOf(this.search_val);
                this.historyList.splice(i, 1)
                this.historyList.unshift(this.search_val);
                localStorage.setItem("historyList", JSON.stringify(this.historyList));
                }
                //this.search_val = "";//输入栏的内容清空
                if(this.historyList.length==5){
                this.historyList.pop();
                }
                //跳转到搜索结果页
                this.$router.push({
                    path: "/datashow",
                    query: {
                        search_val: this.search_val,
                    },
                });
            }
        },

        //清空历史搜索记录
        empty() {
        // this.$toast.success('清空历史搜索成功');
        
        localStorage.removeItem('historyList');
        this.historyList = [];
        },

        showPopup() {//打开弹窗
        this.popupVisible = true;
        
        },
        closePopup() {//关闭弹窗
        this.popupVisible = false;
        },
        show_rule(){//展示语法规则
        this.popupContent = '规则如下：';
        this.showPopup();
        }
    },
}
</script>


<style scoped>
.all{
width:100%;
min-height: 800px;
background-color: #f5f6fb;;
background-image: url("../assets/back.png");
background-size:cover;
}
.logo {
display: flex;
width: 300px;
height: 200px;
margin: auto;
font-size: 30px;
text-align: center;
align-items: center;
color: hsl(0, 0%, 0%);
}
h1{
    margin-block-start: 0em;
    margin-block-end: 0em
}
.search {
width: 800px;
height: 150px;
margin: auto;
/* padding: 50px; */
/* 弹性盒子模型 */
display: flex;
/* 子盒子在父盒子中垂直居中 */
align-items: center;
/* 子盒子在父盒子中水平居中 */
justify-content: center;
/* background-color: blue; */

}

.in {
width: 600px;
height: 50px;
/* background-color: red; */
font-size: 20px;
border-radius: 20px;
}

.icon-large {
width: 40px;
/* background-color: green; */
padding-left: 10px;
/* padding-top: 100px; */
}

.rule {
width: 200px;
height: 80px;
display: flex;
align-items: center;
justify-content: center;
margin: auto;
/* background-color: red; */
}

/* .son-rule {
border: 2px solid white;
border-radius: 30px;
background-color: green;
} */

/* h2 {
background-color: blue;
} */

.hot-search {
margin: auto;
width: 800px;
height: 200px;
background-color: #FCFDFE;
display: flex;
border-radius: 30px;
flex-direction: column;
}

.hot-reasch-title {
width: 800px;
height: 50px;
margin-left: 20px;
margin-top: 10px;
display: flex;
/* background-color: #AAA; */
}

.icon-rubbish{
margin-left: 600px;
}
.hot-reasch-content {
width: 500px;
/* background-color: aqua; */
margin-left: 10px;
}

/* li {
background-color: aliceblue;
border: 1px solid black;
} */
</style>