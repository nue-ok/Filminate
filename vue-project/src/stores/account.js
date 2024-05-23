import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useAccountStore = defineStore('account', () => {
  const router=useRouter()

  const API_URL='http://127.0.0.1:8000'
  const token=ref(null)

  const myName=ref(null)
  const userProfile=ref(null)
  const userReviews=ref(null)
  const userComments=ref(null)
  const errorMsg=ref(null)
  const isLogin=computed(()=>{
    if (token.value===null){
      return false
    } else {
      return true
    }
  })

  const signUp=function(payload){
    const username=payload.username
    const email=payload.email
    const password1=payload.password1
    const password2=payload.password2

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        email,
        password1,
        password2,
      }
    })
    .then((response)=>{
      router.push({name: 'login'})
    })
    .catch((error)=>{
      console.log(error.response.data)

      for (const errors in error.response.data) {
        window.alert(error.response.data[errors])
        break
      }     
    })
  }

  const login=function(payload){
    const username=payload.username
    const password=payload.password

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username,
        password,
      }
    })
    .then((response)=>{
      token.value=response.data.key
      myName.value=payload.username
      router.push({name: 'main'})
    })
    .catch((error)=>{
      console.log(error)
      for (const errors in error.response.data) {
        window.alert(error.response.data[errors])
        break
      }
    })
  }

  const logout=function(){
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
    .then((response)=>{
      token.value=null
      myName.value=null
      router.push({name: 'main'})
    })
    .catch((error)=>{
      console.log(error)
      router.push({name: 'main'})
    })
  }

  const getUser=function(username){
    return axios({
      headers: {
        Authorization: `Token ${token.value}`,
      },
      method: 'get',
      url: `${API_URL}/user/${username}/`,
    })
    .then((response)=>{
      userProfile.value=response.data
    })
    .catch((error)=>{
      console.log(error)
    })
  }

  const getUserReviews=function(username){
    return axios({
      headers: {
        Authorization: `Token ${token.value}`,
      },
      method: 'get',
      url: `${API_URL}/user/${username}/my_reviews/`,
    })
    .then((response)=>{
      userReviews.value=response.data
    })
    .catch((error)=>{
      console.log(error)
    })
  }

  const getUserComments=function(username){
    return axios({
      headers: {
        Authorization: `Token ${token.value}`,
      },
      method: 'get',
      url: `${API_URL}/user/${username}/my_comments/`,
    })
    .then((response)=>{
      userComments.value=response.data
    })
    .catch((error)=>{
      console.log(error)
    })
  }

  const userUpdate=function(user, payload){
    const username=payload.username
    const email=payload.email
    const profile_image=payload.profile_image
    return axios({
      headers: {
        Authorization: `Token ${token.value}`,
        'Content-Type': 'multipart/form-data',
      },
      method: 'put',
      url: `${API_URL}/user/${user}/update/`,
      data: {
        username,
        email,
        profile_image,
      }
    })
    .then((response)=>{
      myName.value=username
      router.push({name: "main"})
    })
    .catch((error)=>{
      console.log(error)
    })
  }


  const getAccount=function(){
    return axios({
      headers: {
        Authorization: `Token ${token.value}`,
      },
      method: 'get',
      url: `${API_URL}/accounts/user/`,
    })
    .then((response)=>{
      userProfile.value=response.data
    })
    .catch((error)=>{
      console.log(error)
    })
  }


  return {
    API_URL,
    token,
    signUp,
    login,
    logout,
    isLogin,
    myName,
    getUser,
    userProfile,
    getUserReviews,
    userReviews,
    getUserComments,
    userComments,
    userUpdate,
    getAccount,
    errorMsg,
  }
}, { persist: true })
