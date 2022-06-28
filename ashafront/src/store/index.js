import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    cart: {
        items: [],
    },
    categories : [],
    isAuthenticated: false,
    token: '',
    isLoading: false
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }

      if (localStorage.getItem('token')) {
          state.token = localStorage.getItem('token')
          state.isAuthenticated = true
      } else {
          state.token = ''
          state.isAuthenticated = false
      } 
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.product.id === item.product.id)
      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
        console.log('exists.length :>> ', exists.length);
      } else {
        state.cart.items.push(item)
      }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    setIsLoading(state, status) {
      state.isLoading = status
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
      state.cart = { items: [] }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    getCategories(state,categories){
      state.categories = categories;
    }
  },
  actions: {
    getCategories({commit}) {
      axios.get("/category/")
          .then(response => {
            let cat = response.data
            console.log('cat :>> ', cat);
              commit('getCategories', cat);
          }).catch(error => {
              console.log(error);
          })},

    getCartItems(){}
  },
  modules: {
  }
})