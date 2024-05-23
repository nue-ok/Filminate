<template>
  <div class="movie-detail"><MovieDetail/></div>
  <div class="recommend-moviebar"><RecommendMoviebar v-if="!loading" :mainmovie="store.movieDetail"></RecommendMoviebar></div>
  <div class="reviewbar"><ReviewBar/></div>
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
.movie-detail{
  margin-top: 200px;
  margin-bottom: 200px;
}

.recommend-moviebar{
  margin-bottom: 100px;
}

.reviewbar{
  margin-bottom: 300px;
}

</style>