import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
// import store from './store'
//import echarts from 'echarts'
import { vLoading } from 'element-plus/es/components/loading/src/directive';

const app=createApp(App)
// app.use(store).use(router).mount('#app')
app.use(router).mount('#app')
app.directive('load',vLoading)
//Vue.prototype.$echarts=echarts
