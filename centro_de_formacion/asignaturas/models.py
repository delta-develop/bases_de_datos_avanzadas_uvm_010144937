from django.db import models

# Create your models here.
class Asignatura(models.Model):
    nombre = models.TextField()
    codigo = models.TextField()
    area = models.TextField()
    departamento = models.TextField()
    creditos = models.FloatField()

    class Meta:
        db_table = "Asignaturas"
