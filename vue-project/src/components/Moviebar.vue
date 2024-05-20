<template>
<div class="moviebar">
    <div class="moviebar-elements">
      <p class="moviebar-title">test</p>
      <div class="moviebar-movies">
        <Movie class="moviebar-movie" v-for="searchId in 20" :key="searchId" :searchId="searchId"></Movie>
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

</script>

<style scoped>
.moviebar{
  text-align: center;
  margin-top: 200px;
}

.moviebar-movie{
  display: inline-block;
}

.moviebar-elements{
  text-align: left;
  display: inline-block;
}
.moviebar-title{
  text-align: left;
  display: inline-block;
  font-size: 2.2rem;
  font-weight: 500;
  margin-left: 10px;
}
</style>