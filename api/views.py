from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializer import *
from .serializerPost import *
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
    def get_serializer_class(self):
        if self.action == 'create':
            return PostRatingSerializer
        else:
            return RatingSerializer
        
    def get_queryset(self):
        usuario_id = self.request.query_params.get('usuario_id', None)
        pelicula_id = self.request.query_params.get('pelicula_id', None)

        if usuario_id:
            queryset = Rating.objects.filter(usuario_id=usuario_id)
        elif pelicula_id:
            queryset = Rating.objects.filter(pelicula_id=pelicula_id)
        elif usuario_id and pelicula_id:
            queryset = Rating.objects.filter(usuario_id=usuario_id, pelicula_id=pelicula_id)
        else:
            queryset = Rating.objects.all()

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            message = "No se encontraron directores para los criterios de búsqueda proporcionados."
            return Response(data={"detail": message}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
