<template>
  <div>
    <p class="main-text">첫번째 제목</p>
    <p class="main-text">두줄 제목</p>
    <Moviebar/>
  </div>
</template>

<script setup>
import Moviebar from '@/components/Moviebar.vue'

</script>

<style scoped>
/* 1rem=10px */
.main-text{
  font-weight: 700;
  font-size: 20rem;
  margin: 0px 20px;
}
</style>