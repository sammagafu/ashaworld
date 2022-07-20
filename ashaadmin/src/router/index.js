import {
  createRouter,
  createWebHistory
} from 'vue-router'
import RouteView from "@/views/RouterView.vue"
import BaseApp from "@/views/BaseApp.vue"
import AdminBaseView from "@/views/AdminBaseView"
import Login from "@/views/Login.vue"
import store from '../store'

const routes = [{
    path: '',
    component: RouteView,
    children: [{
        path: "",
        component: BaseApp,
        name: "UserRouteViews",
        meta: {
          requireLogin: true
        },
        children: [{
            path: "",
            name: 'home',
            component: () => import('../views/HomeView.vue')
          },
          {
            path: '/product/',
            name: 'product',
            component: () => import('../views/Products.vue')
          },
          {
            path: '/orders/',
            name: 'order',
            component: () => import('../views/Orders.vue')
          },

          {
            path: "/point-of-sale/",
            component: RouteView,
            children: [
              {
                path: "pos",
                component: () => import('../views/pointofsale/PointOfSale.vue'),
                name: 'Pos'
              },
              {
                path: "order",
                component: () => import('../views/pointofsale/Orders.vue'),
                name: 'PosOrders'
              }, 
              {
                path: "customer",
                component: () => import('../views/pointofsale/Customers.vue'),
                name: 'PosCustomers'
              },
              {
                path: "product",
                component: () => import('../views/pointofsale/Products.vue'),
                name: 'PosProducts',
              }, 
            ]
          },

          {
            path: '/team/',
            name: 'team',
            component: () => import('../views/Teams.vue')
          },

        ]
      },
      {
        path: "/account/",
        name: "AdminRouteViews",
        component: AdminBaseView,
        children: [{
          path: "login/",
          name: "Login",
          component: Login,
        }]
      }
    ]
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/account/login')
  } else {
    next()
  }
})


export default router