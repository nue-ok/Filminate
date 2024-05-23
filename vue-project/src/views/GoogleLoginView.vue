<template>
    <h1>Google Login</h1>
    <button @click="GoogleLogin">google login</button>
  </template>
  
  <script setup>
  import axios from 'axios';
//   axios.defaults.withCredentials = true;
  const GoogleLogin = function() {
    axios({
        method: 'get',
        // url: 'http://127.0.0.1:8000/user/google/login/'
        url: 'http://127.0.0.1:8000/accounts/google/login/',
        headers: {
        // 'Content-Type': 'application/json',
        'Accept': '*/*',
        }
    }).then((response) => {
        console.log(response)
        // console.log(response.data.key)
    }).catch((error) => {
        console.log(error)
    })
  }
  </script>
  
  <style scoped>
  
  </style>