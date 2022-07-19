import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    compared: {
        items: [],
    },
    cartItems : [],
    categories : [],
    isAuthenticated: false,
    token: '',
    user: {
      id: 0,
      email: ''
    },
    isLoading: false
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.email = localStorage.getItem('email')
        state.user.id = localStorage.getItem('userid')
        // state.team.name = localStorage.getItem('team_name')
        // state.team.id = localStorage.getItem('team_id')
        // state.team.plan = localStorage.getItem('team_plan')
        // state.team.max_leads = localStorage.getItem('team_max_leads')
        // state.team.max_clients = localStorage.getItem('team_max_clients')
      } else {
        state.token = ''
        state.isAuthenticated = false
        state.user.id = 0
        state.user.username = ''
        // state.team.id = 0
        // state.team.name = ''
        // state.team.plan = ''
        // state.team.max_leads = 0
        // state.team.max_clients = 0
      }
    },
    addToCompare(state, item) {
      console.log('item :>> ', item);
      state.compared.items.push(item)

      // const exists = state.cart.items.filter(i => i.product.id === item.product.id)
      // if (exists.length) {
      //   console.log('"exists" :>> ', "exists");
      // } else {
      //   state.compared.items.push(item)
      // }

      localStorage.setItem('compared', JSON.stringify(item))
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },

    setUser(state, user) {
      state.user = user
    },

    setToken(state, token) {
        state.token = token
        state.isAuthenticated = true
    },  
    removeToken(state) {
        state.token = ''
        state.isAuthenticated = false
    },
    clearCart(state) {
      state.cartItems = { items: [] }
      localStorage.removeItem('cart')
    },
    getCategories(state,categories){
      state.categories = categories;
    },
    getCartItems(state,cartItems){
      state.cartItems = cartItems;
    }
  },
  actions: {
    getCategories({commit}) {
      axios.get("/category/")
          .then(response => {
            let cat = response.data
              commit('getCategories', cat);
          }).catch(error => {
              console.log(error);
          })},

    getCartItems({commit}){
      const token = localStorage.getItem('token')
      axios.get("/cart/",{ headers: {"Authorization" : `Token ${token}`} })
          .then(response => {
            let cart = response.data
              commit('getCartItems', cart);
          }).catch(error => {
              console.log(error);
          })
    },
  },
  modules: {
  }
})