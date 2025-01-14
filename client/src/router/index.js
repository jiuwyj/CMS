import { createRouter, createWebHashHistory } from 'vue-router'
import search from '../views/search.vue'

const routes = [
  {
    path: '/',
    name: 'search',
    component: search
  },
  {
    path: '/datashow',
    name: 'datashow',
    component: ()=>import('../views/datashow.vue')
  },
  {
    path: '/detail',
    name: 'detail',
    component: ()=>import('../views/detail.vue'),
    children:[ // 嵌套子路由
            {
                path:'otherdetail', // 子页面1
                name:'otherdetail',
                component:()=>import('../views/otherdetail.vue')
            },
            {
                path:'tree', // 子页面2
                name:'tree',
                component:()=>import('../views/tree.vue')
            },
    ]
  },
  {
    path: '/loading',
    name: 'loading',
    component: ()=>import('../views/loading.vue')
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
