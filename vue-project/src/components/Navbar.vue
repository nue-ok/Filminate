<template>
  <nav class="navbar">
    <p class="nav-logo">FILMINATE</p>
    <ul>
      <li class="nav-element">검색하기</li>
      <li class="nav-element">내 정보</li>
    </ul>
    <!-- <p class="nav-logo">FILMINATE</p>
    <p class="nav-element">검색하기</p> -->
  </nav>
</template>

<script setup>

</script>

<style scoped>
.navbar{
  margin-top: 16px;
  padding: 0px 8px;
}
.nav-logo{
  display: inline-block;
  font-size: 1.6rem;
  font-weight: 600;
  margin: 0px;
}
.nav-element{
  font-size: 1.5rem;
  font-weight: 400;
}

nav ul{
  float: right;
  margin: 0;
}

nav li{
  display: inline-block;
  padding-left: 30px;
}
</style>


<!-- 로그인 회원가입 -->
<!-- 로그아웃 마이페이지 검색.... -->