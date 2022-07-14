import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import '../src/assets/css/asha.css'
import SimpleTypeahead from 'vue3-simple-typeahead';
import 'vue3-simple-typeahead/dist/vue3-simple-typeahead.css'; 
// import 'flowbite';



axios.defaults.baseURL = 'http://localhost:8000/api/v1/'
createApp(App).use(store).use(SimpleTypeahead).use(router,axios).mount('#app')
