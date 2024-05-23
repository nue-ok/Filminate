<template>
  <div>
    <p @click="scrollTop" class="top">TOP</p>
    <Navbar v-if="$route.name !== 'login' && $route.name !== 'signup'" />
    <RouterView :key="$route.fullPath" />
  </div>
  <!-- <footer class="footer" style="text-align: center;">
    <p class="nav-logo button" @click="router.push({name: 'main'})">FILM<span class="logosub">INATE</span></p>
  </footer> -->
</template>

<script setup>
import { RouterView } from 'vue-router'
import Navbar from '@/components/Navbar.vue'

const scrollTop=function(){
  window.scrollTo(0, 0)
}
</script>

<style scoped>
.bg{
  background-color: black;
  top: 0;
  height: 100vh;

}

.top{
  right: 0;
  bottom: 0;
  position: fixed;
  padding: 3px;
  margin: 10px;
  font-size: 1.4rem;
  font-weight: 500;
  cursor: pointer;
}



.nav-logo{
  display: inline-block;
  font-size: 1.8rem;
  font-weight: 800;
  margin: 0px;
  letter-spacing: 1.0rem;
}
.logosub{
  display: inline-block;
  /* font-size: 2.5rem; */
  font-weight: 100;
  margin: 0px;
  /* letter-spacing: 1.0rem; */
}

html, body{height: 100%;}
.wrapper{
  height: auto;
  min-height: 100%;
  padding-bottom: 200px;
}
footer{
  height: 20px;
  position: relative;
  transform: translateY(-100%);
}
</style>