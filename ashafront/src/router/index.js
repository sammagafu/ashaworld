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
            path: '/become-a-vendor',
            name: 'vendor',
            component: () => import( /* webpackChunkName: "about" */ '../views/BecomeVendor.vue')
          },
          {
            path: '/contact-us',
            name: 'contact',
            component: () => import( /* webpackChunkName: "about" */ '../views/ContactUsPage.vue')
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
            path: '/signup/vendor',
            name: 'vendorSignUp',
            component: () => import( /* webpackChunkName: "about" */ '../views/VendorSignUp.vue')
          },
          {
            path: '/my-account/',
            name: 'UsersAccount',
            component: RouteView,
            meta: {
              requireLogin: true
            },
            children :[
            {
              path:'',
              name: 'my-account',
              component: () => import('../views/myaccount/MyAccount.vue'),
            },
            {
              path: 'wishlist/',
              name: 'wishlist',
              component: () => import('../views/myaccount/WishList.vue'),
            },
            {
              path: 'cart/',
              name: 'cart',
              component: () => import('../views/myaccount/CartItems.vue'),
            },
            {
              path: 'order/',
              name: 'myorders',
              component: () => import('../views/myaccount/MyOrders.vue'),
            },
            ]
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