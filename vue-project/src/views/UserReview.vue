<template>
  <div v-if="!loading">
    <p class="main-text" v-if="accountStore.myName===route.params.username">내가 쓴<br>{{accountStore.userReviews.length}}편의 감상평</p>
    <p class="main-text" v-else>{{route.params.username}}의<br>{{accountStore.userReviews.length}}편의 감상평</p>

    <UserReviewList :reviews="accountStore.userReviews" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useAccountStore } from '@/stores/account'
import UserReviewList from '@/components/UserReviewList.vue'

const route=useRoute()
const accountStore=useAccountStore()
const loading=ref(true)

onMounted(()=>{
  accountStore.getUserReviews(route.params.username).then(()=>{
    loading.value=false
  })
})
</script>

<style scoped>
.main-text{
  font-weight: 700;
  font-size: 15rem;
  margin: 0px 20px;
  text-align: end;
}
</style>