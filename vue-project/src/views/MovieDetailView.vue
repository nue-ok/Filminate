<template>
  <div style="display: flex; justify-content: center; margin-top: 200px;">
    <img class="movie-detail-poster" src="../assets/img/eternalsunshine.jpg" alt="">
    <div style="display: flex; flex-direction: column;">
      <p class="movie-detail-title">이터널 선샤인</p>
      <p class="movie-detail-genre">2005, SF/드라마/로맨스, 미국</p>
      <p class="movie-detail-time">1시간 48분, 15세 이용가</p>
      <p class="movie-detail-director">미셸 공드리</p>
      <p class="movie-detail-cast">짐 캐리, 케이트 윈슬렛</p>
      <p style="width: 800px;" class="movie-detail-description">조엘은 아픈 기억만을 지워준다는 라쿠나사를 찾아가 헤어진 연인 클레멘타인의 기억을 지우기로 결심한다. 기억이 사라져 갈수록 조엘은 사랑이 시작되던 순간, 행복한 기억들, 가슴 속에 각인된 추억들을 지우기 싫어지기만 하는데... 당신을 지우면 이 아픔도 사라질까요? 사랑은 그렇게 다시 기억된다.</p>
      <p class="movie-detail-cast">● 357 / ☆ 
        125</p>

      <div style="display: flex; margin-top: auto;">
        <p class="movie-detail-button" style="margin-right: 30px;">내 목록에 담기</p>
        <p class="movie-detail-button">후기 남기기</p>
      </div>

    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route=useRoute()

// const movieid=route.params.movie_id
</script>

<style scoped>
.movie-detail-poster{
  width: 300px;
  height: 450px;
  margin-right: 35px;
}
.movie-detail-title{
  font-size: 3.2rem;
  font-weight: 700;
  margin: 0px 0px 20px 0px;
}

.movie-detail-genre{
  font-size: 1.6rem;
  font-weight: 500;
  margin: 0px 0px 5px 0px;
}
.movie-detail-time{
  font-size: 1.4rem;
  font-weight: 400;
  margin: 0px 0px 35px 0px;
}
.movie-detail-director{
  font-size: 1.4rem;
  font-weight: 500;
  margin: 0px 0px 5px 0px;
}
.movie-detail-cast{
  font-size: 1.4rem;
  font-weight: 400;
  margin: 0px 0px 45px 0px;
}
.movie-detail-description{
  font-size: 1.6rem;
  font-weight: 300;
  margin: 0px 0px 50px 0px;
}

.movie-detail-button{
  font-size: 1.6rem;
  margin: 0px 0px 0px 0px;
}
</style>