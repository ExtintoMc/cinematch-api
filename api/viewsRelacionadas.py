from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializer import *
from .serializerPost import *
from .models import *

class PeliculasActoresView(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'create':
            return PostPeliculasActoresSerializer
        else:
            return PeliculasActoresSerializer
    
    def get_queryset(self):
        pelicula_id = self.request.query_params.get('pelicula_id', None)
        actor_id = self.request.query_params.get('actor_id', None)

        if pelicula_id and actor_id:
            queryset = PeliculasActores.objects.filter(pelicula_id=pelicula_id, actor_id=actor_id)
        elif pelicula_id:
            queryset = PeliculasActores.objects.filter(pelicula_id=pelicula_id)
        elif actor_id:
            queryset = PeliculasActores.objects.filter(actor_id=actor_id)
        else:
            queryset = PeliculasActores.objects.all()

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            message = "No se encontraron directores para los criterios de búsqueda proporcionados."
            return Response(data={"detail": message}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)  

class PeliculasGenerosView(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'create':
            return PostPeliculasGenerosSerializer
        else:
            return PeliculasGenerosSerializer
    
    def get_queryset(self):
        pelicula_id = self.request.query_params.get('pelicula_id', None)
        genero_id = self.request.query_params.get('genero_id', None)

        if pelicula_id and genero_id:
            queryset = PeliculasGeneros.objects.filter(pelicula_id=pelicula_id, genero_id=genero_id)
        elif pelicula_id:
            queryset = PeliculasGeneros.objects.filter(pelicula_id=pelicula_id)
        elif genero_id:
            queryset = PeliculasGeneros.objects.filter(genero_id=genero_id)
        else:
            queryset = PeliculasGeneros.objects.all()

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            message = "No se encontraron directores para los criterios de búsqueda proporcionados."
            return Response(data={"detail": message}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class PeliculasProvedoresView(viewsets.ModelViewSet):
    
    def get_serializer_class(self):
        if self.action == 'create':
            return PostPeliculasProvedoresSerializer
        else:
            return PeliculasProvedoresSerializer

    def get_queryset(self):
        pelicula_id = self.request.query_params.get('pelicula_id', None)
        provedor_id = self.request.query_params.get('provedor_id', None)

        if pelicula_id and provedor_id:
            queryset = PeliculasProvedores.objects.filter(pelicula_id=pelicula_id, provedor_id=provedor_id)
        elif pelicula_id:
            queryset = PeliculasProvedores.objects.filter(pelicula_id=pelicula_id)
        elif provedor_id:
            queryset = PeliculasProvedores.objects.filter(provedor_id=provedor_id)
        else:
            queryset = PeliculasProvedores.objects.all()

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            message = "No se encontraron directores para los criterios de búsqueda proporcionados."
            return Response(data={"detail": message}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class PeliculasProductorasView(viewsets.ModelViewSet):
    serializer_class = PeliculasProductorasSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return PostPeliculasProductorasSerializer
        else:
            return PeliculasProductorasSerializer

    def get_queryset(self):
        pelicula_id = self.request.query_params.get('pelicula_id', None)
        productora_id = self.request.query_params.get('productora_id', None)

        if pelicula_id and productora_id:
            queryset = PeliculasProductoras.objects.filter(pelicula_id=pelicula_id, productora_id=productora_id)
        elif pelicula_id:
            queryset = PeliculasProductoras.objects.filter(pelicula_id=pelicula_id)
        elif productora_id:
            queryset = PeliculasProductoras.objects.filter(productora_id=productora_id)
        else:
            queryset = PeliculasProductoras.objects.all()

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            message = "No se encontraron directores para los criterios de búsqueda proporcionados."
            return Response(data={"detail": message}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class PeliculasDirectoresView(viewsets.ModelViewSet):
    serializer_class = PeliculasDirectoresSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return PostPeliculasDirectoresSerializer
        else:
            return PeliculasDirectoresSerializer

    def get_queryset(self):
        pelicula_id = self.request.query_params.get('pelicula_id', None)
        director_id = self.request.query_params.get('director_id', None)

        if pelicula_id and director_id:
            queryset = PeliculasDirectores.objects.filter(pelicula_id=pelicula_id, director_id=director_id)
        elif pelicula_id:
            queryset = PeliculasDirectores.objects.filter(pelicula_id=pelicula_id)
        elif director_id:
            queryset = PeliculasDirectores.objects.filter(director_id=director_id)
        else:
            queryset = PeliculasDirectores.objects.all()

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            message = "No se encontraron directores para los criterios de búsqueda proporcionados."
            return Response(data={"detail": message}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)