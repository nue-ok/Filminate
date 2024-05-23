<template>
  <nav class="navbar">
    <p class="nav-logo button" @click="router.push({name: 'main'})">FILM<span class="logosub">INATE</span></p>
    <ul>
      <li class="nav-element button" @click="router.push({name: 'search'})">검색하기</li>
      <li class="nav-element button" @click="router.push({name: 'profile', params: {username: accountStore.myName}})" v-if="accountStore.isLogin">내 정보</li>
      <li class="nav-element button" @click="router.push({name: 'signup'})" v-if="!accountStore.isLogin">회원가입</li>
      <li class="nav-element button" @click="router.push({name: 'login'})" v-if="!accountStore.isLogin">로그인</li>
      <li class="nav-element button" @click="accountStore.logout" v-if="accountStore.isLogin">로그아웃</li>
    </ul>
    
    <!-- <p class="nav-logo">FILMINATE</p>
    <p class="nav-element">검색하기</p> -->
  </nav>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/account'

const accountStore=useAccountStore()

const router=useRouter()
</script>

<style scoped>
.navbar{
  margin-top: 16px;
  padding: 0px 8px;
}
.nav-logo{
  display: inline-block;
  font-size: 2.8rem;
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
.nav-element{
  font-size: 1.5rem;
  font-weight: 400;
}

nav ul{
  float: right;
  margin: 0;
}

nav li{
  display: inline-block;
  padding-left: 30px;
}

.button{
  cursor: pointer;
}

</style>


<!-- 로그인 회원가입 -->
<!-- 로그아웃 마이페이지 검색.... -->