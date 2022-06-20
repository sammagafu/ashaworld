import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

axios.defaults.baseURL = 'https://asha-world.com/api/v1/'
createApp(App).use(store).use(router,axios).mount('#app')

// http://localhost:8000/api/v1/category/