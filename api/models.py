from django.db import models
from django.contrib.auth.models import User

# Tablas Unicas

class Directores(models.Model):
    id_director = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100, null=True)
    fecha_nacimiento = models.DateField(max_length=100, null=True)
    biografia = models.CharField(max_length=3500, null=True)
    foto = models.CharField(max_length=255, null=True)

class Actores(models.Model):
    id_actor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100, null=True)
    fecha_nacimiento = models.DateField(max_length=50, null=True)
    biografia = models.CharField(max_length=3500, null=True)
    foto = models.CharField(max_length=255, null=True)
 
class Genero(models.Model):
    id_genero = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)

class Provedores(models.Model):
    id_provedor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    foto = models.CharField(max_length=255, null=True)

class Productoras(models.Model):
    id_productora = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    logo = models.CharField(max_length=250)

class Peliculas(models.Model):
    id_pelicula = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100)
    anno_estreno = models.DateField(max_length=50)
    duracion_minutos = models.IntegerField()
    descripcion = models.CharField(max_length=5000, null=True)
    poster = models.CharField(max_length=255, null=True)
    bg_imagen = models.CharField(max_length=255, null=True)

class Rating(models.Model):
    id_rating = models.AutoField(primary_key=True)
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE, db_column='pelicula_id')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column='usuario_id')
    rating = models.IntegerField()

#Tablas de favoritos

class DirectoresFavoritos(models.Model):
    id_fDirectores = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column='usuario_id')
    director = models.ForeignKey(Directores, on_delete=models.CASCADE, db_column='director_id')

class GenerosFavoritos(models.Model):
    id_fGeneros = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column='usuario_id')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, db_column='genero_id')

class PeliculasFavoritas(models.Model):
    id_fPelicula = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column='usuario_id')
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE, db_column='pelicula_id')

class ProductorasFavoritas(models.Model):
    id_fProductoras = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column='usuario_id')
    productora = models.ForeignKey(Productoras, on_delete=models.CASCADE, db_column='productora_id')

#Tablas relacionadas

class PeliculasActores(models.Model):
    id_pActores = models.AutoField(primary_key=True)
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE, db_column='pelicula_id')
    actor = models.ForeignKey(Actores, on_delete=models.CASCADE, db_column='actor_id')

class PeliculasGeneros(models.Model):
    id_pGeneros = models.AutoField(primary_key=True)
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE, db_column='pelicula_id')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, db_column='genero_id')

class PeliculasProvedores(models.Model):
    id_pProvedores = models.AutoField(primary_key=True)
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE, db_column='pelicula_id')
    provedor = models.ForeignKey(Provedores, on_delete=models.CASCADE, db_column='provedor_id')

class PeliculasProductoras(models.Model):
    id_pProductoras = models.AutoField(primary_key=True)
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE, db_column='pelicula_id')
    productora = models.ForeignKey(Productoras, on_delete=models.CASCADE, db_column='productora_id')

class PeliculasDirectores(models.Model):
    id_pDirectores = models.AutoField(primary_key=True)
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE, db_column='pelicula_id')
    director = models.ForeignKey(Directores, on_delete=models.CASCADE, db_column='director_id')