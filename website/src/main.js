import Vue from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import VueGoodTable from 'vue-good-table'
import './registerServiceWorker'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import FontAwesome from '@fortawesome/fontawesome'
import solidIcons from '@fortawesome/fontawesome-free-solid'
import regularIcons from '@fortawesome/fontawesome-free-regular'

FontAwesome.library.add(solidIcons, regularIcons)

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(VueGoodTable)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
