from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Post(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

class Materia(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la Materia', max_length = 100, null = 2, blank = False)
    Nivel = models.CharField('Nivel de complejidad', max_length=100, null=False, blank=False)
    Descripcion = models.CharField('Descripcion de Materia', max_length=100, null=False, blank=False)
    estado = models.BooleanField('Materia Activada/Materia Desactivada', default= True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add= True)

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

    def __str__(self):
        return self.nombre

class Tema_General(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del Tema General', max_length=100, null=2, blank=False)
    Nivel = models.CharField('Nivel de complejidad', max_length=100, null=False, blank=False)
    Descripcion = models.CharField('Descripcion de Tema General', max_length=100, null=False, blank=False)
    estado = models.BooleanField('Tema General Activada/Tema General Desactivada', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    materia = models.ForeignKey(Materia, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del Articulo', max_length=100, null=2, blank=False)
    link_video = models.URLField('Ingresa Link de Video de Vimeo')
    portada = models.ImageField()
    Descripcion = models.TextField('Descripcion del Articulo', max_length=100, null=False, blank=False)
    estado = models.BooleanField('Articulo Activada/Articulo Desactivada', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    Categoria = models.ForeignKey(Tema_General, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return self.nombre
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoria', max_length=100, null=2, blank=False)
    Descripcion = models.CharField('Descripcion de Tema General', max_length=100, null=False, blank=False)
    estado = models.BooleanField('Tema General Activada/Tema General Desactivada', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    Tema_General = models.ForeignKey(Tema_General, null=True, blank=True, on_delete=models.CASCADE)
    Articulo = models.ForeignKey(Articulo, null=True, blank=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre





class pedidos(models.Model):
    n_pedido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

class articulo_1(models.Model):
    n_articulo = models.CharField(max_length=100)
    seccion = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

class ej_pedidos(models.Model):
    ej_pedido_n = models.CharField(max_length=100)
    ej_direccion_n = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

class ej_articulo(models.Model):
    ej_articulo = models.CharField(max_length=100)
    ej_categoria = models.CharField(max_length=20)
    ej_ciudad = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'