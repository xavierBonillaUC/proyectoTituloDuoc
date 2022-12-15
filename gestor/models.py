from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '. by ' + self.user.username

class Usuarios(models.Model):
    id_usuario = models.IntegerField(11)
    nombre_usuario = models.TextField(max_length=50)
    email = models.EmailField()
    telefono = models.TextField(11)
    username = models.TextField(max_length=50)
    password = models.TextField(max_length=50)
    tipo_nivel = models.TextField()
    estatus = models.TextField()
    registrado_por = models.TextField()

    