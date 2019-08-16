import Vue from 'vue'
import Router from 'vue-router'
// import APP from '@/App.vue'
import MenuView from '@/views/MenuView.vue'; 
import ChartView from '@/views/ChartView.vue';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'menu-view',
      component: MenuView,
      meta: {
        title: '博士娃幼儿园每周菜谱'
      }
    },
    {
      path: '/chart',
      name: 'chart-view',
      component: ChartView,
      meta: {
        title: '博士娃幼儿园每周菜谱'
      }
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
    //   component: () => import(/* webpackChunkName: "chart" */ './views/ChartView.vue')
    }
  ]
})
