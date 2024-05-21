<template>
  <MovieDetail/>
  <Moviebar :movieCnt="5"></Moviebar>
  <ReviewBar/>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'
import MovieDetail from '@/components/MovieDetail.vue'
import ReviewBar from '@/components/ReviewBar.vue'
import Moviebar from '@/components/Moviebar.vue'
import { useMovieStore } from '@/stores/movie'

const route=useRoute()
const store=useMovieStore()

onMounted(()=>{
  store.getMovies()
})
</script>


<style scoped>

</style>