from rest_framework.response import Response
from rest_framework.views import APIView
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from .models import *
import pandas as pd

class rPeliculasView(APIView):
    def get(self, request, user_id):
        # Cargar los datos de películas y calificaciones usando el ORM de Django
        peliculas = Peliculas.objects.all().values('id_pelicula', 'titulo')
        ratings = Rating.objects.filter(id_usuario=user_id).values('id_pelicula', 'rating')

        # Procesamiento de recomendación
        movies_users = pd.DataFrame(list(ratings)).pivot(index='id_pelicula', columns='id_usuario', values='rating').fillna(0)
        user_sorted = ratings.order_by('-rating').values_list('id_pelicula', flat=True)

        movie_names = []
        for movie_id in user_sorted:
            rating = ratings.filter(id_pelicula=movie_id).first()
            if rating.rating > 5:
                movie_name = peliculas.get(id_pelicula=movie_id)['titulo']
                movie_names.append(movie_name)

        mat_movies = csr_matrix(movies_users.values)
        model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20)
        model.fit(mat_movies)

        def recommender(movie_names, data, n):
            unique_recommendations = set()
            for movie_name in movie_names:
                movie_id = peliculas.get(titulo=movie_name)['id_pelicula']
                idx = movies_users.index.get_loc(movie_id)
                distance, indices = model.kneighbors(data[idx], n_neighbors=n)
                for index, i in enumerate(indices[0]):
                    if i != idx:
                        unique_recommendations.add(movies_users.index[i])
            return list(unique_recommendations)[:10]

        recommended_movies = recommender(movie_names, mat_movies, 10)

        # Devuelve las recomendaciones como una respuesta JSON
        return Response({'recomendaciones': recommended_movies})