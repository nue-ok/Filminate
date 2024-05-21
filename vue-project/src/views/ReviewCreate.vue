<template>
  <div>
    <h1>Review Create</h1>
    {{ route.params.movie_id }}
    <form @submit.prevent="reviewCreate">
      <textarea name="review_content" id="review_content"
      v-model="review_content"></textarea>
      <input type="submit">
      {{ review_content }}
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movie'

const route=useRoute()
const store=useMovieStore()

const review_content=ref(null)
// id, review_content, created_at, updated_at, movie_id, user_id
const reviewCreate=function(){
  const payload={
    movie_id: route.params.movie_id,
    review_content: review_content.value,
  }
  store.reviewCreate(payload)
}
</script>

<style scoped>

</style>