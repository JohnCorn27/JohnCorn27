# Generated by Django 3.0 on 2021-08-26 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curso', '0014_auto_20210825_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=2, verbose_name='Nombre de la Categoria')),
                ('Nivel', models.CharField(max_length=100, verbose_name='Nivel de complejidad')),
                ('Descripcion', models.CharField(max_length=100, verbose_name='Descripcion de Categoria')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoria Activada/Categoria Desactivada')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('materia', models.ManyToManyField(to='Curso.Materia')),
            ],
        ),
    ]
