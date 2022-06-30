import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'





require('@/assets/css/main.scss')
axios.defaults.baseURL = 'https://api.asha-world.com/api/v1/'
createApp(App).use(store).use(router,axios).mount('#app')
// require('../css/main.scss');

