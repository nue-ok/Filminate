<template>
<div class="moviebar">
  <!-- <p class="moviebar-title">{{ mainmovie.movie_title }}</p> -->
    <div class="moviebar-elements">
      <div class="grid"><p class="grid-title">{{ mainmovie.movie_title }}: 추천 영화</p></div>
      <div class="moviebar-movies">
        <RecommendMovie v-if="$route.name !== 'detail'" :poster_path="mainmovie.poster_path" :movie_title="mainmovie.movie_title" :release_date="mainmovie.release_date" :countries="mainmovie.countries" :id="mainmovie.id" />
        <RecommendMovie v-if="$route.name === 'main'" v-for="similar in mainmovie.choice_list" :poster_path="similar.poster_path" :movie_title="similar.movie_title" :release_date="similar.release_date" :countries="similar.countries" :id="similar.id" />
        <RecommendMovie v-else v-for="similar in mainmovie.similars" :poster_path="similar.poster_path" :movie_title="similar.movie_title" :release_date="similar.release_date" :countries="similar.countries" :id="similar.id" />

      </div>
    </div>
</div>
</template>

<script setup>
import { ref, watch, computed } from 'vue'
import { useMovieStore } from '@/stores/movie.js'
import { onMounted } from 'vue'
import RecommendMovie from '@/components/RecommendMovie.vue'

const store=useMovieStore()

const props=defineProps({
  mainmovie: Object,
})


</script>

<style scoped>
.moviebar{
  text-align: center;
}

.moviebar-movie{

}
.moviebar-movies{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, max-content));
  grid-gap: 10px;
  justify-content: center;
  padding: initial;
  margin: 0px 0px 0px 0px;
}
/* .moviebar-movies{
  display: inline-flex;
  flex-wrap: wrap;
  justify-content: center;
} */

.moviebar-elements{
  text-align: left;
  /* display: flex; */
  /* flex-direction: column; */
  /* justify-content: center; */
  margin-left: 140px;
  margin-right: 140px;
}
.moviebar-title{
  text-align: left;
  font-size: 2.2rem;
  font-weight: 500;

  /* margin: 0px, 0px, 0px, 265px; */
}


.grid{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, max-content));
  grid-gap: 10px;
  /* justify-content: center; */
  /* padding: initial; */
  margin: 0px 0px 0px 120px;
}

.grid-title{
  text-align: left;
  font-size: 2.2rem;
  font-weight: 500;
  /* width: 250px; */
  /* overflow: hidden; */
  margin: 0px 0px 10px 0px;
}
</style>