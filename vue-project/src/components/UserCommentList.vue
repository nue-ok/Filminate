<template>
  <div class="review-list">
    <p v-for="comment in comments">
      <UserCommentListCell :comment="comment" />
    </p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import UserCommentListCell from '@/components/UserCommentListCell.vue'

const props=defineProps({
  comments: Array,
})

</script>

<style scoped>
.review-list{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, max-content));
  grid-gap: 20px;
  justify-content: center;
  padding: initial;
  margin: 200px 200px 0px 200px;
}
</style>