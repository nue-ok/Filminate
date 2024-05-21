<template>
  <div class="name-input-box">
    <input class="name-input" type="text" required>
    <label class="name-label">아이디</label>
    <span class="slide"></span>
  </div>
</template>

<script setup>

</script>

<style scoped>
/* .name-input-box {

} */

.name-input-box {
  /* font-family: 'Pretendard'; */
  margin: 0;
  padding: 0;
  box-sizing: border-box;

  position: relative;
  width: 300px;
  /* margin-left: 50px;
  margin-top: 100px; */
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
  left: 0%;  /* right로만 바꿔주면 오 - 왼 */
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
</style>