from django.db import models
from personas.models import Persona
# Create your models here.

class Alumno(Persona):
    matricula = models.TextField()
    semestre = models.PositiveIntegerField()
    contacto_emergencia = models.TextField()
    area = models.TextField()

    class Meta:
        db_table = "Alumnos"