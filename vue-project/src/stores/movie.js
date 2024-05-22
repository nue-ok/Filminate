import axios from 'axios'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import { useAccountStore } from '@/stores/account.js'

export const useMovieStore = defineStore('movie', () => {
  const accountStore=useAccountStore()
  const router=useRouter()
  const movies=ref([])
  const movieDetail=ref([])
  const reviewDetail=ref()
  const API_URL='http://127.0.0.1:8000'

  const getMovies=function(){
    axios({
      headers: {
        Authorization: `Token ${accountStore.token}`,
      },
      method: 'get',
      url: `${API_URL}/api/movies/`,
    })
    .then((response)=>{
      movies.value=response.data
    })
    .catch((error)=>{
      console.log(error)
    })
  }

  
  const searchMovies=function(payload){
    const searchStr=payload.searchStr
    axios({
      headers: {
        Authorization: `Token ${accountStore.token}`,
      },
      method: 'get',
      url: `${API_URL}/api/movies/search/`,
      params: {
        searchStr: searchStr
      }
    })
    .then((response)=>{
      movies.value=response.data
    })
    .catch((error)=>{
      console.log(error)
    })
  }


  const getMovieDetail=function(movieId){
    axios({
      headers: {
        Authorization: `Token ${accountStore.token}`,
      },
      method: 'get',
      url: `${API_URL}/api/movies/${movieId}/`,
      // params: {
      //   movieId: movieId
      // }
    })
    .then((response)=>{
      movieDetail.value=response.data
    })
    .catch((error)=>{
      console.log(error)
    })
  }

  const reviewCreate=function(payload){
    const movie_id=payload.movie_id
    const review_content=payload.review_content

    axios({
      headers:{
        Authorization: `Token ${accountStore.token}`
      },
      method: 'post',
      url: `${API_URL}/api/reviews/${movie_id}/create/`,
      data: {
        movie_id,
        review_content,
      }
    })
    .then((response)=>{
      router.push({name: 'detail', params: {movie_id: movie_id}})
    })
    .catch((error)=>{
      console.log(error)
    })
  }

  const getReviewDetail=function(reviewId){
    axios({
      headers: {
        Authorization: `Token ${accountStore.token}`,
      },
      method: 'get',
      url: `${API_URL}/api/reviews/${reviewId}/`,
    })
    .then((response)=>{
      console.log(response.data)
      reviewDetail.value=response.data
    })
    .catch((error)=>{
      console.log(error)
    })
  }

  return { movies, API_URL, getMovies, searchMovies, movieDetail, reviewDetail, getMovieDetail, reviewCreate, getReviewDetail }
})
