import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import SearchView from '@/views/SearchView.vue'
import ReviewCreate from '@/views/ReviewCreate.vue'
import ReviewDetail from '@/views/ReviewDetail.vue'
import ReviewListView from '@/views/ReviewListView.vue'
import ProfileView from '@/views/ProfileView.vue'

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
    {
      path: '/reviews/:movie_id/create/',
      name: 'review_create',
      component: ReviewCreate
    },
    {
      path: '/reviews/:review_id/',
      name: 'review_detail',
      component: ReviewDetail
    },
    {
      path: '/movies/:movie_id/reviews/',
      name: 'review_list',
      component: ReviewListView
    },
    {
      path: '/user/:username/',
      name: 'profile',
      component: ProfileView
    }

  ]
})

export default router
