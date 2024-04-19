from rest_framework.response import Response
from rest_framework.views import APIView
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from django.db.models import Count
from .models import *
from .serializer import *
import pandas as pd

class rPeliculasView(APIView):
    def get(self, request, user_id):
        
        ratings = Rating.objects.filter(usuario_id=user_id)
        
        if not ratings:
            unique_movies = {}  
            recommended_ids = set()
            popular_movies = Rating.objects.values('pelicula_id').annotate(rating_count=Count('pelicula_id')).order_by('-rating_count')[:10]
            popular_movie_ids = [movie['pelicula_id'] for movie in popular_movies]
            for movie in popular_movie_ids:
                recommended_ids.add(movie)
                recommended_movie = Peliculas.objects.get(id_pelicula=movie)
                serializer = PeliculaSerializer(recommended_movie)
                unique_movies[movie] = serializer.data

            return Response({'recomendaciones': list(unique_movies.values())[:15]})

        ratingsUsuarios = Rating.objects.all().distinct('pelicula_id', 'usuario_id')
        moviesUsers = pd.DataFrame(list(ratingsUsuarios.values('pelicula_id', 'usuario_id', 'rating'))).pivot(index='pelicula_id', columns='usuario_id', values='rating').fillna(0)

        moviesId = []
        for rating_obj in ratings:
            if rating_obj.rating > 5:
                moviesId.append(rating_obj.pelicula_id)

        matMovies = csr_matrix(moviesUsers.values)
        model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=6)
        model.fit(matMovies)

        user_ratings = [rating.pelicula_id for rating in ratings]
        
        def recommender(moviesIds, data, n, user_ratings):
            recommendations = {}
            for movieId in moviesIds:
                movieId = Peliculas.objects.get(id_pelicula=movieId).id_pelicula

                idx = moviesUsers.index.get_loc(movieId)
                distance, indices = model.kneighbors(data[idx], n_neighbors=n)

                recommendations[movieId] = []
                for index, i in enumerate(indices[0]):
                    if i != idx:
                        recommended_movie_id = Peliculas.objects.get(id_pelicula=moviesUsers.index[i]).id_pelicula
                        if recommended_movie_id not in user_ratings:
                            recommendations[movieId].append(recommended_movie_id)
                            if len(recommendations[movieId]) >= n:
                                break

            return recommendations
        
        def get_unique_recommendations(recommendations, user_ratings):
            unique_movies = {}
            recommended_ids = set()
            for movie_id, recommended_movies in recommendations.items():
                for recommended_movie_id in recommended_movies:
                    if recommended_movie_id not in recommended_ids and recommended_movie_id not in user_ratings:
                        recommended_ids.add(recommended_movie_id)
                        recommended_movie = Peliculas.objects.get(id_pelicula=recommended_movie_id)
                        serializer = PeliculaSerializer(recommended_movie)
                        unique_movies[recommended_movie_id] = serializer.data
                        if len(unique_movies) >= 15:
                            return list(unique_movies.values())
            return list(unique_movies.values())
        
        idPeliculasRecommender = recommender(moviesId, matMovies, 10, user_ratings)
        peliculasRecommender = get_unique_recommendations(idPeliculasRecommender, user_ratings)

        return Response({'recomendaciones': peliculasRecommender})

