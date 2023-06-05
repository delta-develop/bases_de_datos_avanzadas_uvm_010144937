from django.db import models
from profesores.models import Profesor
from asignaturas.models import Asignatura
# Create your models here.

class Profesores_Asignaturas(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    class Meta:
        db_table = "profesores_asignaturas"
