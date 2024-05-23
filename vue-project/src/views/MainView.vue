<template>
  <div>
    <div class="bg-video">
      <video class="bg-video__content" autoplay muted loop>
        <source src="../assets/video/bg2.mp4" type="video/mp4" />
      </video>
    </div>
    <p class="main-text">당신을 위한</p>
    <p class="main-text">영화 추천</p>
    <div v-if="store.isLogin">
      <div style="margin-top: 400px;" v-if="!loading">
        <div style="margin-bottom: 300px;" v-for="mainmovie in movieStore.movies">
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
.bg-video {
  position: absolute;
  top: 0;
  left: 0;
  height: 70vh;
  width: 100vw;
  z-index: -1;
  opacity: 0.5;
  /* filter: brightness(50%); */
  filter: grayscale(50%);
  
  
}
.bg-video__content {
  height: 100%;
  width: 100%;
  object-fit: cover;
  
}
/* 1rem=10px */
.background{
  background-image: url('../assets/img/loginbg.jpg');
  background-size: cover;
  width: 100vw;
  height: 70vh;
}

.main-text{
  font-weight: 700;
  font-size: 15rem;
  margin: 0px 0px 0px 20px;
}

.bbgg{
  margin: 30px;
  margin-top: 50px;
  width: 95vw;
  height: 200px;
}
</style>