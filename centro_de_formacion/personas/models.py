from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.TextField()
    apellidos = models.TextField()
    edad = models.PositiveIntegerField()
    curp = models.TextField()

    class Meta:
        db_table = "Persona"


