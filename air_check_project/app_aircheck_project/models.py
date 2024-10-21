from django.db import models

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key = True)
    name = models.TextField(max_length = 255)
    email = models.TextField(max_length = 255)
    subject = models.TextField(max_length = 255)
    message = models.TextField(max_length = 255)
    