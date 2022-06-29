import {
  createRouter,
  createWebHistory
} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BaseView from "@/views/BaseView.vue"
import RouteView from "@/views/RouteView.vue"
import AdminBaseView from "@/views/AdminBaseView.vue"
import store from '../store'


const routes = [

  {
    path: "",
    component: RouteView,
    children: [

      {
        path: "",
        component: BaseView,
        name:"UserRouteViews",
        children: [

          {
            path: '',
            name: 'home',
            component: HomeView
          },
          {
            path: '/about',
            name: 'about',
            component: () => import( /* webpackChunkName: "about" */ '../views/AboutView.vue')
          },

          {
            path: '/login',
            name: 'login',
            component: () => import( /* webpackChunkName: "about" */ '../views/Login.vue')
          },

          {
            path: '/signup',
            name: 'signup',
            component: () => import( /* webpackChunkName: "about" */ '../views/SignUp.vue')
          },


          {
            path: '/cart',
            name: 'cart',
            component: () => import('../views/CartItems.vue'),
            meta: {
              requireLogin: true
            }

          },

          {
            path: '/my-account',
            name: 'my-account',
            component: () => import('../views/MyAccount.vue'),
            meta: {
              requireLogin: true
            }

          },

          {
            path: '/wishlist',
            name: 'wishlist',
            component: () => import('../views/WishList.vue'),
            meta: {
              requireLogin: true
            }

          },


          {
            path: '/compared',
            name: 'compared',
            component: () => import('../views/CompareProducts.vue')
          },


          {
            path: "/product/",
            component: RouteView,
            children:[
              {
                path:"",
                component: () => import("../views/TheProducts.vue"),
                name:"TheProducts",
              },
              
              {
                path:"",
                component: RouteView,
                children:[
                  {
                    path:"/:category_slug/:product_slug/",
                    component: () => import("../views/ProductDetails.vue"),
                    name:"ProductDetails"
                  },

                  {
                    path:"update/",
                    component: () => import("../views/ProductUpdate.vue"),
                    name:"ProductUpdate"
                  }
                ]
              },
            ]
          },
          {
            path: ":slug/products",
            component: RouteView,
            children:[
              {
                path:"",
                component: () => import("../views/CategoryProductList.vue"),
                name:"CategoryProducts",
              },
            
            ]
          }
        ]
      },

      {
        path:"admins",
        name:"AdminRouteViews",
        meta: { adminOnly: true },
        component: RouteView,
        children:[
          {
            path:"",
            component: AdminBaseView,
            beforeEnter:(to, from) => {
              const user = JSON.parse(localStorage.getItem("ashaUser"))
              console.log("user", user)
              if(to.meta.adminOnly && user.isAdmin){
                return true
              }
              return { path:"", name:"UserRouteViews"}
            },
            children:[
              {
                path:"login",
                name:"AdminLogin",
                component: () => import("../views/UserLogin.vue")
              }
            ]
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

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router