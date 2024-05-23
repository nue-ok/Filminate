<template>
  <div v-if="!loading">
    <h1>profileupdate</h1>
    <h1>{{ route.params.username }}</h1>
    <h3>{{ accountStore.userProfile }}</h3>
    <img :src="`${accountStore.userProfile.profile_image}`" alt="">

    <form @submit.prevent="submituser">
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
        <input type="file" id="profile_image" @change="readInputFile">
      </div>

      <input type="submit">
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

</style>