class rPeliculasGenerosView(APIView):
    def get(self, request, user_id):
        genero_deseado = request.query_params.get('genero_id', None)

        ratings = Rating.objects.filter(usuario_id=user_id)
        moviesIdUser = [rating.pelicula_id for rating in ratings]

        if not moviesIdUser:
            genero_count = Rating.objects.filter(pelicula__peliculasgeneros__genero__id_genero=genero_deseado).values('pelicula__peliculasgeneros__genero__nombre').annotate(num_ratings=Count('pelicula_id')).order_by('-num_ratings')

            if genero_count:
                genero_mas_popular = genero_count[0]['pelicula__peliculasgeneros__genero__nombre']

                movies_mas_populares = PeliculasGeneros.objects.filter(genero__nombre=genero_mas_popular).values_list('pelicula_id', flat=True)
                peliculas_mas_populares = Peliculas.objects.filter(id_pelicula__in=movies_mas_populares)[:10]

                serializer = PeliculaSerializer(peliculas_mas_populares, many=True)
                return Response({'recomendaciones': serializer.data[:15]})

        ratingsUsuariosGenero = Rating.objects.filter(pelicula__peliculasgeneros__genero__id_genero=genero_deseado).distinct('pelicula_id', 'usuario_id')
        moviesUsersGenero = pd.DataFrame(list(ratingsUsuariosGenero.values('pelicula_id', 'usuario_id', 'rating')))

        # Eliminar duplicados si existen
        moviesUsersGenero.drop_duplicates(['pelicula_id', 'usuario_id'], inplace=True)

        # Luego, realiza la operación pivot
        moviesUsersGenero = moviesUsersGenero.pivot(index='pelicula_id', columns='usuario_id', values='rating').fillna(0)

        moviesIdsByGenero = []
        for movie_id in moviesIdUser:
            if PeliculasGeneros.objects.filter(pelicula_id=movie_id, genero__id_genero=genero_deseado).exists():
                rating = Rating.objects.get(usuario_id=user_id, pelicula_id=movie_id).rating
                if rating > 5:
                    moviesIdsByGenero.append(movie_id)

        matMovies = csr_matrix(moviesUsersGenero.values)
        model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20)
        model.fit(matMovies)

        user_ratings = [rating.pelicula_id for rating in ratings]

        def recommender(moviesIds, data, n, user_ratings):
            recommendations = {}
            for movieId in moviesIds:
                movieId = Peliculas.objects.get(id_pelicula=movieId).id_pelicula

                idx = moviesUsersGenero.index.get_loc(movieId)
                distance, indices = model.kneighbors(data[idx], n_neighbors=n)

                recommendations[movieId] = []
                for index, i in enumerate(indices[0]):
                    if i != idx:
                        recommended_movie_id = Peliculas.objects.get(id_pelicula=moviesUsersGenero.index[i]).id_pelicula
                        if recommended_movie_id not in user_ratings:
                            recommendations[movieId].append(recommended_movie_id)
                            if len(recommendations[movieId]) >= n:
                                break

            return recommendations

        def get_unique_recommendations(recommendations, user_ratings):
            unique_movies = {}
            recommended_ids = set()
            for movie_id, recommended_movies in recommendations.items():
                for recommended_movie_id in recommended_movies:
                    if recommended_movie_id not in user_ratings and recommended_movie_id not in recommended_ids:
                        recommended_ids.add(recommended_movie_id)
                        recommended_movie = Peliculas.objects.get(id_pelicula=recommended_movie_id)
                        serializer = PeliculaSerializer(recommended_movie)
                        unique_movies[recommended_movie_id] = serializer.data
                        if len(unique_movies) >= 15:
                            return list(unique_movies.values())
            return list(unique_movies.values())

        idPeliculasRecommender = recommender(moviesIdsByGenero, matMovies, 15, user_ratings)
        peliculasRecommender = get_unique_recommendations(idPeliculasRecommender, user_ratings)

        return Response({'recomendaciones': peliculasRecommender[:15]})

class rPeliculasProvedoresView(APIView):
    def get(self, request, user_id):
        provedor_deseado = request.query_params.get('provedor_id', None)

        ratings = Rating.objects.filter(usuario_id=user_id)
        movies_id_user = [rating.pelicula_id for rating in ratings]

        if provedor_deseado is not None:
            provedor_count = Rating.objects.filter(pelicula__peliculasprovedores__provedor__id_provedor=provedor_deseado).values('pelicula__peliculasprovedores__provedor__nombre').annotate(num_ratings=Count('pelicula_id')).order_by('-num_ratings')

            if provedor_count:
                provedor_mas_popular = provedor_count[0]['pelicula__peliculasprovedores__provedor__nombre']

                movies_mas_populares = PeliculasProvedores.objects.filter(provedor__nombre=provedor_mas_popular).values_list('pelicula_id', flat=True)[:10]
                peliculas_mas_populares = Peliculas.objects.filter(id_pelicula__in=movies_mas_populares)

                serializer = PeliculaSerializer(peliculas_mas_populares, many=True)
                return Response({'recomendaciones': serializer.data})

        ratings_usuarios_proveedor = Rating.objects.filter(pelicula__peliculasprovedores__provedor__id_provedor=provedor_deseado)
        movies_users_proveedor = pd.DataFrame(list(ratings_usuarios_proveedor.values('pelicula_id', 'usuario_id', 'rating'))).pivot(index='pelicula_id', columns='usuario_id', values='rating').fillna(0)

        movies_ids_by_proveedor = []
        for movie_id in movies_id_user:
            if PeliculasProvedores.objects.filter(pelicula_id=movie_id, provedor__id_provedor=provedor_deseado).exists():
                rating = Rating.objects.get(usuario_id=user_id, pelicula_id=movie_id).rating
                if rating > 5:
                    movies_ids_by_proveedor.append(movie_id)

        mat_movies = csr_matrix(movies_users_proveedor.values)
        model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=6)
        model.fit(mat_movies)

        user_ratings = [rating.pelicula_id for rating in ratings]

        def recommender(movies_ids, data, n, user_ratings):
            recommendations = {}
            for movie_id in movies_ids:
                movie_id = Peliculas.objects.get(id_pelicula=movie_id).id_pelicula

                idx = movies_users_proveedor.index.get_loc(movie_id)
                distance, indices = model.kneighbors(data[idx], n_neighbors=n)

                recommendations[movie_id] = []
                for index, i in enumerate(indices[0]):
                    if i != idx:
                        recommended_movie_id = Peliculas.objects.get(id_pelicula=movies_users_proveedor.index[i]).id_pelicula
                        if recommended_movie_id not in user_ratings:
                            recommendations[movie_id].append(recommended_movie_id)
                            if len(recommendations[movie_id]) >= n:
                                break

            return recommendations

        def get_unique_recommendations(recommendations, user_ratings):
            unique_movies = []
            recommended_ids = set()
            for movie_id, recommended_movies in recommendations.items():
                for recommended_movie_id in recommended_movies:
                    if recommended_movie_id not in user_ratings and recommended_movie_id not in recommended_ids:
                        recommended_ids.add(recommended_movie_id)
                        recommended_movie = Peliculas.objects.get(id_pelicula=recommended_movie_id)
                        serializer = PeliculaSerializer(recommended_movie)
                        unique_movies.append(serializer.data)
                        if len(unique_movies) >= 15:
                            return unique_movies
            return unique_movies

        id_peliculas_recommender = recommender(movies_ids_by_proveedor, mat_movies, 15, user_ratings)
        peliculas_recommender = get_unique_recommendations(id_peliculas_recommender, user_ratings)

        return Response({'recomendaciones': peliculas_recommender})
