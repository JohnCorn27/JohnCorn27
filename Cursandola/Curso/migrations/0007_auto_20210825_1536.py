# Generated by Django 3.0 on 2021-08-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curso', '0006_auto_20210825_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.TextField(),
        ),
    ]
