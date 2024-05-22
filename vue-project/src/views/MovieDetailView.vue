<template>
  <MovieDetail/>
  <RecommendMoviebar v-if="!loading" :mainmovie="store.movieDetail"></RecommendMoviebar>
  <ReviewBar/>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import MovieDetail from '@/components/MovieDetail.vue'
import ReviewBar from '@/components/ReviewBar.vue'
import RecommendMoviebar from '@/components/RecommendMoviebar.vue'
import { useMovieStore } from '@/stores/movie'

const route=useRoute()
const store=useMovieStore()
const loading=ref(true)

onMounted(()=>{
  store.getMovies()
  store.getMovieDetail(route.params.movie_id).then(()=>{
    loading.value=false
  })
})
</script>


<style scoped>

</style>