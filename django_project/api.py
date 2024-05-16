import os
import django
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "filminate.settings")
django.setup()

import movies.models as models


def get_movie():
    country = 'KR'
    for i in range(1, 6):
        # 쿼리로 검색
        url = f'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&page={i}&region=KR&sort_by=popularity.desc&with_origin_country={country}&vote_count.gte=90&vote_average.gte=5'
        # 상영중 영화
        # url = "https://api.themoviedb.org/3/movie/now_playing?language=ko-KR&page=1&region=KR"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWY4ZjBjODVhZWE5ZTI2MTcyODM1OGY3N2NjNTkxMSIsInN1YiI6IjY2MzQ1MTY0ZDE4NTcyMDEyMjM0OTZlZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.19-_jBkbFj160vAMKnMM_kJxsNMNLudRf2WVZvAthP4"
        }

        response = requests.get(url, headers=headers)
        response = response.json()

        for res in response.get('results'):  
            detail_id = res.get('id')
            
            # 영화 주연배우, 감독 조회
            peoples = get_people(detail_id)
            
            # 영화 디테일 조회(러닝타임용)
            detail_url = f"https://api.themoviedb.org/3/movie/{detail_id}?language=en-US"

            detail_headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWY4ZjBjODVhZWE5ZTI2MTcyODM1OGY3N2NjNTkxMSIsInN1YiI6IjY2MzQ1MTY0ZDE4NTcyMDEyMjM0OTZlZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.19-_jBkbFj160vAMKnMM_kJxsNMNLudRf2WVZvAthP4"
            }

            detail_response = requests.get(detail_url, headers=detail_headers).json()
            
            # 배우 테이블 데이터추가
            create_actor_tuple(detail_id)
            
            # 영화 테이블 데이터추가
            movie = models.Movie.objects.create(
                director=peoples.get('director'), 
                movie_title=res.get('title'), 
                description=res.get('overview'), 
                poster_path=res.get('poster_path'), 
                running_time=detail_response.get('runtime'), 
                release_date=res.get('release_date'), 
                is_adult=res.get('adult')
                )
            
            # M:N 추가
            actors = peoples.get('actors')
            actors_obj = []
            for item in actors:
                actors_obj.append(models.Actor.objects.get(actor_name=item))
    
            genres = res.get('genre_ids')
            genres_obj = []
            for item in genres:
                genres_obj.append(models.Genre.objects.get(genre_code=item))
                
            movie.genre.add(*genres_obj)
            movie.actor.add(*actors_obj)
            

def get_genre():
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWY4ZjBjODVhZWE5ZTI2MTcyODM1OGY3N2NjNTkxMSIsInN1YiI6IjY2MzQ1MTY0ZDE4NTcyMDEyMjM0OTZlZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.19-_jBkbFj160vAMKnMM_kJxsNMNLudRf2WVZvAthP4"
    }

    response = requests.get(url, headers=headers).json()

    for res in response.get('genres'):
        models.Genre.objects.create(code=res['id'], genre=res['name'])


def get_people(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=ko-KR"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWY4ZjBjODVhZWE5ZTI2MTcyODM1OGY3N2NjNTkxMSIsInN1YiI6IjY2MzQ1MTY0ZDE4NTcyMDEyMjM0OTZlZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.19-_jBkbFj160vAMKnMM_kJxsNMNLudRf2WVZvAthP4"
    }
    
    director = ''
    actor_list = []
    
    response = requests.get(url, headers=headers).json()
    directors = response.get('crew')
    actors = response.get('cast')
    
    for people in directors:
        if people.get('job') == 'Director':
            director = people.get('name')
            break
    
    for i in range(3):
        actor_list.append(actors[i].get('name'))
    
    return {'director': director, 'actors': actor_list}


def create_actor_tuple(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=ko-KR"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWY4ZjBjODVhZWE5ZTI2MTcyODM1OGY3N2NjNTkxMSIsInN1YiI6IjY2MzQ1MTY0ZDE4NTcyMDEyMjM0OTZlZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.19-_jBkbFj160vAMKnMM_kJxsNMNLudRf2WVZvAthP4"
    }
    
    response = requests.get(url, headers=headers).json()
    actors = response.get('cast')
    
    for i in range(3):
        id = actors[i].get('id')
        name = actors[i].get('name')
        
        if not models.Actor.objects.filter(actor_code=id).exists():
            models.Actor.objects.create(actor_name=name, actor_code=id)


# get_genre()
get_movie()