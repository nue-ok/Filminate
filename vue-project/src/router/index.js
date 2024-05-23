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

import GoogleLoginView from '@/views/GoogleLoginView.vue'

import UserLikeMovie from '@/views/UserLikeMovie.vue'
import UserReview from '@/views/UserReview.vue'
import UserComment from '@/views/UserComment.vue'
import ProfileUpdate from '@/views/ProfileUpdate.vue'

import testlogin from '@/views/testlogin.vue'


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
    },
    {
      path: '/google/logintest/',
      name: 'googlelogin',
      component: GoogleLoginView
    },
      path: '/user/:username/like_movies/',
      name: 'like_movies',
      component: UserLikeMovie
    },
    {
      path: '/user/:username/my_reviews/',
      name: 'user_reviews',
      component: UserReview
    },
    {
      path: '/user/:username/my_comments/',
      name: 'user_comments',
      component: UserComment
    },
    {
      path: '/testlogin/',
      name: 'test',
      component: testlogin
    },
    {
      path: '/user/:username/update/',
      name: 'profile_update',
      component: ProfileUpdate
    }
  ]
})

export default router
