import os
import django
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "filminate.settings")
django.setup()

import movies.models as models


def get_movie(url):
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWY4ZjBjODVhZWE5ZTI2MTcyODM1OGY3N2NjNTkxMSIsInN1YiI6IjY2MzQ1MTY0ZDE4NTcyMDEyMjM0OTZlZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.19-_jBkbFj160vAMKnMM_kJxsNMNLudRf2WVZvAthP4"
    }

    response = requests.get(url, headers=headers)
    response = response.json()

    for res in response.get('results'):  
        if res.get('original_language') in ('en', 'ko', 'ja'):
            detail_id = res.get('id')
            
            # 영화 주연배우, 감독 조회
            peoples = get_people(detail_id)
            
            # 영화 디테일 조회(러닝타임용)
            detail_url = f"https://api.themoviedb.org/3/movie/{detail_id}?language=ko-KR"

            detail_headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWY4ZjBjODVhZWE5ZTI2MTcyODM1OGY3N2NjNTkxMSIsInN1YiI6IjY2MzQ1MTY0ZDE4NTcyMDEyMjM0OTZlZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.19-_jBkbFj160vAMKnMM_kJxsNMNLudRf2WVZvAthP4"
            }

            detail_response = requests.get(detail_url, headers=detail_headers).json()
            # 국가 조회
            try:
                # iso = detail_response.get('production_countries')[0].get('iso_3166_1')
                iso = detail_response.get('origin_country')[0]
            except:
                continue
        
            country_url = "https://api.themoviedb.org/3/configuration/countries?language=ko-KR"

            country_headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWY4ZjBjODVhZWE5ZTI2MTcyODM1OGY3N2NjNTkxMSIsInN1YiI6IjY2MzQ1MTY0ZDE4NTcyMDEyMjM0OTZlZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.19-_jBkbFj160vAMKnMM_kJxsNMNLudRf2WVZvAthP4"
            }

            country_response = requests.get(country_url, headers=country_headers).json()
            
            movie_country = ''
            for country in country_response:
                if country.get('iso_3166_1') == iso:
                    movie_country = country.get('native_name')
                    break
                
            # 개봉일, 상영등급 조회
            release_url = f"https://api.themoviedb.org/3/movie/{detail_id}/release_dates"

            release_headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWY4ZjBjODVhZWE5ZTI2MTcyODM1OGY3N2NjNTkxMSIsInN1YiI6IjY2MzQ1MTY0ZDE4NTcyMDEyMjM0OTZlZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.19-_jBkbFj160vAMKnMM_kJxsNMNLudRf2WVZvAthP4"
            }

            release_response = requests.get(release_url, headers=release_headers).json()
            release_response = release_response.get('results')
            
            certification = 0
            release_date = ''
            is_korea = True
            for release in release_response:
                if release.get('iso_3166_1') == 'KR':
                    info_list = release.get('release_dates')
                    for info in info_list:
                        if info.get('type') == 3:
                            certification = info.get('certification')
                            release_date = info.get('release_date')[:4] # 년도만
                            break
                        if info.get('type') == 4:
                            certification = info.get('certification')
                            release_date = info.get('release_date')[:4] # 년도만
                            break
                    break
            else:
                is_korea = False
            
            # 데이터 없으면 거르기
            if not is_korea or certification == 0 or release_date == '':
                continue
            
            # 상영등급 만들기
            if certification.isdigit(): # 나이만 있으면
                certification = certification + '세 이상 관람가'
            elif certification.lower() != certification: # 영문 포함
                if certification.lower() == 'all':
                    certification = '전체관람가'
                
            # 배우 테이블 데이터추가(중복 X)
            create_actor_tuple(detail_id)
            print(res.get('title'))
            print(detail_response)
            # 영화 테이블 데이터추가(중복 X)
            try:
                if not models.Movie.objects.filter(movie_code=detail_id).exists():
                    movie = models.Movie.objects.create(
                        director=peoples.get('director'), 
                        movie_title=res.get('title'), 
                        description=res.get('overview'), 
                        poster_path=res.get('poster_path'), 
                        running_time=detail_response.get('runtime'), 
                        release_date=release_date,
                        countries=movie_country,
                        certification=certification,
                        movie_code=detail_id
                        )


                    
                    # M:N 추가
                    actors = peoples.get('actors')
                    actors_obj = []
                    for item in actors:
                        actors_obj.append(models.Actor.objects.get(actor_code=item))

                    genres = res.get('genre_ids')
                    genres_obj = []
                    for item in genres:
                        genres_obj.append(models.Genre.objects.get(genre_code=item))
                        
                    movie.genre.add(*genres_obj)
                    movie.actor.add(*actors_obj)
            except:
                print(f'문제있는 놈 -> {detail_id}')
                continue
            

def get_genre():
    url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWY4ZjBjODVhZWE5ZTI2MTcyODM1OGY3N2NjNTkxMSIsInN1YiI6IjY2MzQ1MTY0ZDE4NTcyMDEyMjM0OTZlZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.19-_jBkbFj160vAMKnMM_kJxsNMNLudRf2WVZvAthP4"
    }

    response = requests.get(url, headers=headers).json()

    for res in response.get('genres'):
        models.Genre.objects.create(genre_code=res['id'], genre=res['name'])


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
    
    if len(actors)>=3:
        for i in range(3):
            actor_list.append(actors[i].get('id'))
    else:
        for i in range(len(actors)):
            actor_list.append(actors[i].get('id'))
    
    return {'director': director, 'actors': actor_list}


def create_actor_tuple(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=ko-KR"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZWY4ZjBjODVhZWE5ZTI2MTcyODM1OGY3N2NjNTkxMSIsInN1YiI6IjY2MzQ1MTY0ZDE4NTcyMDEyMjM0OTZlZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.19-_jBkbFj160vAMKnMM_kJxsNMNLudRf2WVZvAthP4"
    }
    
    response = requests.get(url, headers=headers).json()
    actors = response.get('cast')
    
    
    if len(actors)>=3:
        for i in range(3):
            id = actors[i].get('id')
            name = actors[i].get('name')
            
            if not models.Actor.objects.filter(actor_code=id).exists():
                models.Actor.objects.create(actor_name=name, actor_code=id)
    else:
        for i in range(len(actors)):
            id = actors[i].get('id')
            name = actors[i].get('name')
            
            if not models.Actor.objects.filter(actor_code=id).exists():
                models.Actor.objects.create(actor_name=name, actor_code=id)


# get_genre()
# for i in range(1, 14):
#     print(f'kr{i}')
#     get_movie(f'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&page={i}&region=KR&sort_by=popularity.desc&with_origin_country=KR&vote_count.gte=90&vote_average.gte=5')
# # 151
# for i in range(1, 151):
#     print(f'us{i}')
#     get_movie(f'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&page={i}&region=KR&sort_by=popularity.desc&with_origin_country=US&vote_count.gte=90&vote_average.gte=5')

# for i in range(1, 41):
# print(f'jp{i}')
get_movie(f'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&page=5&region=KR&sort_by=popularity.desc&with_origin_country=JP&vote_count.gte=90&vote_average.gte=5')


# for i in range(0, 11):
#     get_movie(f'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&page={i}&region=KR&sort_by=popularity.desc&vote_count.gte=90&vote_average.gte=5')

