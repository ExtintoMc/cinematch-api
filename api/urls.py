from django.urls import path, include
from rest_framework import routers
from api import views
from api import viewsAuth

router = routers.DefaultRouter()
router.register(r'directores', views.DirectoresView, 'directores')
router.register(r'actores', views.ActoresView, 'actores')
router.register(r'generos', views.GenerosView, 'generos')
router.register(r'provedores', views.ProvedoresView, 'provedores')
router.register(r'productoras', views.ProductorasView, 'productoras')
router.register(r'peliculas', views.PeliculasView, 'peliculas')
router.register(r'rating', views.RatingView, 'rating')
router.register(r'directores_f', views.DirectoresFavoritosView, 'directores_f')
router.register(r'generos_f', views.GenerosFavoritosView, 'generos_f')
router.register(r'peliculas_f', views.PeliculasFavoritasView, 'peliculas_f')
router.register(r'productoras_f', views.ProductorasFavoritasView, 'productoras_f')
router.register(r'peliculas_actores', views.PeliculasActoresView, 'peliculas_actores')
router.register(r'peliculas_generos', views.PeliculasGenerosView, 'peliculas_generos')
router.register(r'peliculas_provedores', views.PeliculasProvedoresView, 'peliculas_provedores')
router.register(r'peliculas_productoras', views.PeliculasProductorasView, 'peliculas_productoras')
router.register(r'peliculas_directores', views.PeliculasDirectoresView, 'peliculas_directores')

urlpatterns = [
    path("v1/", include(router.urls)),
    path('login', viewsAuth.login),
    path('register', viewsAuth.register),
    path('profile', viewsAuth.profile),
]