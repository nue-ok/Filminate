<template>
  <div>
    <h1>signup</h1>
    
    <form @submit.prevent="signUp">
      <div>
        <label for="username">username: </label>
        <input type="text" id="username"
        v-model.trim="username">
      </div>

      <div>
        <label for="password1">password: </label>
        <input type="password" id="password1"
        v-model.trim="password1">
      </div>

      <div>
        <label for="password2">password confirm: </label>
        <input type="password" id="password2"
        v-model.trim="password2">
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account'

const store=useAccountStore()

const username=ref(null)
const password1=ref(null)
const password2=ref(null)

const signUp=function(){
  const payload={
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  }
  store.signUp(payload)
}
</script>

<style scoped>

</style>