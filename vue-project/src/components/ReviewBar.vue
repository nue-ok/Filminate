<template>

  <div class="review-bar">
    <!-- {{ store.movieDetail.review_set }} -->
    <!-- {{ store.movieDetail.review_set[4] }} -->
    <!-- <div v-for="i in store.movieDetail.review_set.slice(0, 4)">
      {{ i.id }}
    </div> -->
    <ReviewCell v-for="i in 4" :reviewCnt="i-1"></ReviewCell>

  </div>

</template>

<script setup>
import { useMovieStore } from '@/stores/movie'
import ReviewCell from '@/components/ReviewCell.vue'

const store=useMovieStore()
// const props=defineProps({
//   movie_id: String,
// })

</script>

<style scoped>
.review-bar{
  display: flex;
  justify-content: center;
  margin-top: 200px;
}
</style>