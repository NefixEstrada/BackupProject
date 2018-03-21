import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
import Backup from './views/Backup.vue'
import Archive from './views/Archive.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/backup/:backupId',
      name: 'backup',
      component: Backup
    },
    {
      path: '/backup/:backupId/:archiveName',
      name: 'archive',
      component: Archive
    }
  ]
})
