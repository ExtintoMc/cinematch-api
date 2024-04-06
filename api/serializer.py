from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directores
        fields = '__all__'

class ActoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actores
        fields = '__all__'

class GenerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class ProvedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provedores
        fields = '__all__'

class ProductorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productoras
        fields = '__all__'

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peliculas
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class DirectoresFavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectoresFavoritos
        fields = '__all__'

class GenerosFavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenerosFavoritos
        fields = '__all__'

class PeliculasFavoritasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeliculasFavoritas
        fields = '__all__'

class ProductorasFavoritasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductorasFavoritas
        fields = '__all__'

class PeliculasActoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeliculasActores
        fields = '__all__'

class PeliculasGenerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeliculasGeneros
        fields = '__all__'

class PeliculasProvedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeliculasProvedores
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email', 'password']