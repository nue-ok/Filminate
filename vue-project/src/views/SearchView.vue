<template>
  <div>
    Search
    <form>
      <input :value="searchStr" @input="change" type="text">
    </form>
    <Moviebar></Moviebar>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useMovieStore } from '@/stores/movie'
import Moviebar from '@/components/Moviebar.vue'

const store=useMovieStore()
const searchStr=ref('')

const change = (event) => {
  searchStr.value = event.target.value;
  const payload={
    searchStr: searchStr.value,
  }
  store.searchMovies(payload)
}
</script>

<style scoped>

</style>