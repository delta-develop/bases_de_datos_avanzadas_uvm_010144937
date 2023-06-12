from personas.models import Persona
from django.db import models
# Create your models here.
class Profesor(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    no_cuenta = models.PositiveIntegerField()
    academia = models.TextField()
    nivel = models.TextField()

    class Meta:
        db_table = "Profesor"