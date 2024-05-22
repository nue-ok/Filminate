<template>
  <div>
    <!-- {{ comment }} -->
    <div class="comment-profile-box">
      <img class="comment-profile-image" :src="`http://localhost:8000${comment.user.profile_image}`" alt="">
      <p class="comment-username">{{ comment.user.username }}</p>
      <div style="display: flex; align-items: center; margin-left: auto;">
        <p v-if="comment.user.username===accountStore.myName" class="comment-update">수정</p>
        <p @click="store.commentDelete(comment.id)" v-if="comment.user.username===accountStore.myName" class="comment-delete">삭제</p>
        <p class="comment-created">{{ comment.created_at }}</p>
      </div>
    </div>
    <p class="comment-content">{{ comment.comment_content }}</p>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie'
import { useAccountStore } from '@/stores/account'
const accountStore=useAccountStore()
const store=useMovieStore()

const props=defineProps({
  comment: Object,
})


</script>

<style scoped>
.comment-profile-box{
  display: flex;
  align-items: center;
}

.comment-profile-image{
  border-radius: 50%;
  width: 25px;
  height: 25px;
  margin: 0px 10px 0px 0px;
}

.comment-username{

  font-size: 1.4rem;
  font-weight: 400;
  margin-right: 30px;
}

.comment-created{
  font-size: 1.2rem;
  font-weight: 200;
}

.comment-update{
  font-size: 1.3rem;
  font-weight: 400;
  margin-right: 8px;
  cursor: pointer;
}

.comment-delete{
  font-size: 1.3rem;
  font-weight: 400;
  margin-right: 10px;
  cursor: pointer;
}

.comment-content{
  font-size: 1.4rem;
  font-weight: 300;
  margin: 0;
}

</style>