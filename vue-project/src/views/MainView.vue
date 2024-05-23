<template>
  <div>
    <p class="main-text">첫번째 제목</p>
    <p class="main-text">두줄 제목</p>
    <!-- <img class="bbgg" src="../assets/img/hhhh.png" alt=""> -->
    <!-- <Moviebar v-if="store.isLogin" :movieCnt="5"></Moviebar>
    <h1 v-else>로그인하새요</h1> -->
    <div v-if="store.isLogin">
      <div style="margin-top: 300px;" v-if="!loading">
        <div style="margin-bottom: 300px;" v-for="mainmovie in movieStore.movies">
          <!-- <p>{{ mainmovie.movie_title }}</p> -->
          <RecommendMoviebar :mainmovie="mainmovie" />
        </div>
      </div>
    </div>
    <h1 v-else>Login</h1>
  </div>
</template>

<script setup>
import RecommendMoviebar from '@/components/RecommendMoviebar.vue'
import { useAccountStore } from '@/stores/account'
import { useMovieStore } from '@/stores/movie'
import { storeToRefs } from 'pinia'
import { ref, onMounted } from 'vue'
const store=useAccountStore()
const movieStore=useMovieStore()
const loading=ref(true)

onMounted(()=>{
  movieStore.getRecommendations().then(()=>{
    loading.value=false
  })
})
</script>

<style scoped>
/* 1rem=10px */
.main-text{
  font-weight: 700;
  font-size: 15rem;
  margin: 0px 20px;
}

.bbgg{
  margin: 30px;
  margin-top: 50px;
  width: 95vw;
  height: 200px;
}
</style>