# Generated by Django 5.0.4 on 2024-04-10 01:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actores',
            fields=[
                ('id_actor', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=100, null=True)),
                ('fecha_nacimiento', models.DateField(max_length=50, null=True)),
                ('biografia', models.CharField(max_length=3500, null=True)),
                ('foto', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Directores',
            fields=[
                ('id_director', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=100, null=True)),
                ('fecha_nacimiento', models.DateField(max_length=100, null=True)),
                ('biografia', models.CharField(max_length=3500, null=True)),
                ('foto', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id_pelicula', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('anno_estreno', models.DateField(max_length=50)),
                ('duracion_minutos', models.IntegerField()),
                ('descripcion', models.CharField(max_length=5000, null=True)),
                ('poster', models.CharField(max_length=255, null=True)),
                ('bg_imagen', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productoras',
            fields=[
                ('id_productora', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=50)),
                ('logo', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Provedores',
            fields=[
                ('id_provedor', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DirectoresFavoritos',
            fields=[
                ('id_fDirectores', models.AutoField(primary_key=True, serialize=False)),
                ('director', models.ForeignKey(db_column='director_id', on_delete=django.db.models.deletion.CASCADE, to='api.directores')),
                ('usuario', models.ForeignKey(db_column='usuario_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GenerosFavoritos',
            fields=[
                ('id_fGeneros', models.AutoField(primary_key=True, serialize=False)),
                ('genero', models.ForeignKey(db_column='genero_id', on_delete=django.db.models.deletion.CASCADE, to='api.genero')),
                ('usuario', models.ForeignKey(db_column='usuario_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PeliculasActores',
            fields=[
                ('id_pActores', models.AutoField(primary_key=True, serialize=False)),
                ('actor', models.ForeignKey(db_column='actor_id', on_delete=django.db.models.deletion.CASCADE, to='api.actores')),
                ('pelicula', models.ForeignKey(db_column='pelicula_id', on_delete=django.db.models.deletion.CASCADE, to='api.peliculas')),
            ],
        ),
        migrations.CreateModel(
            name='PeliculasDirectores',
            fields=[
                ('id_pDirectores', models.AutoField(primary_key=True, serialize=False)),
                ('director', models.ForeignKey(db_column='director_id', on_delete=django.db.models.deletion.CASCADE, to='api.directores')),
                ('pelicula', models.ForeignKey(db_column='pelicula_id', on_delete=django.db.models.deletion.CASCADE, to='api.peliculas')),
            ],
        ),
        migrations.CreateModel(
            name='PeliculasFavoritas',
            fields=[
                ('id_fPelicula', models.AutoField(primary_key=True, serialize=False)),
                ('resena', models.CharField(max_length=500)),
                ('pelicula', models.ForeignKey(db_column='pelicula_id', on_delete=django.db.models.deletion.CASCADE, to='api.peliculas')),
                ('usuario', models.ForeignKey(db_column='usuario_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PeliculasGeneros',
            fields=[
                ('id_pGeneros', models.AutoField(primary_key=True, serialize=False)),
                ('genero', models.ForeignKey(db_column='genero_id', on_delete=django.db.models.deletion.CASCADE, to='api.genero')),
                ('pelicula', models.ForeignKey(db_column='pelicula_id', on_delete=django.db.models.deletion.CASCADE, to='api.peliculas')),
            ],
        ),
        migrations.CreateModel(
            name='PeliculasProductoras',
            fields=[
                ('id_pProductoras', models.AutoField(primary_key=True, serialize=False)),
                ('pelicula', models.ForeignKey(db_column='pelicula_id', on_delete=django.db.models.deletion.CASCADE, to='api.peliculas')),
                ('productora', models.ForeignKey(db_column='productora_id', on_delete=django.db.models.deletion.CASCADE, to='api.productoras')),
            ],
        ),
        migrations.CreateModel(
            name='ProductorasFavoritas',
            fields=[
                ('id_fProductoras', models.AutoField(primary_key=True, serialize=False)),
                ('pelicula', models.ForeignKey(db_column='pelicula_id', on_delete=django.db.models.deletion.CASCADE, to='api.peliculas')),
                ('provedor', models.ForeignKey(db_column='provedor_id', on_delete=django.db.models.deletion.CASCADE, to='api.provedores')),
            ],
        ),
        migrations.CreateModel(
            name='PeliculasProvedores',
            fields=[
                ('id_pProvedores', models.AutoField(primary_key=True, serialize=False)),
                ('pelicula', models.ForeignKey(db_column='pelicula_id', on_delete=django.db.models.deletion.CASCADE, to='api.peliculas')),
                ('provedor', models.ForeignKey(db_column='provedor_id', on_delete=django.db.models.deletion.CASCADE, to='api.provedores')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id_rating', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('pelicula', models.ForeignKey(db_column='pelicula_id', on_delete=django.db.models.deletion.CASCADE, to='api.peliculas')),
                ('usuario', models.ForeignKey(db_column='usuario_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
