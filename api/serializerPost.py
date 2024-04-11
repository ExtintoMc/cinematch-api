from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class PostRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'

class PostDirectoresFavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectoresFavoritos
        fields = '__all__'

class PostGenerosFavoritosSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenerosFavoritos
        fields = '__all__'

class PostPeliculasFavoritasSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeliculasFavoritas
        fields = '__all__'

class PostProductorasFavoritasSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductorasFavoritas
        fields = '__all__'


class PostPeliculasActoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeliculasActores
        fields = '__all__'

class PostPeliculasGenerosSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeliculasGeneros
        fields = '__all__'

class PostPeliculasProvedoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeliculasProvedores
        fields = '__all__'

class PostPeliculasProductorasSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeliculasProductoras
        fields = '__all__'

class PostPeliculasDirectoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeliculasDirectores
        fields = '__all__'