import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'
import router from './router'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// import 'bootstrap'
// import 'bootstrap/dist/css/bootstrap.min.css'
// import SelectDate from '@/components/SelectDate.vue' //global import

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueResource)
Vue.config.productionTip = false
// Vue.component('selectDate', SelectDate) //global registration

router.beforeEach((to, from, next) => {
  document.title = to.meta.title
  next()
})

new Vue({
  router,
  render: h => h(App)
//  'render: h => h(App)' is a shortened expression of below:
//   render: function (createElement) {
//     return createElement(App);
// }
}).$mount('#app')
