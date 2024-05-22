<template>
  <div>
    <h1>mypage</h1>
    <!-- {{ route.params.username }} -->
    <p v-if="!loading">{{ accountStore.userProfile }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useAccountStore  } from '@/stores/account'

const route=useRoute()
const accountStore=useAccountStore()
const loading=ref(true)

onMounted(()=>{
  accountStore.getUser(route.params.username).then(()=>{
    loading.value=false
  })
})
</script>

<style scoped>

</style>