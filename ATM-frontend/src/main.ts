import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import './styles.css'; // 导入全局样式文件
import axios from 'axios'

axios.defaults.withCredentials=true;

// 创建axios实例
const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000',
  });

createApp(App)
.use(router)
.use(ElementPlus)
.provide("axios",axiosInstance)
.mount('#app')
