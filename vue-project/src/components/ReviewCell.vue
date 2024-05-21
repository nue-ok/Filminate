<template>
<div @click="reviewClick" v-if="store.movieDetail.review_set" class="review-box">
  <div v-if="store.movieDetail.review_set[reviewCnt]">
    <div  class="user-profile">
      <img class="profile-image" src="../assets/img/pingu.png" alt="">
      <p class="review-user">{{ store.movieDetail.review_set[reviewCnt].user }}</p>
    </div>
    <div class="review-content-box">
      <p class="review-content">{{ store.movieDetail.review_set[reviewCnt].review_content }}</p>
      <p class="review-content"></p>
    </div>
    <p class="review-comment">댓글 {{ store.movieDetail.review_set[reviewCnt].comment_count }}</p>
  </div>
</div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useMovieStore } from '@/stores/movie'

const store=useMovieStore()
const router=useRouter()
const loading=ref(false)

const props=defineProps({
  reviewCnt: Number,
})

const reviewClick=function(){
  console.log(store.movieDetail.review_set[props.reviewCnt].id)
  router.push({name: 'review_detail', params: {review_id: store.movieDetail.review_set[props.reviewCnt].id}})
  window.scrollTo(0, 0)
}

// onMounted(async()=>{
//   loading.value=true
//   try{
//     await store.
//   }
// })
</script>

<style scoped>
.review-box{
  display: flex;
  flex-direction: column;
  height: 160px;
  width: 280px;
  margin: 0px 50px 0px 50px;
  cursor: pointer;

}

.user-profile{
  display: flex;
  align-items: center;
}

.profile-image{
  border-radius: 50%;
  width: 30px;
  height: 30px;
  margin: 0px 10px 0px 0px;
}

.review-user{
  font-size: 1.5rem;
  font-weight: 400;
  margin: 0px 0px 0px 0px;
}

.review-content-box{
  width: 280px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  margin: 20px 0px 30px 0px;
}

.review-content{
  font-size: 1.4rem;
  font-weight: 300;
  margin: 0px 0px 0px 0px;
}

.review-comment{
  font-size: 1.3rem;
  font-weight: 200;
  margin: 0px 0px 0px 0px;
  margin-top: auto;
  align-self: flex-end;
}
</style>