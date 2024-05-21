<template>
<div class="moviebar">
    <div class="moviebar-elements">
      <!-- <p class="moviebar-title">영화 한줄</p> -->
      <div class="moviebar-movies">
        <Movie class="moviebar-movie" v-for="searchId in movieCnt" :key="searchId" :searchId="searchId-1"></Movie>
      </div>
    </div>
</div>
</template>

<script setup>
import { ref, watch, computed } from 'vue'
import { useMovieStore } from '@/stores/movie.js'
import { onMounted } from 'vue'
import Movie from '@/components/Movie.vue'

const store=useMovieStore()

const props=defineProps({
  movieCnt: Number,
})

// onMounted(()=>{
//   store.getMovies()
//   console.log('bbbbb')
// })

</script>

<style scoped>
.moviebar{
  text-align: center;
  margin-top: 200px;
  /* flex-wrap: wrap; */
  /* justify-content: center; */
}

.moviebar-movie{
  /* display: inline-flex;
  flex-wrap: wrap; */
}
.moviebar-movies{
  /* text-align: center; */
  display: inline-flex;
  flex-wrap: wrap;
  justify-content: center;

}

.moviebar-elements{
  text-align: left;
  display: flex;
  justify-content: center;
  margin-left: 140px;
  margin-right: 140px;
}
.moviebar-title{
  text-align: left;
  display: inline-block;
  font-size: 2.2rem;
  font-weight: 500;
  margin-left: 10px;
}
</style>