<template>
  <div v-if="!loading">
    <p class="main-text" v-if="accountStore.myName===route.params.username">내가 쓴<br>{{accountStore.userComments.length}}개의 댓글</p>
    <p class="main-text" v-else>{{route.params.username}}의<br>{{accountStore.userComments.length}}개의 댓글</p>

    <UserCommentList :comments="accountStore.userComments" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useAccountStore } from '@/stores/account'
import UserCommentList from '@/components/UserCommentList.vue'

const route=useRoute()
const accountStore=useAccountStore()
const loading=ref(true)

onMounted(()=>{
  accountStore.getUserComments(route.params.username).then(()=>{
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