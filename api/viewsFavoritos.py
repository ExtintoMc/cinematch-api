from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializer import *
from .serializerPost import *
from .models import *

class DirectoresFavoritosView(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return PostDirectoresFavoritosSerializer
        else:
            return DirectoresFavoritosSerializer

    def get_queryset(self):
        user = self.request.query_params.get('id', None)

        if user:
            queryset = DirectoresFavoritos.objects.filter(user=user)
        else:
            queryset = DirectoresFavoritos.objects.all()

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            message = "No se encontraron directores para los criterios de búsqueda proporcionados."
            return Response(data={"detail": message}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class GenerosFavoritosView(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return PostGenerosFavoritosSerializer
        else:
            return GenerosFavoritosSerializer
    
    def get_queryset(self):
        user = self.request.query_params.get('id', None)

        if user:
            queryset = DirectoresFavoritos.objects.filter(user=user)
        else:
            queryset = DirectoresFavoritos.objects.all()

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            message = "No se encontraron directores para los criterios de búsqueda proporcionados."
            return Response(data={"detail": message}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class PeliculasFavoritasView(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return PostPeliculasFavoritasSerializer
        else:
            return PeliculasFavoritasSerializer
       
    def get_queryset(self):
        user = self.request.query_params.get('id', None)

        if user:
            queryset = DirectoresFavoritos.objects.filter(user=user)
        else:
            queryset = DirectoresFavoritos.objects.all()

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            message = "No se encontraron directores para los criterios de búsqueda proporcionados."
            return Response(data={"detail": message}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ProductorasFavoritasView(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return PostProductorasFavoritasSerializer
        else:
            return ProductorasFavoritasSerializer
          
    def get_queryset(self):
        user = self.request.query_params.get('id', None)

        if user:
            queryset = DirectoresFavoritos.objects.filter(user=user)
        else:
            queryset = DirectoresFavoritos.objects.all()

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            message = "No se encontraron directores para los criterios de búsqueda proporcionados."
            return Response(data={"detail": message}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
