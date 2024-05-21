<template>
  <div>
    <Navbar/>
    <RouterView :key="$route.fullPath" />
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
import Navbar from '@/components/Navbar.vue'

</script>

<style scoped>
.bg{
  background-color: black;
  height: 100vh;

}
</style>