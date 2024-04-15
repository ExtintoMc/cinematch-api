from rest_framework.response import Response
from rest_framework.views import APIView
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from .models import *
from .serializer import *
import pandas as pd

class rPeliculasView(APIView):
    def get(self, request, user_id):
        
        ratings = Rating.objects.filter(usuario_id=user_id)
        ratingsUsuarios = Rating.objects.all()
        moviesUsers = pd.DataFrame(list(ratingsUsuarios.values('pelicula_id', 'usuario_id', 'rating'))).pivot(index='pelicula_id', columns='usuario_id', values='rating').fillna(0)

        moviesId = []
        for rating_obj in ratings:
            if rating_obj.rating > 5:
                moviesId.append(rating_obj.pelicula_id)

        matMovies = csr_matrix(moviesUsers.values)
        model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=6)
        model.fit(matMovies)

        def recommender(moviesIds, data, n):
            recommendations = {}
            for movieId in moviesIds:
                movieId = Peliculas.objects.get(id_pelicula=movieId).id_pelicula

                idx = moviesUsers.index.get_loc(movieId)
                distance, indices = model.kneighbors(data[idx], n_neighbors=n)

                recommendations[movieId] = []
                for index, i in enumerate(indices[0]):
                    if i != idx:
                        recommended_movie_id = Peliculas.objects.get(id_pelicula=moviesUsers.index[i]).id_pelicula
                        recommendations[movieId].append(recommended_movie_id)
                    if i < n:
                        break

            return recommendations
        
        def get_unique_recommendations(recommendations):
            unique_movies = {}  # Utilizamos un diccionario para almacenar los objetos de película únicos
            recommended_ids = set()  # Utilizamos un conjunto para llevar un registro de los IDs de película recomendados
            for movie_id, recommended_movies in recommendations.items():
                for recommended_movie_id in recommended_movies:
                    # Verificamos si el ID de película ya ha sido recomendado
                    if recommended_movie_id not in recommended_ids:
                        recommended_ids.add(recommended_movie_id)  # Agregamos el ID de película al conjunto de IDs recomendados
                        # Obtenemos el objeto Peliculas y lo serializamos
                        recommended_movie = Peliculas.objects.get(id_pelicula=recommended_movie_id)
                        serializer = PeliculaSerializer(recommended_movie)
                        # Agregamos los datos serializados al diccionario de películas únicas
                        unique_movies[recommended_movie_id] = serializer.data
            return list(unique_movies.values())
        
        idPeliculasRecommender = recommender(moviesId, matMovies, 10)
        peliculasRecommender = get_unique_recommendations(idPeliculasRecommender)

        return Response({'recomendaciones': peliculasRecommender})
    

class rPeliculasGenerosView(APIView):
    def get(self, request, user_id):
        
        genero_deseado = request.query_params.get('genero_id', None)
        
        ratings = Rating.objects.filter(usuario_id=user_id)
        moviesIdUser = [rating.pelicula_id for rating in ratings]
        ratingsUsuariosGenero = Rating.objects.filter(pelicula__peliculasgeneros__genero__id_genero=genero_deseado)
        moviesUsersGenero = pd.DataFrame(list(ratingsUsuariosGenero.values('pelicula_id', 'usuario_id', 'rating'))).pivot(index='pelicula_id', columns='usuario_id', values='rating').fillna(0)

        moviesIdsByGenero = []
        for movie_id in moviesIdUser:
            if PeliculasGeneros.objects.filter(pelicula_id=movie_id, genero__id_genero=genero_deseado).exists():
                rating = Rating.objects.get(usuario_id=user_id, pelicula_id=movie_id).rating
                if rating > 5:
                    moviesIdsByGenero.append(movie_id)

        matMovies = csr_matrix(moviesUsersGenero.values)
        model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=6)
        model.fit(matMovies)

        def recommender(moviesIds, data, n):
            recommendations = {}
            for movieId in moviesIds:
                movieId = Peliculas.objects.get(id_pelicula=movieId).id_pelicula

                idx = moviesUsersGenero.index.get_loc(movieId)
                distance, indices = model.kneighbors(data[idx], n_neighbors=n)

                recommendations[movieId] = []
                for index, i in enumerate(indices[0]):
                    if i != idx:
                        recommended_movie_id = Peliculas.objects.get(id_pelicula=moviesUsersGenero.index[i]).id_pelicula
                        recommendations[movieId].append(recommended_movie_id)
                    if i < n:
                        break

            return recommendations
        
        def get_unique_recommendations(recommendations):
            unique_movies = {}  # Utilizamos un diccionario para almacenar los objetos de película únicos
            recommended_ids = set()  # Utilizamos un conjunto para llevar un registro de los IDs de película recomendados
            for movie_id, recommended_movies in recommendations.items():
                for recommended_movie_id in recommended_movies:
                    # Verificamos si el ID de película ya ha sido recomendado
                    if recommended_movie_id not in recommended_ids:
                        recommended_ids.add(recommended_movie_id)  # Agregamos el ID de película al conjunto de IDs recomendados
                        # Obtenemos el objeto Peliculas y lo serializamos
                        recommended_movie = Peliculas.objects.get(id_pelicula=recommended_movie_id)
                        serializer = PeliculaSerializer(recommended_movie)
                        # Agregamos los datos serializados al diccionario de películas únicas
                        unique_movies[recommended_movie_id] = serializer.data
            return list(unique_movies.values())
        
        idPeliculasRecommender = recommender(moviesIdsByGenero, matMovies, 10)
        peliculasRecommender = get_unique_recommendations(idPeliculasRecommender)

        return Response({'recomendaciones': peliculasRecommender})
    