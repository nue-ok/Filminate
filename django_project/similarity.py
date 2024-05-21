import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
from pathlib import Path
import os
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import natsort

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "filminate.settings")
django.setup()

import movies.models as models


# Read image features
fe = FeatureExtractor()
features = []
img_paths = []
for feature_path in Path("C:/Users/SSAFY/Desktop/find_poster/features").glob("*.npy"):
    features.append(np.load(feature_path))
    img_paths.append(Path("C:/Users/SSAFY/Desktop/find_poster/download_posters") / (feature_path.stem + ".*"))
features = np.array(features)


# Save query image
dirs = 'C:/Users/SSAFY/Desktop/find_poster/download_posters/'
poster_list = natsort.natsorted(os.listdir(dirs))

for poster in poster_list:
    path = os.path.join(dirs, poster)
    img = Image.open(path)  # PIL image

    # Run search
    query = np.array(fe.extract(img))
    query = query.reshape(1, -1)
    dists = []
    for feature in features:
        feature = np.array(feature).reshape(1, -1)
        dists.append(cosine_similarity(feature, query)[0][0])
    # dists = np.linalg.norm(features-query, axis=1)  # L2 distances to features
    ids = np.argsort(dists)[-6:-1]  # Top 5 results
    scores = [(dists[id], img_paths[id]) for id in ids]

    for idx, score in enumerate(scores):
        resultFileName = score[1].__str__()
        resultFileName = resultFileName[:-2].split("\\")[1]
        
        # 유사영화 관계 추가
        movie_pk = int(poster[:-4])
        movie = models.Movie.objects.get(pk=movie_pk)
        
        similar_pk = int(resultFileName)
        similar_movie = models.Movie.objects.get(pk=similar_pk)
        
        movie.similars.add(similar_movie)
        
        print('='*30)
        print(f'score: {score[0]}  imageName: {resultFileName}')
