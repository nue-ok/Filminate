<template>
  <div>
    <h1>ReviewDetail</h1>
    {{ route.params.review_id }}
    <p v-if="loading">loading...</p>
    <p v-else v-if="review">{{ store.reviewDetail }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movie'

const route=useRoute()
const store=useMovieStore()
const loading=ref(false)

const review=computed(()=>store.getReviewDetail)

onMounted(async()=>{
  loading.value=true
  try{
    await store.getReviewDetail(route.params.review_id)
  } catch(error){
    console.error('Error fetching movies:', error)
  } finally {
    loading.value=false
  }
})
</script>

<style scoped>

</style>