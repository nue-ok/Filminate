<template>
  <div>
    <p class="main-text">첫번째 제목</p>
    <p class="main-text">두줄 제목</p>
    <img class="bbgg" src="../assets/img/hhhh.png" alt="">
    <Moviebar v-if="store.isLogin" :movieCnt="5"></Moviebar>
    <h1 v-else>로그인하새요</h1>
  </div>
</template>

<script setup>
import Moviebar from '@/components/Moviebar.vue'
import { useAccountStore } from '@/stores/account';
import { useMovieStore } from '@/stores/movie';
import { storeToRefs } from 'pinia';
import { onMounted } from 'vue';
const store=useAccountStore()
const movieStore=useMovieStore()

onMounted(()=>{
  movieStore.getMovies()
})
</script>

<style scoped>
/* 1rem=10px */
.main-text{
  font-weight: 700;
  font-size: 20rem;
  margin: 0px 20px;
}

.bbgg{
  margin: 30px;
  margin-top: 50px;
  width: 95vw;
  height: 200px;
}
</style>