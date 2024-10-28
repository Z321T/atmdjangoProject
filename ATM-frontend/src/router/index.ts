import {createRouter,createWebHistory}from 'vue-router'

//引入可能要呈现的组件
import InsertCard from '@/views/InserCard.vue'
import Login from '@/views/Login.vue'
import SelectService from '@/views/SelectService.vue'
import Withdraw from '@/views/Withdraw.vue'
import Inquiry from '@/views/Inquiry.vue'
import TakeCard from '@/views/TakeCard.vue'

//创建路由器
const router=createRouter({
    history:createWebHistory(),
    routes:[
        {
        path: '/InsertCard',
        name:'InsertCard',
        component: InsertCard
        },
        {
            path: '/Login',
            name:'Login',
            component: Login
        },
        {
            path: '/SelectService',
            name:'SelectService',
            component: SelectService
        },
        {
            path: '/Withdraw',
            name:'Withdraw',
            component: Withdraw
        },
        {
            path: '/Inquiry',
            name:'Inquiry',
            component: Inquiry
        },
        {
            path: '/TakeCard',
            name:'TakeCard',
            component: TakeCard
        },

    ]
})

export default router
