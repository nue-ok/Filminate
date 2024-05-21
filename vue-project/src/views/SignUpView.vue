<template>
  <div>
    <form class="signup-form" @submit.prevent="signUp">
      <div class="name-input-box">
        <input class="name-input" type="text" required
        id="username" v-model.trim="username">
        <label class="name-label">아이디</label>
        <span class="slide"></span>
      </div>

      <div class="name-input-box">
        <input class="name-input" type="email" required
        id="email" v-model.trim="email">
        <label class="name-label">이메일</label>
        <span class="slide"></span>
      </div>

      <div class="name-input-box">
        <input class="name-input" type="password" required
        id="password1" v-model.trim="password1">
        <label class="name-label">비밀번호</label>
        <span class="slide"></span>
      </div>

      <div class="name-input-box">
        <input class="name-input" type="password" required
        id="password2" v-model.trim="password2">
        <label class="name-label">비밀번호 확인</label>
        <span class="slide"></span>
      </div>
      <input class="submit-btn" type="submit" value="회원가입">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account'

const store=useAccountStore()

const username=ref(null)
const email=ref(null)
const password1=ref(null)
const password2=ref(null)

const signUp=function(){
  const payload={
    username: username.value,
    email: email.value,
    password1: password1.value,
    password2: password2.value,
  }
  store.signUp(payload)
}
</script>

<style scoped>
.signup-form{
  display: flex;
  width: 320px;
  flex-direction: column;
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
  align-self: flex-end;
  margin-top: 20px;
}

</style>