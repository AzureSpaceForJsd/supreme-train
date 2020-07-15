import Vue from 'vue'
import Router from 'vue-router'
import MeetingReserve from '@/components/Order/MeetingReserve'
import Orderlist from '@/components/Order/Orderlist'
import Login from '@/components/User/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/Order/MeetingReserve',
      name: 'MeetingReserve',
      component: MeetingReserve
    },
    {
      path: '/',
      name: 'Orderlist',
      component: Orderlist
    },
    {
      path: '/user/login',
      name: 'Login',
      component: Login
    }
  ]
})
