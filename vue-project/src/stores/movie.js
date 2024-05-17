import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useMovieStore = defineStore('movie', () => {
  const movies=ref([])
  const API_URL='http://127.0.0.1:8000'

  const getMovies=function(){
    axios({
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

  return { movies, API_URL, getMovies }
})
