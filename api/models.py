from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Directores(models.Model):
    id_director = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(max_length=100)
    biografia = models.CharField(max_length=3500)
    foto = models.CharField(max_length=255)

class Actores(models.Model):
    id_actor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(max_length=50)
    biografia = models.CharField(max_length=1500)
    foto = models.CharField(max_length=255)
 
class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

class Provedores(models.Model):
    id_provedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    foto = models.CharField(max_length=255)

class Productoras(models.Model):
    id_productora = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    logo = models.CharField(max_length=250)

class Peliculas(models.Model):
    id_pelicula = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    anno_estreno = models.IntegerField()
    duracion_minutos = models.IntegerField()
    descripcion = models.CharField(max_length=5000)
    titulo = models.CharField(max_length=3500)
    director = models.ForeignKey(Directores, on_delete=models.CASCADE, db_column='director_id')
    productora = models.ForeignKey(Productoras, on_delete=models.CASCADE, db_column='productora_id')
    poster = models.CharField(max_length=255)
    bg_imagen = models.CharField(max_length=255)

class Rating(models.Model):
    id_rating = models.AutoField(primary_key=True)
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE, db_column='pelicula_id')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column='usuario_id')
    rating = models.IntegerField()

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
    resena = models.CharField(max_length=500)

class ProductorasFavoritas(models.Model):
    id_fProductoras = models.AutoField(primary_key=True)
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE, db_column='pelicula_id')
    provedor = models.ForeignKey(Provedores, on_delete=models.CASCADE, db_column='provedor_id')

class PeliculasActores(models.Model):
    id_pActores = models.AutoField(primary_key=True)
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE, db_column='pelicula_id')
    actores = models.ForeignKey(Actores, on_delete=models.CASCADE, db_column='actor_id')

class PeliculasGeneros(models.Model):
    id_pGeneros = models.AutoField(primary_key=True)
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE, db_column='pelicula_id')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, db_column='genero_id')

class PeliculasProvedores(models.Model):
    id_pProvedores = models.AutoField(primary_key=True)
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE, db_column='pelicula_id')
    provedor = models.ForeignKey(Provedores, on_delete=models.CASCADE, db_column='provedor_id')