class rPeliculasProductorasView(APIView):
    def get(self, request, user_id):
        productora_deseada = request.query_params.get('productora_id', None)
        
        ratings = Rating.objects.filter(usuario_id=user_id)
        movies_id_user = [rating.pelicula_id for rating in ratings]
        
        if not productora_deseada:
            productora_count = Rating.objects.values('pelicula__peliculasproductoras__productora__nombre').annotate(num_ratings=Count('pelicula_id')).order_by('-num_ratings')
            
            if productora_count:
                productora_mas_popular = productora_count[0]['pelicula__peliculasproductoras__productora__nombre']

                movies_mas_populares = PeliculasProductoras.objects.filter(productora__nombre=productora_mas_popular).values_list('pelicula_id', flat=True)
                peliculas_mas_populares = Peliculas.objects.filter(id_pelicula__in=movies_mas_populares)[:10]
                
                serializer = PeliculaSerializer(peliculas_mas_populares, many=True)
                return Response({'recomendaciones': serializer.data[:15]})
        
        ratings_usuarios_productora = Rating.objects.filter(pelicula__peliculasproductoras__productora__id_productora=productora_deseada)
        movies_users_productora = pd.DataFrame(list(ratings_usuarios_productora.values('pelicula_id', 'usuario_id', 'rating'))).pivot(index='pelicula_id', columns='usuario_id', values='rating').fillna(0)

        movies_ids_by_productora = []
        for movie_id in movies_id_user:
            if PeliculasProductoras.objects.filter(pelicula_id=movie_id, productora__id_productora=productora_deseada).exists():
                rating = Rating.objects.get(usuario_id=user_id, pelicula_id=movie_id).rating
                if rating > 5:
                    movies_ids_by_productora.append(movie_id)

        mat_movies = csr_matrix(movies_users_productora.values)
        model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=6)
        model.fit(mat_movies)

        user_ratings = [rating.pelicula_id for rating in ratings]

        def recommender(movies_ids, data, n, user_ratings):
            recommendations = {}
            for movie_id in movies_ids:
                movie_id = Peliculas.objects.get(id_pelicula=movie_id).id_pelicula

                idx = movies_users_productora.index.get_loc(movie_id)
                distance, indices = model.kneighbors(data[idx], n_neighbors=n)

                recommendations[movie_id] = []
                for index, i in enumerate(indices[0]):
                    if i != idx:
                        recommended_movie_id = Peliculas.objects.get(id_pelicula=movies_users_productora.index[i]).id_pelicula
                        if recommended_movie_id not in user_ratings:
                            recommendations[movie_id].append(recommended_movie_id)
                            if len(recommendations[movie_id]) >= n:
                                break

            return recommendations
        
        def get_unique_recommendations(recommendations, user_ratings):
            unique_movies = {}
            recommended_ids = set()
            for movie_id, recommended_movies in recommendations.items():
                for recommended_movie_id in recommended_movies:
                    if recommended_movie_id not in user_ratings and recommended_movie_id not in recommended_ids:
                        recommended_ids.add(recommended_movie_id)
                        recommended_movie = Peliculas.objects.get(id_pelicula=recommended_movie_id)
                        serializer = PeliculaSerializer(recommended_movie)
                        unique_movies[recommended_movie_id] = serializer.data
                        if len(unique_movies) >= 15:
                            return list(unique_movies.values())
            return list(unique_movies.values())
        
        id_peliculas_recommender = recommender(movies_ids_by_productora, mat_movies, 15, user_ratings)
        peliculas_recommender = get_unique_recommendations(id_peliculas_recommender, user_ratings)

        return Response({'recomendaciones': peliculas_recommender[:15]})