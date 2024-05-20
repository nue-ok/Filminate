<template>
  <div>
    Search
    <form>
      <input v-model="searchStr" type="text">
    </form>
    <p>{{ searchStr }}</p>
    <p>{{ store.movies }}</p>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useMovieStore } from '@/stores/movie'

const store=useMovieStore()
const searchStr=ref('')

watch(searchStr, ()=>{
  // 여기에 장고 얍
  const payload={
    searchStr: searchStr.value,
  }
  store.searchMovies(payload)
})
</script>

<style scoped>

</style>