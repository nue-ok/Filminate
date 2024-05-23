<template>
  <div style="display: flex">
    <div class="bg">
      <p class="nav-logo">FILM<span class="logosub">INATE</span></p>
    </div>
    <div class="login-box">
      <form class="login-form" @submit.prevent="login">
        <div class="name-input-box">
          <input class="name-input" type="text" required
          id="username" v-model.trim="username">
          <label class="name-label">아이디</label>
          <span class="slide"></span>
        </div>
        <div class="name-input-box">
          <input class="name-input" type="password" required
          id="password" v-model.trim="password">
          <label class="name-label">비밀번호</label>
          <span class="slide"></span>
        </div>
        <div class="user-buttons">
          <p @click="router.push({name: 'signup'})" class="signin-btn">회원가입</p>
          <input class="submit-btn" type="submit" value="로그인">
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/account'

const store=useAccountStore()
const router=useRouter()

const username=ref(null)
const password=ref(null)

const login=function(){
  const payload={
    username: username.value,
    password: password.value,
  }
  store.login(payload)
}

</script>

<style scoped>
.nav-logo{
  display: inline-block;
  font-size: 5.0rem;
  font-weight: 800;
  margin: 0px;
  letter-spacing: 3.5rem;
  margin-top: 35%;
  
}
.logosub{
  display: inline-block;
  /* font-size: 2.5rem; */
  font-weight: 100;
  margin: 0px;
  /* letter-spacing: 1.0rem; */
}


.bg{
  background-image: url('../assets/img/login.jpg');
  background-size: cover;
  width:60vw;
  height: 100vh;

  text-align: center;
}

.login-box{
  display: flex;
  width: 40vw;
  justify-content: center;
  align-items: center;
}

.login-form{
  background-color: black;
  display: flex;
  width: 320px;
  flex-direction: column;
  margin-bottom: 10%;
}

.name-input-box {
  margin: 0;
  padding: 0;
  box-sizing: border-box;

  position: relative;
  width: 300px;
  margin-top: 40px;
}

.name-input {
  font-size: 16px;
  color: #ffffff;
  font-family: 'Pretendard';
  font-weight: 300;
  width: 300px;
  border: none;
  border-bottom: solid #8a8a8a 1px;
  padding-bottom: 10px;
  padding-left: 10px;
  padding-right: 10px;
  position: relative;
  background: none;
  z-index: 5;
}

.name-input:focus {
  outline: none;
}

.slide {
  display: block;
  position: absolute;
  bottom: 0;
  left: 0%;
  background-color: #d9d9d9;
  width: 0;
  height: 2px;
  border-radius: 2px;
  transition: 0.5s;
  z-index: 6;
}

.name-label {
  position: absolute;
  font-weight: 300;
  color: #d9d9d9;
  left: 10px;
  font-size: 16px;
  bottom: 8px;
  transition: all .2s;
}

.name-input:focus ~ label, input:valid ~ label {
  font-size: 14px;
  bottom: 40px;
  color: #8a8a8a;
  font-weight: 500;
}

input:focus ~ span, input:valid ~ span {
  width: 320px;
}

.submit-btn{
  font-family: 'Pretendard';
  font-size: 1.6rem;
  font-weight: 300;
  color: #ffffff;
  border: 0px;
  background-color: #00000000;
  padding: 0;
  cursor: pointer;
}

.signin-btn{
  font-size: 1.6rem;
  font-weight: 300;
  margin-right: 20px;
  cursor: pointer;
}

.user-buttons{
  display: flex;
  width: fit-content;
  margin-top: 20px;
  align-self: flex-end;
}
</style>