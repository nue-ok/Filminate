<template>
  <div v-if="!loading">
    <p class="main-text" v-if="accountStore.myName===route.params.username">내가 좋아하는<br>{{movieStore.movies.length}}편의 영화들</p>
    <p class="main-text" v-else>{{route.params.username}}이 좋아하는<br>{{movieStore.movies.length}}편의 영화들</p>
    <div style="margin-bottom: 300px; margin-top: 300px;"><Moviebar :movieCnt="movieStore.movies.length"/></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useAccountStore } from '@/stores/account'
import { useMovieStore } from '@/stores/movie'
import Moviebar from '@/components/Moviebar.vue'

const route=useRoute()
const accountStore=useAccountStore()
const movieStore=useMovieStore()
const loading=ref(true)

onMounted(()=>{
  movieStore.getLikeMovies(route.params.username).then(()=>{
    loading.value=false
  })
})
</script>

<style scoped>
.main-text{
  font-weight: 700;
  font-size: 15rem;
  margin: 0px 20px;
  text-align: end;
}

</style>