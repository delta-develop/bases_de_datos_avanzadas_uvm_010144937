from personas.models import Persona
from django.db import models
# Create your models here.
class Profesor(Persona):
    no_cuenta = models.PositiveIntegerField()
    academia = models.TextField()
    nivel = models.TextField()

    class Meta:
        db_table = "Profesores"