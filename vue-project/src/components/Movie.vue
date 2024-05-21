<template>
        <!-- <li class="nav-element button" @click="router.push({name: 'search'})">검색하기</li> -->
  <div>
    <p v-if="loading">Loading...</p>
    <div class="movie-click" v-else v-if="movie" @click="movieClick">
      <!-- {{ movie }} -->
      <img :src="`https://image.tmdb.org/t/p/w600_and_h900_bestv2${movie.poster_path}`" alt="">
      <p class="moviebar-movie-title">{{ movie.movie_title }}</p>
      <p class="moviebar-movie-description">{{ movie.release_date }}, {{ movie.countries }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useMovieStore } from '@/stores/movie.js'
import { useRouter } from 'vue-router'

const router=useRouter()
const store = useMovieStore()
const loading = ref(false)

const props = defineProps({
  searchId: Number,
})

const movie = computed(() => store.movies[props.searchId])

const movieClick=function(){
  router.push({name: 'detail', params: {movie_id: movie.value.id}})
  window.scrollTo(0, 0)
}

</script>

<style scoped>

img{
  width: 250px;
  height: 375px;
  margin: 0px 10px;
}

.moviebar-movie-title{
  font-size: 1.6rem;
  font-weight: 300;
  margin: 10px 0px 0px 10px;
  
  width: 250px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}

.moviebar-movie-description{
  font-size: 1.4rem;
  font-weight: 200;
  margin: 3px 0px 0px 10px;
}

.movie-click{
  cursor: pointer;
  margin-bottom: 100px;
}
</style>