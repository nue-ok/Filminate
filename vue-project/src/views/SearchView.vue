<template>
  <div>
    <form class="search-form">
      <div class="name-input-box">
        <input class="name-input" type="text" required
        :value="searchStr" @input="change">
        <label class="name-label">검색</label>
        <span class="slide"></span>
      </div>
    </form>

    <!-- <form>
      <input :value="searchStr" @input="change" type="text">
    </form> -->
    <Moviebar :movieCnt="100"></Moviebar>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue'
import { useMovieStore } from '@/stores/movie'
import Moviebar from '@/components/Moviebar.vue'

const store=useMovieStore()
const searchStr=ref('')

const change = (event) => {
  searchStr.value = event.target.value
  const payload={
    searchStr: searchStr.value,
  }
  store.searchMovies(payload)
}

onMounted (()=>{
  store.getMovieList()
})


</script>

<style scoped>
.search-form{
  display: flex;
  width: 320px;
  flex-direction: column;
  
  margin-left: 50px;
}

.name-input-box {
  margin: 0;
  padding: 0;
  box-sizing: border-box;

  position: relative;
  width: 300px;
  margin-top: 40px;
}
.name-input {
  font-size: 16px;
  color: #ffffff;
  font-family: 'Pretendard';
  font-weight: 300;
  width: 300px;
  border: none;
  border-bottom: solid #8a8a8a 1px;
  padding-bottom: 10px;
  padding-left: 10px;
  padding-right: 10px;
  position: relative;
  background: none;
  z-index: 5;
}

.name-input:focus {
  outline: none;
}

.slide {
  display: block;
  position: absolute;
  bottom: 0;
  left: 0%;
  background-color: #d9d9d9;
  width: 0;
  height: 2px;
  border-radius: 2px;
  transition: 0.5s;
  z-index: 6;
}

.name-label {
  position: absolute;
  font-weight: 300;
  color: #d9d9d9;
  left: 10px;
  font-size: 16px;
  bottom: 8px;
  transition: all .2s;
}

.name-input:focus ~ label, input:valid ~ label {
  font-size: 14px;
  bottom: 40px;
  color: #8a8a8a;
  font-weight: 500;
}

input:focus ~ span, input:valid ~ span {
  width: 320px;
}

.submit-btn{
  font-family: 'Pretendard';
  font-size: 1.6rem;
  font-weight: 300;
  color: #ffffff;
  border: 0px;
  background-color: #00000000;
  padding: 0;
  cursor: pointer;
}

.signin-btn{
  font-size: 1.6rem;
  font-weight: 300;
  margin-right: 20px;
  cursor: pointer;
}

.user-buttons{
  display: flex;
  width: fit-content;
  margin-top: 20px;
  align-self: flex-end;
}
</style>