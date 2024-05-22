<template>


<div style="">
  <div class="review-bar">
    <ReviewCell v-for="i in 4" :reviewCnt="i-1"></ReviewCell>
  </div>
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
/* .review-bar{
  display: flex;
  flex-wrap: wrap;
} */

.review-bar {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, max-content));
  grid-gap: 20px;
  justify-content: center;
  padding: initial;
}
</style>