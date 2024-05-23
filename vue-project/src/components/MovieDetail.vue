<template>
  <p v-if="loading">Loading...</p>
  <div v-else v-if="movie" style="display: flex; justify-content: center; margin-top: 200px;">
    <!-- <h1>{{ store.movieDetail.similars }}</h1> -->
    <img class="movie-detail-poster" :src="`https://image.tmdb.org/t/p/w600_and_h900_bestv2${store.movieDetail.poster_path}`" alt="">
    <div style="display: flex; flex-direction: column;">
      <p class="movie-detail-title">{{ store.movieDetail.movie_title }}</p>

      <p class="movie-detail-genre">{{ store.movieDetail.release_date }},
        <span v-if="store.movieDetail.genre">{{ store.movieDetail.genre[0].genre }}</span>
        <span v-if="store.movieDetail.genre">
          <span v-for="idx in store.movieDetail.genre.length">
            <span v-if="store.movieDetail.genre[idx]">/{{ store.movieDetail.genre[idx].genre }}</span>
          </span>
        </span>,
        {{ store.movieDetail.countries }}</p>

      <p class="movie-detail-time">{{ store.movieDetail.running_time }}분, {{ store.movieDetail.certification }}</p>
      <p class="movie-detail-director">{{ store.movieDetail.director }}</p>
      <p class="movie-detail-cast">
        <span v-if="store.movieDetail.actor">
          {{ store.movieDetail.actor[0].actor_name }}<span v-for="idx in store.movieDetail.actor.length"><span v-if="store.movieDetail.actor[idx]">, {{ store.movieDetail.actor[idx].actor_name }}</span></span>
        </span>
      </p>

      <p style="width: 800px;" class="movie-detail-description">{{ store.movieDetail.description }}</p>
      <p class="movie-detail-cast">좋아요 {{ store.movieDetail.like_count }} / 감상평 {{ store.movieDetail.review_count }}</p>
      <div style="display: flex; margin-top: auto;">
        <p class="movie-detail-button" @click="movieLikeClick(route.params.movie_id)" style="margin-right: 30px;">좋아요</p>
        <p class="movie-detail-button" @click="reviewCreateClick">감상평</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useMovieStore } from '@/stores/movie.js'

const route=useRoute()
const router=useRouter()
const store = useMovieStore()
const loading = ref(false)

const tmp=ref('a')

const movieId=ref(route.params.movie_id-1)
const certStr=ref('')
const movie = computed(() => store.getMovieDetail)

onMounted(async()=>{
  loading.value=true
  try{
    await store.getMovieDetail(route.params.movie_id)
  } catch(error){
    console.error('Error fetching movies:', error)
  } finally {
    loading.value=false
  }
})

const reviewCreateClick=function(){
  router.push({name: 'review_create', params: {movie_id: movie.value.id}})
  window.scrollTo(0, 0)
}

const movieLikeClick=function(movie_id){
  store.movieLike(movie_id)
  router.go()
}

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
  line-height: 140%;
}

.movie-detail-button{
  font-size: 1.6rem;
  margin: 0px 0px 0px 0px;
  cursor: pointer;
}
</style>