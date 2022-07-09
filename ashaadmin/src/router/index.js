import { createRouter, createWebHistory } from 'vue-router'
import RouteView from "@/views/RouterView.vue"
import BaseApp from "@/views/BaseApp.vue"

const routes = [
  {
    path: '',
    component: RouteView,
    children:[
      {
        path: "",
        component: BaseApp,
        name:"UserRouteViews",
        children : [
          {
            path: '',
            name: 'home',
            component: () => import('../views/HomeView.vue')
          },
          {
            path: '/product/',
            name: 'product',
            component: () => import('../views/Products.vue')
          },
          {
            path: '/order/',
            name: 'order',
            component: () => import('../views/Orders.vue')
          },
          {
            path: '/point-of-sale/',
            name: 'pos',
            component: () => import('../views/PointOfSale.vue')
          },
        ]
      }
    ]
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
