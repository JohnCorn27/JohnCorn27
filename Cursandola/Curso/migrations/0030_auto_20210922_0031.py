# Generated by Django 3.0 on 2021-09-22 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Curso', '0029_auto_20210922_0024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulo',
            options={'verbose_name': 'Articulo', 'verbose_name_plural': 'Articulos'},
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
    ]
