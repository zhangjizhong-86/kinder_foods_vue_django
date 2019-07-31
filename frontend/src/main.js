import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// import 'bootstrap'
// import 'bootstrap/dist/css/bootstrap.min.css'
// import SelectDate from '@/components/SelectDate.vue' //global import

Vue.use(BootstrapVue)
Vue.use(VueResource)
Vue.config.productionTip = false
// Vue.component('selectDate', SelectDate) //global registration

new Vue({
  router,
  render: h => h(App)
//  'render: h => h(App)' is a shortened expression of below:
//   render: function (createElement) {
//     return createElement(App);
// }
}).$mount('#app')
