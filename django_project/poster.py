'''
액션
모험
애니메이션
코미디
범죄
다큐멘터리
드라마
가족
판타지
역사
공포
음악
미스터리
로맨스
SF
TV 영화
스릴러
전쟁
서부
'''

import requests
from PIL import Image
from io import BytesIO
import os
import django
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "filminate.settings")
django.setup()

import movies.models as models

url_list = {}
urls = models.Movie.objects.all()
# print(urls)
for url in urls:
    url_list[url.movie_title] = [url.poster_path, url.genre.all()]


idx = 0
for title in url_list.keys():
    # 라벨용 이름
    genre_vector = list('0000000000000000000')
    # 이미지 URL
    image_url = f'http://image.tmdb.org/t/p/w300{url_list[title][0]}'
    
    genres = url_list[title][1]
    for genre in genres:
        genre = genre.genre
        if genre == '액션':
            genre_vector[0] = '1'
        elif genre == '모험':
            genre_vector[1] = '1'
        elif genre == '애니메이션':
            genre_vector[2] = '1'
        elif genre == '코미디':
            genre_vector[3] = '1'
        elif genre == '범죄':
            genre_vector[4] = '1'
        elif genre == '다큐멘터리':
            genre_vector[5] = '1'
        elif genre == '드라마':
            genre_vector[6] = '1'
        elif genre == '가족':
            genre_vector[7] = '1'
        elif genre == '판타지':
            genre_vector[8] = '1'
        elif genre == '역사':
            genre_vector[9] = '1'
        elif genre == '공포':
            genre_vector[10] = '1'
        elif genre == '음악':
            genre_vector[11] = '1'
        elif genre == '미스터리':
            genre_vector[12] = '1'
        elif genre == '로맨스':
            genre_vector[13] = '1'
        elif genre == 'SF':
            genre_vector[14] = '1'
        elif genre == 'TV 영화':
            genre_vector[15] = '1'
        elif genre == '스릴러':
            genre_vector[16] = '1'
        elif genre == '전쟁':
            genre_vector[17] = '1'
        elif genre == '서부':
            genre_vector[18] = '1'
    
    genre_vector = ''.join(genre_vector)
    filename = str(idx) + '_' + genre_vector
    # print(genre_vector)
    
    # HTTP GET 요청을 보내어 이미지를 다운로드
    response = requests.get(image_url)

    # 요청이 성공했는지 확인
    if response.status_code == 200:
        # 이미지 데이터를 바이너리 스트림으로 변환
        image_data = BytesIO(response.content)
        
        # Pillow를 사용하여 이미지 열기
        image = Image.open(image_data)
        
        # title = title.split()
        # title = '_'.join(title)
        # title = title.replace(':', '')
        
        # 이미지 저장 (로컬 경로를 지정)
        # idx_19자리vector.jpg
        label = filename.split('_')[1].split('.')[0]
        image.save(f'C:/Users/JUNG1/OneDrive/바탕 화면/이미지유사도/train/posters/{filename}.jpg')
        print("이미지가 성공적으로 저장되었습니다.")
    else:
        print("이미지를 다운로드하는데 실패했습니다.", response.status_code)
    idx += 1
