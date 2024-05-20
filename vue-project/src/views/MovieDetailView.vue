<template>
  <MovieDetail/>
  <ReviewCell/>
</template>

<script setup>
import { useRoute } from 'vue-router'
import MovieDetail from '@/components/MovieDetail.vue'
import ReviewCell from '@/components/ReviewCell.vue'
const route=useRoute()

</script>

<style scoped>

</style>