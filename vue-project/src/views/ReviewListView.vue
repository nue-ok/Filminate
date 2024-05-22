<template>
  <div v-if="!loading">
    <div class="review-list">
      <ReviewListCell v-for="i in store.movieDetail.review_set.length" :reviewCnt="i-1" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movie'
import ReviewListCell from '@/components/ReviewListCell.vue'

const route=useRoute()
const store=useMovieStore()
const loading=ref(true)

onMounted(()=>{
  store.getMovieDetail(route.params.movie_id).then(()=>{
    loading.value=false
  })
})
</script>

<style scoped>
.review-list{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, max-content));
  grid-gap: 20px;
  justify-content: center;
  padding: initial;
  margin: 200px 200px 0px 200px;
}
</style>