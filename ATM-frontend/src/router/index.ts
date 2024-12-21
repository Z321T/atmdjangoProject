import {createRouter,createWebHistory}from 'vue-router'

//引入可能要呈现的组件
import InsertCard from '@/views/InsertCard.vue'
import Login from '@/views/Login.vue'
import SelectService from '@/views/SelectService.vue'
import Withdraw from '@/views/Withdraw.vue'
import Inquiry from '@/views/Inquiry.vue'
import TakeCard from '@/views/TakeCard.vue'
import InvalidPass from '@/views/InvalidPass.vue'
import WithdrawSuccess from '@/views/WithdrawSuccess.vue'
import WithdrawFailure from '@/views/WithdrawFailure.vue'
import Zhuanzhang from '@/views/Zhuanzhang.vue'
import ModifyPassword from '@/views/ModifyPassword.vue'
import PasswordFailure from '@/views/PasswordFailure.vue'
import PasswordSuccess from '@/views/PasswordSuccess.vue'
import CunKuan from '@/views/CunKuan.vue'
import TransferFail from '@/views/TransferFail.vue'
import TransferSuccess from '@/views/TransferSuccess.vue'
import DepositSuccess from '@/views/DepositSuccess.vue'

const router=createRouter({
    history:createWebHistory(),
    routes:[
        {
            path: '/DepositSuccess',
            name:'  DepositSuccess',
            component: DepositSuccess
            },
        {
            path: '/TransferSuccess',
            name:'  TransferSuccess',
            component:TransferSuccess
            },
        {
            path: '/TransferFail',
            name:'TransferFail',
            component: TransferFail
            },

        {
            path: '/CunKuan',
            name:'  CunKuan',
            component: CunKuan
            },

        {
            path: '/PasswordSuccess',
            name:'  PasswordSuccess',
            component: PasswordSuccess
            },

        {
            path: '/PasswordFailure',
            name:'  PasswordFailure',
            component: PasswordFailure
            },
        {
            path: '/ModifyPassword',
            name:'ModifyPassword',
            component: ModifyPassword
            },

        {
            path: '/Zhuanzhang',
            name:'Zhuanzhang',
            component: Zhuanzhang
            },

        {
            path: '/WithdrawFailure',
            name:'WithdrawFailure',
            component: WithdrawFailure
            },


        {
            path: '/WithdrawSuccess',
            name:'WithdrawSuccess',
            component: WithdrawSuccess
            },

        {
        path: '/InsertCard',
        name:'InsertCard',
        component: InsertCard
        },
        {
            path: '/InvalidPass',
            name:'InvalidPass',
            component:InvalidPass
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
