<template>
  <div>
    <p v-if="loading">loading...</p>
    <div class="review-detail-box" v-else v-if="store.reviewDetail">
      <div class="review-profile-box">
        <img @click="router.push({name: 'profile', params: {username: store.reviewDetail.user.username}})" class="review-profile-image" :src="`http://localhost:8000${store.reviewDetail.user.profile_image}`" alt="">
        <p class="review-username">{{ store.reviewDetail.user.username }}</p>
        <p class="review-created">{{ store.reviewDetail.created_at }}</p>
      </div>
      <div class="review-content-box">
        <p class="review-movie-title">{{ store.reviewDetail.movie.movie_title }}</p>
        <p class="review-content">{{ store.reviewDetail.review_content }}</p>
      </div>
      <div class="review-comment-menu">
        <p class="review-comment-count">댓글 {{ store.reviewDetail.comment_count }}</p>
        <p @click="hide" class="review-comment-create">댓글 쓰기</p>
        <p v-if="accountStore.myName===store.reviewDetail.user.username" class="review-update">수정</p>
        <p v-if="accountStore.myName===store.reviewDetail.user.username" @click="store.reviewDelete(store.reviewDetail.id)" class="review-delete">삭제</p>
      </div>
      <form @submit.prevent="commentCreate" v-bind:class="hiddenForm">
        <input type="text" v-model="comment_content">
        <input type="submit" value="쓰기">
      </form>
      <div style="margin-top: 80px;">
        <Comment style="margin-bottom: 60px;" v-for="comment in store.reviewDetail.comment_set" :comment="comment" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useMovieStore } from '@/stores/movie'
import { useAccountStore } from '@/stores/account'
import Comment from '@/components/Comment.vue'

const route=useRoute()
const router=useRouter()
const store=useMovieStore()
const accountStore=useAccountStore()
const loading=ref(false)

onMounted(async()=>{
  loading.value=true
  try{
    await store.getReviewDetail(route.params.review_id)
  } catch(error){
    console.error('Error fetching movies:', error)
  } finally {
    loading.value=false
  }
})

const hiddenForm=ref('hidden-form')
const hide=function(){
  if (hiddenForm.value==='hidden-form'){
    hiddenForm.value=''
  } else if (hiddenForm.value===''){
    hiddenForm.value='hidden-form'
  }
}

const comment_content=ref(null)

const commentCreate=function(){
  const payload={
    review_id: route.params.review_id,
    comment_content: comment_content.value,
  }
  store.commentCreate(payload)
}


</script>

<style scoped>
.hidden-form{
  visibility: hidden;
}

.review-detail-box{
  /* display: flex; */
  margin: 200px 500px 0px 500px;
}

.review-profile-box{
  display: flex;
  align-items: center;
  margin-bottom: 30px;
}

.review-profile-image{
  border-radius: 50%;
  width: 30px;
  height: 30px;
  margin: 0px 10px 0px 0px;
  cursor: pointer
}

.review-username{
  font-size: 1.5rem;
  font-weight: 400;
  margin-right: 30px;
}

.review-created{
  font-size: 1.4rem;
  font-weight: 200;
}

.review-content-box{
  display: flex;
  flex-direction: column;
  margin-bottom: 40px;
}

.review-movie-title{
  font-size: 1.4rem;
  font-weight: 200;
  margin: 0px 0px 10px 0px;
}

.review-content{
  font-size: 1.6rem;
  font-weight: 300;
  margin: 0;
}

.review-comment-menu{
  display: flex;
}

.review-comment-count{
  font-size: 1.4rem;
  font-weight: 400;
  margin-right: 20px;
}

.review-comment-create{
  font-size: 1.4rem;
  font-weight: 500;
  cursor: pointer;
  margin-right: 20px;
}

.review-update{
  font-size: 1.4rem;
  font-weight: 500;
  cursor: pointer;
  margin-right: 20px;
}

.review-delete{
  font-size: 1.4rem;
  font-weight: 500;
  cursor: pointer;
}
</style>