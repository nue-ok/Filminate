<template>

  <div class="review-bar">
    <ReviewCell v-for="i in 4"></ReviewCell>
  </div>

</template>

<script setup>
import ReviewCell from '@/components/ReviewCell.vue'

</script>

<style scoped>
.review-bar{
  display: flex;
  justify-content: center;
  margin-top: 200px;
}
</style>