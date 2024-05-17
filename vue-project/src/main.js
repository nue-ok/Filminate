import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

//fonts
import '@/assets/fontpretendard/pretendard.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
