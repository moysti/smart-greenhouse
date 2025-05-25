import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios';
import router from "../router/index.js";

axios.interceptors.response.use(
    response => response,
    error => {
        if (error.response.status === 401) {
            router.push('/');
        }
        return Promise.reject(error);
    }
);

const app = createApp(App)

app.use(router)

app.mount('#app')
