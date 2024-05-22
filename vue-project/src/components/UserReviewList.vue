<template>
  <div class="review-list">
    <p v-for="review in reviews">
      <UserReviewListCell :review="review" />
    </p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import UserReviewListCell from '@/components/UserReviewListCell.vue'

const props=defineProps({
  reviews: Array,
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