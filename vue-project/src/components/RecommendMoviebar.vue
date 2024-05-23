<template>
<div class="moviebar">
    <div class="moviebar-elements">
      <div class="moviebar-movies">
        <RecommendMovie v-if="$route.name !== 'detail'" :poster_path="mainmovie.poster_path" :movie_title="mainmovie.movie_title" :release_date="mainmovie.release_date" :countries="mainmovie.countries" :id="mainmovie.id" />
        <RecommendMovie v-if="$route.name === 'main'" v-for="similar in mainmovie.similars" :poster_path="similar.poster_path" :movie_title="similar.movie_title" :release_date="similar.release_date" :countries="similar.countries" :id="similar.id" />
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
  margin-top: 200px;
  /* flex-wrap: wrap; */
  /* justify-content: center; */
}

.moviebar-movie{
  /* display: inline-flex;
  flex-wrap: wrap; */
}
.moviebar-movies{
  /* text-align: center; */
  display: inline-flex;
  flex-wrap: wrap;
  justify-content: center;

}

.moviebar-elements{
  text-align: left;
  display: flex;
  justify-content: center;
  margin-left: 140px;
  margin-right: 140px;
}
.moviebar-title{
  text-align: left;
  display: inline-block;
  font-size: 2.2rem;
  font-weight: 500;
  margin-left: 10px;
}
</style>