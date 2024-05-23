<template>

  <div class="profile-box" v-if="!loading">
    <img class="profile-image" :src="`http://localhost:8000${accountStore.userProfile.profile_image}`" alt="">
    <p class="profile-username">{{ accountStore.userProfile.username }}</p>
    <p v-if="accountStore.myName===accountStore.userProfile.username" class="profile-update" @click="router.push({name: 'profile_update', params: {username: accountStore.userProfile.username}})">회원정보 수정</p>

    <div class="profile-count-box">
      <div @click="router.push({name: 'like_movies', params: {username: route.params.username}})" class="profile-like-box">
        <p class="profile-like-count">{{ accountStore.userProfile.like_movie_count }}</p>
        <p class="profile-like">좋아요</p>
      </div>
      <div @click="router.push({name: 'user_reviews', params: {username: route.params.username}})" class="profile-review-box">
        <p class="profile-review-count">{{ accountStore.userProfile.review_count }}</p>
        <p class="profile-review">감상평</p>
      </div>
      <div @click="router.push({name: 'user_comments', params: {username: route.params.username}})" class="profile-comment-box">
        <p class="profile-comment-count">{{ accountStore.userProfile.comment_count }}</p>
        <p class="profile-comment">댓글</p>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAccountStore  } from '@/stores/account'

const route=useRoute()
const router=useRouter()
const accountStore=useAccountStore()
const loading=ref(true)

onMounted(()=>{
  accountStore.getUser(route.params.username).then(()=>{
    loading.value=false
  })
})
</script>

<style scoped>

.main-text{
  font-weight: 700;
  font-size: 20rem;
  margin: 0px 20px;
}
.profile-box{
  width: fit-content;
  margin: auto;
  margin-top: 150px;
}

.profile-image{
  border-radius: 50%;
  width: 150px;
  height: 150px;
  margin-bottom: 40px;
}

.profile-username{
  font-size: 2.2rem;
  font-weight: 600;
  margin: 0px 0px 10px 0px;
}

.profile-update{
  font-size: 1.4rem;
  font-weight: 300;
  margin: 0px 0px 0px 0px;
  cursor: pointer;
}

.profile-count-box{
  display: flex;
  justify-content: center;
  margin: 70px 0px 0px 0px;
}

.profile-like-box{
  text-align: center;
  width: fit-content;
  margin-right: 150px;
  cursor: pointer;
}

.profile-like-count{
  font-size: 1.6rem;
  font-weight: 700;
  margin: 0px 0px 5px 0px;
}

.profile-like{
  font-size: 1.4rem;
  font-weight: 300;
  margin: 0px 0px 0px 0px;
}

.profile-review-box{
  text-align: center;
  width: fit-content;
  margin-right: 150px;
  cursor: pointer;
}

.profile-review-count{
  font-size: 1.6rem;
  font-weight: 700;
  margin: 0px 0px 5px 0px;
}

.profile-review{
  font-size: 1.4rem;
  font-weight: 300;
  margin: 0px 0px 0px 0px;
}

.profile-comment-box{
  text-align: center;
  width: fit-content;
  cursor: pointer;
}

.profile-comment-count{
  font-size: 1.6rem;
  font-weight: 700;
  margin: 0px 0px 5px 0px;
}

.profile-comment{
  font-size: 1.4rem;
  font-weight: 300;
  margin: 0px 0px 0px 0px;
}

</style>