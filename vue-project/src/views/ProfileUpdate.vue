<template>
  <div>
    <h1>profileupdate</h1>
    <h1>{{ route.params.username }}</h1>

    <form>
      <div>
        <label for="username">username:</label>
          <input type="text" id="username" v-model="username">
      </div>

      <div>
        <label for="email">email:</label>
        <input type="email" id="email" v-model="email">
      </div>

      <div>
        <label for="profile_image">profileimage:</label>
        <input type="file" id="profile_image" @change="handleFileChange">
      </div>
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

onMounted(()=>{
  const payload={
    username: username,
    email: email,
    // profile_image: 'null',
  }
  accountStore.userUpdate(route.params.username, payload).then(()=>{
    loading.value=false
  })
})
</script>

<style scoped>

</style>