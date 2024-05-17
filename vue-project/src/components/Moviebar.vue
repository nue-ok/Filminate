<template>
<div class="moviebar">
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

    <div
    v-for="movie in store.movies"
    :key="movie.pk">
    <p>{{ movie }}</p>
    </div>
</div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie.js'
import { onMounted } from 'vue';

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
    height: 374.16px;
    margin: 0px 10px;
  }
</style>