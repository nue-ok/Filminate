<template>
  <div class="profile-box" v-if="!loading">
    <img :src="`${accountStore.userProfile.profile_image}`" alt="">
    <form class="login-form" @submit.prevent="submituser">
      <div class="name-input-box">
        <input class="name-input" required type="text" id="username" v-model="username">
        <label class="name-label" for="username">아이디</label>
        <span class="slide"></span>
      </div>

      <div class="name-input-box">
        <input class="name-input" type="email" id="email" v-model="email">
        <label class="name-label" for="email">이메일</label>
        <span class="slide"></span>
      </div>

      <div class="name-input-box">
        <input class="name-input" type="file" id="profile_image" @change="readInputFile">
        <label class="name-label file-upload" for="profile_image">프로필 사진</label>
        <span class="slide"></span>
      </div>

      <input class="submit-btn" type="submit" value="수정">
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useAccountStore } from '@/stores/account'

const route=useRoute()
const accountStore=useAccountStore()
const loading=ref(true)

const username=ref(null)
const email=ref(null)
const profile_image=ref(null)

const readInputFile=function(file){
  profile_image.value=file.target.files[0]
}

onMounted(()=>{
  accountStore.getAccount().then(()=>{
    loading.value=false
    username.value=accountStore.userProfile.username
    email.value=accountStore.userProfile.email
  })
})

const submituser=function(){
  const payload={
    username: username.value,
    email: email.value,
    profile_image: profile_image.value,
  }
  accountStore.userUpdate(route.params.username, payload)
}
</script>

<style scoped>
.profile-box{
  margin: auto;
  margin-top: 150px;
  width: fit-content;
}

img{
  border-radius: 50%;
  width: 200px;
  height: 200px;
  margin-bottom: 20px;
}

.login-form{
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
  width: fit-content;
  margin-left: auto;
  margin-top: 20px;
}

input[type=file]::file-selector-button{
  background-color: black;
  border: 0px;
  color: white;
  font-family: 'Pretendard';
  font-weight: 700;
  cursor: pointer;
}
</style>