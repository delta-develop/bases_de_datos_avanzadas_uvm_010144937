from django.db import models
from personas.models import Persona
# Create your models here.

class Alumno(models.Model):
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    matricula = models.TextField()
    semestre = models.PositiveIntegerField()
    contacto_emergencia = models.TextField()
    area = models.TextField()

    class Meta:
        db_table = "Alumno"