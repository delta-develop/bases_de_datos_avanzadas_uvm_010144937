from django.db import models
from alumnos.models import Alumno
from asignaturas.models import Asignatura
# Create your models here.

class Alumnos_Asignaturas(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    def __str__(self):
        value = f"Alumno: {self.alumno.persona.nombre} {self.alumno.persona.apellidos}  Materia: {self.asignatura.nombre}"
        return value
    
    class Meta:
        db_table = "alumnos_asignaturas"