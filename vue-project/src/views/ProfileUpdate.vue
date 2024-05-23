<template>
  <div>
    <h1>profileupdate</h1>
    <h1>{{ route.params.username }}</h1>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useAccountStore } from '@/stores/account'

const route=useRoute()
const accountStore=useAccountStore()
const loading=ref(true)

onMounted(()=>{
  const payload={
    username: 'newname',
    email: 'sadf@gmail.com',
    profile_image: '../assets/img/saewoo.jpg',
  }
  accountStore.userUpdate(route.params.username, payload).then(()=>{
    loading.value=false
  })
})
</script>

<style scoped>

</style>