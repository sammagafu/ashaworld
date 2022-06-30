import { createRouter, createWebHistory } from 'vue-router'
import RouteView from "@/views/RouterView.vue"
import BaseAppView from "@/views/BaseAppView.vue"


const routes = [
  {
    path:"",
    component:RouteView,
    children : [
     {
      path: "",
        component: BaseAppView,
        name:"UserRouteViews",
        children: [
          {
            path: '',
            name: 'home',
            component: () => import( /* webpackChunkName: "about" */ '../views/Dashboard.vue')
          },

          {
            path: "/product/",
            component: RouteView,
            children:[
              {
                path:"",
                component: () => import("../views/ProductList.vue"),
                name:"productlist",
              },
              
              {
                path:"",
                component: RouteView,
                children:[
                  // {
                  //   path:"/:category_slug/:product_slug/",
                  //   component: () => import("../views/ProductDetails.vue"),
                  //   name:"ProductDetails"
                  // },

                  // {
                  //   path:"update/",
                  //   component: () => import("../views/ProductUpdate.vue"),
                  //   name:"ProductUpdate"
                  // }
                ]
              },
            ]},

            {
              path: "/orders/",
              component: RouteView,
              children:[
                {
                  path:"",
                  component: () => import("../views/Orders.vue"),
                  name:"orderlist",
                },
                
                {
                  path:"",
                  component: RouteView,
                  children:[
                    // {
                    //   path:"/:category_slug/:product_slug/",
                    //   component: () => import("../views/ProductDetails.vue"),
                    //   name:"ProductDetails"
                    // },
  
                    // {
                    //   path:"update/",
                    //   component: () => import("../views/ProductUpdate.vue"),
                    //   name:"ProductUpdate"
                    // }
                  ]
                },
              ]},

              {
                path: "/customers/",
                component: RouteView,
                children:[
                  {
                    path:"",
                    component: () => import("../views/Customers.vue"),
                    name:"customers",
                  },
                  
                  {
                    path:"",
                    component: RouteView,
                    children:[
                      // {
                      //   path:"/:category_slug/:product_slug/",
                      //   component: () => import("../views/ProductDetails.vue"),
                      //   name:"ProductDetails"
                      // },
    
                      // {
                      //   path:"update/",
                      //   component: () => import("../views/ProductUpdate.vue"),
                      //   name:"ProductUpdate"
                      // }
                    ]
                  },
                ]},

                {
                  path: "/point-of-sale/",
                  component: RouteView,
                  children:[
                    {
                      path:"",
                      component: () => import("../views/Pointofsale.vue"),
                      name:"pos",
                    },
                    
                    {
                      path:"",
                      component: RouteView,
                      children:[
                        // {
                        //   path:"/:category_slug/:product_slug/",
                        //   component: () => import("../views/ProductDetails.vue"),
                        //   name:"ProductDetails"
                        // },
      
                        // {
                        //   path:"update/",
                        //   component: () => import("../views/ProductUpdate.vue"),
                        //   name:"ProductUpdate"
                        // }
                      ]
                    },
                  ]},
          
        ]
     }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
