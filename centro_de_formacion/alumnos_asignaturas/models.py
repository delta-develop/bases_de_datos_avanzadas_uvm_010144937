from django.db import models
from alumnos.models import Alumno
from asignaturas.models import Asignatura
# Create your models here.

class Alumnos_Asignaturas(models.Model):
    profesor = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    class Meta:
        db_table = "alumnos_asignaturas"