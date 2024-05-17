<template>
  <div>
    <h1>login</h1>

    <form @submit.prevent="login">
      <div>
        <label for="username">username: </label>
        <input type="text" id="username"
        v-model.trim="username">
      </div>
      <div>
        <label for="password">password: </label>
        <input type="password" id="password"
        v-model.trim="password">
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

</style>