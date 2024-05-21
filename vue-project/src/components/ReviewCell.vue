<template>
<div class="review-box">
  <div class="user-profile">
    <img class="profile-image" src="../assets/img/pingu.png" alt="">
    <p class="review-user">이동진 평론가</p>
  </div>
  <div class="review-content-box">
    <p class="review-content">어차피 목뒤로 넘어갈 추억이라면 최대한 입안에서 음미하세요. Wie viel kostet denn der Tisch? Das Bett ist zu klein... Hallo, Wie geht'sihn eneVielen Dank! Wer ist Sie? Das ist Meine Mutter. Ich studiere Geologie an der Pusan National Universitat.</p>
  </div>
  <p class="review-comment">댓글 15</p>
</div>
</template>

<script setup>

</script>

<style scoped>
.review-box{
  display: flex;
  flex-direction: column;
  height: 160px;
  width: 280px;
  margin: 0px 50px 0px 50px;

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