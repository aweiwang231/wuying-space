import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// --- 我们要加的代码从这里开始 ---
import naive from 'naive-ui'
// --- 我们要加的代码到这里结束 ---

const app = createApp(App)

app.use(router)

// --- 把这一行加在 mount 前面 ---
app.use(naive)
// --- 结束 ---

app.mount('#app')
