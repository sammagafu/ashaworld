import { createRouter, createWebHistory } from 'vue-router'
import RouteView from "@/views/RouterView.vue"
import BaseApp from "@/views/BaseApp.vue"
import AdminBaseView from "@/views/AdminBaseView"
import Login from "@/views/Login.vue"

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
          {
            path: '/team/',
            name: 'team',
            component: () => import('../views/Teams.vue')
          },
          {
            path: '/customer/',
            name: 'customer',
            component: () => import('../views/Customers.vue')
          },
        ]
      },
      {
        path:"/account/",
        name:"AdminRouteViews",
        component: AdminBaseView,
        children:[
          {
            path:"login/",
            name:"Login",
            component: Login,
          }
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
