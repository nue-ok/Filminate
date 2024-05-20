<template>
<!-- <div class="moviebar">
    <div class="moviebar-elements">
      <p class="moviebar-title">이터널 선샤인</p>
      <div class="moviebar-images">
        <img src="../assets/img/eternalsunshine.jpg" alt="">
        <img src="../assets/img/trumanshow.jpg" alt="">
        <img src="../assets/img/her.jpg" alt="">
        <img src="../assets/img/amelie.jpg" alt="">
        <img src="../assets/img/prideprejudice.jpg" alt="">
      </div>
    </div>
</div> -->

<div class="moviebar">
    <div class="moviebar-elements">
      <p class="moviebar-title">test</p>
      <div class="moviebar-movies">
        <div
        v-for="movie in store.movies.slice(2, 7)"
        class="moviebar-movie">
          <img :src="`https://image.tmdb.org/t/p/w600_and_h900_bestv2${movie.poster_path}`" alt="">
          <p class="moviebar-movie-title">{{ movie.movie_title }}</p>
          <p class="moviebar-movie-description">{{ movie.release_date }}, {{ movie.countries }}</p>
        </div>
      </div>
    </div>
</div>

</template>

<script setup>
import { useMovieStore } from '@/stores/movie.js'
import { onMounted } from 'vue'

const store=useMovieStore()

onMounted(()=>{
  store.getMovies()
})
</script>

<style scoped>
  .moviebar{
    text-align: center;
    margin-top: 200px;
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
  img{
    width: 250px;
    height: 375px;
    margin: 0px 10px;
  }

  .moviebar-movie{
    display: inline-block;
  }

  .moviebar-movie-title{
    font-size: 1.6rem;
    font-weight: 300;
    margin: 10px 0px 0px 10px;
  }

  .moviebar-movie-description{
    font-size: 1.4rem;
    font-weight: 200;
    margin: 3px 0px 0px 10px;
  }
</style>