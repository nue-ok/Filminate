import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import SearchView from '@/views/SearchView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/accounts/signup/',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/accounts/login/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/movies/:movie_id/',
      name: 'detail',
      component: MovieDetailView
    },
    {
      path: '/movies/search/',
      name: 'search',
      component: SearchView
    },

  ]
})

export default router
