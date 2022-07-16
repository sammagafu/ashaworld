import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import '../src/assets/css/asha.css'
// import 'flowbite';



axios.defaults.baseURL = 'http://localhost:8000/api/v1/'
createApp(App).use(store).use(router,axios).mount('#app')
