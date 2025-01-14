import path from "./path"
import axios from "../utils/request"

const api = {
    getcheck(thissearch_val){
        return axios.get(path.baseUrl + path.check,{
            params: {
                search_val : thissearch_val
             }
        })
            
    },
    getdataList(thissearch_val){
        return axios.get(path.baseUrl + path.datashow,{
            params: {
                search_val : thissearch_val
             }
        })
            
    },
    getdetail(thisip,thisport){
        return axios.get(path.baseUrl + path.detail,{
            params: {
                ip : thisip,
                port : thisport,
             }
        })
            
    },
    gettree(){
        return axios.get(path.baseUrl + path.tree)
            
    },
    getotherdetail(thisotherdetail){
        return axios.get(path.baseUrl + path.otherdetail,{
            params: {
                sotherdetail : thisotherdetail
             }
        })
    }
    // getdata(){
    //     return axios.get(path.baseUrl + path.data)
            
    // },
}

export default api