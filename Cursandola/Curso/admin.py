from django.contrib import admin
from .models import Post, Profile, Materia, Tema_General, Categoria, Articulo, pedidos


admin.site.register(Materia)
admin.site.register(Tema_General)
admin.site.register(Categoria)
admin.site.register(Articulo)


# Register your models here.
