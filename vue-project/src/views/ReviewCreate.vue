<template>
  <div style="display: flex;">
    <!-- <h1>감상평 작성</h1> -->
    <form class="review-form" @submit.prevent="reviewCreate">
      <textarea class="review-textarea" name="review_content" id="review_content" placeholder="감상평 작성"
      v-model="review_content"></textarea>
      <div><input class="review-submit" type="submit" value="작성"></div>

    </form>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movie'

const route=useRoute()
const store=useMovieStore()

const review_content=ref(null)


const reviewCreate=function(){
  const payload={
    movie_id: route.params.movie_id,
    review_content: review_content.value,
  }
  store.reviewCreate(payload)
}
</script>

<style scoped>
.review-form{
  margin: 30px;
  display: flex;
  flex-direction: column;
}
.review-textarea{
  width: 500px;
  height: 300px;
  background-color: #111111;
  border: 0px;
  color: white;
  font-family: 'Pretendard';
  font-size: 1.6rem;

}

.review-submit{
  background-color: black;
  border: 0px;
  font-family: 'Pretendard';
  font-size: 1.6rem;
  color: white;
  margin: 10px;
  cursor: pointer;
}

</style>