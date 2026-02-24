import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: () => import('../views/PlantsDashboardView.vue') },
    { path: '/plants/:id', component: () => import('../views/PlantDetailView.vue') },
    { path: '/plants/create', component: () => import('../views/PlantFormView.vue') },
    { path: '/plants/:id/edit', component: () => import('../views/PlantFormView.vue') },
  ],
})

export default router
