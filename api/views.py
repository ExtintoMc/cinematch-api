from rest_framework import viewsets
from .serializer import *
from .models import *

# Views comunes

class DirectoresView(viewsets.ModelViewSet):
    serializer_class = DirectorSerializer
    queryset = Directores.objects.all()

class ActoresView(viewsets.ModelViewSet):
    serializer_class = ActoresSerializer
    queryset = Actores.objects.all()

class GenerosView(viewsets.ModelViewSet):
    serializer_class = GenerosSerializer
    queryset = Genero.objects.all()

class ProvedoresView(viewsets.ModelViewSet):
    serializer_class = ProvedoresSerializer
    queryset = Provedores.objects.all()

class ProductorasView(viewsets.ModelViewSet):
    serializer_class = ProductorasSerializer
    queryset = Productoras.objects.all()

class PeliculasView(viewsets.ModelViewSet):
    serializer_class = PeliculaSerializer
    queryset = Peliculas.objects.all()

class RatingView(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

#Views de favoritos

class DirectoresFavoritosView(viewsets.ModelViewSet):
    serializer_class = DirectoresFavoritosSerializer
    queryset = DirectoresFavoritos.objects.all()

class GenerosFavoritosView(viewsets.ModelViewSet):
    serializer_class = GenerosFavoritosSerializer
    queryset = GenerosFavoritos.objects.all()

class PeliculasFavoritasView(viewsets.ModelViewSet):
    serializer_class = PeliculasFavoritasSerializer
    queryset = PeliculasFavoritas.objects.all()

class ProductorasFavoritasView(viewsets.ModelViewSet):
    serializer_class = ProductorasFavoritasSerializer
    queryset = ProductorasFavoritas.objects.all()

#Views relacionales

class PeliculasActoresView(viewsets.ModelViewSet):
    serializer_class = PeliculasActoresSerializer
    queryset = PeliculasActores.objects.all()

class PeliculasGenerosView(viewsets.ModelViewSet):
    serializer_class = PeliculasGenerosSerializer
    queryset = PeliculasGeneros.objects.all()

class PeliculasProvedoresView(viewsets.ModelViewSet):
    serializer_class = PeliculasProvedoresSerializer
    queryset = PeliculasProvedores.objects.all()

class PeliculasProductorasView(viewsets.ModelViewSet):
    serializer_class = PeliculasProductorasSerializer
    queryset = PeliculasProductoras.objects.all()

class PeliculasDirectoresView(viewsets.ModelViewSet):
    serializer_class = PeliculasDirectoresSerializer
    queryset = PeliculasDirectores.objects.all()