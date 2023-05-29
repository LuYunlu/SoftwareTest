import { createRouter, createWebHistory } from 'vue-router'

const routes = [

  {
    path: '/',
    name: 'home',
   component:()=>import('../views/HomeView.vue')
  },
  {
    path:"/similar",
    name:'similar',
    component:()=>import('../views/SimilarView.vue')
  },
  {
    path:"/warning",
    name:'warning',
    component:()=>import('../views/WarnView.vue')
  },


]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router


