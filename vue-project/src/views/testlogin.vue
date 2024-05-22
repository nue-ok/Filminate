<template>
  <div v-if="!loading">
    <h1>testpage</h1>
    <h3>{{ store.movies }}</h3>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie'
import { ref, onMounted } from 'vue'

const store=useMovieStore()
const loading=ref(true)

onMounted(()=>{
  store.getRecommendations().then(()=>{
    loading.value=false
  })
})
</script>

<style scoped>

</style>