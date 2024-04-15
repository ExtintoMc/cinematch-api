from django.urls import path, include
from rest_framework import routers
from api import views
from api import viewsAuth
from api import viewsFavoritos
from api import viewsRelacionadas
from api import viewsRecomendaciones

router = routers.DefaultRouter()
router.register(r'directores', views.DirectoresView, 'directores')
router.register(r'actores', views.ActoresView, 'actores')
router.register(r'generos', views.GenerosView, 'generos')
router.register(r'provedores', views.ProvedoresView, 'provedores')
router.register(r'productoras', views.ProductorasView, 'productoras')
router.register(r'peliculas', views.PeliculasView, 'peliculas')
router.register(r'rating', views.RatingView, 'rating')
router.register(r'directores_f', viewsFavoritos.DirectoresFavoritosView, 'directores_f')
router.register(r'generos_f', viewsFavoritos.GenerosFavoritosView, 'generos_f')
router.register(r'peliculas_f', viewsFavoritos.PeliculasFavoritasView, 'peliculas_f')
router.register(r'productoras_f', viewsFavoritos.ProductorasFavoritasView, 'productoras_f')
router.register(r'peliculas_actores', viewsRelacionadas.PeliculasActoresView, 'peliculas_actores')
router.register(r'peliculas_generos', viewsRelacionadas.PeliculasGenerosView, 'peliculas_generos')
router.register(r'peliculas_provedores', viewsRelacionadas.PeliculasProvedoresView, 'peliculas_provedores')
router.register(r'peliculas_productoras', viewsRelacionadas.PeliculasProductorasView, 'peliculas_productoras')
router.register(r'peliculas_directores', viewsRelacionadas.PeliculasDirectoresView, 'peliculas_directores')

urlpatterns = [
    path("v1/", include(router.urls)),
    path('login', viewsAuth.login),
    path('register', viewsAuth.register),
    path('profile', viewsAuth.profile),
    path('recomendaciones/<int:user_id>/', viewsRecomendaciones.rPeliculasView.as_view(), name='recomendaciones'),
    path('recomendacionesByGenero/<int:user_id>/', viewsRecomendaciones.rPeliculasGenerosView.as_view(), name='recomendacionesByGenero'),
    path('recomendacionesByProvedores/<int:user_id>/', viewsRecomendaciones.rPeliculasProvedoresView.as_view(), name='recomendacionesByProvedores'),
    path('recomendacionesByProductoras/<int:user_id>/', viewsRecomendaciones.rPeliculasProductorasView.as_view(), name='recomendacionesByProductoras'),

]