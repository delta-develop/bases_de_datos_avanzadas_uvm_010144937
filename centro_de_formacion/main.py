import os
import sys

sys.path.append("/Users/leonardohg/Projects/bases_de_datos_avanzadas_uvm_010144937/centro_de_formacion")
os.environ["DJANGO_SETTINGS_MODULE"] = "centro_de_formacion.settings"
import django
django.setup()

from faker import Faker

from alumnos.models import Alumno
from personas.models import Persona
from profesores.models import Profesor
from asignaturas.models import Asignatura
from alumnos_asignaturas.models import Alumnos_Asignaturas
from profesores_asignaturas.models import Profesores_Asignaturas
from random import randint

fake = Faker("es_MX")
areas = [
    "Fisico-Matemáticas",
    "Médico-Biológicas",
    "Sociales-Administrativas"
]

materias = [
    "Matematicas",
    "Fisica",
    "Ciencias sociales",
    "Biologia",
    "Lenguas",
    "Taller tecnico"
]

personas = [
    Persona.objects.create(
        nombre=fake.first_name(),
        apellidos=fake.last_name(),
        edad=randint(12,75),
        curp=fake.curp()
    ) for _ in range(15)
]

alumnos = [
    Alumno.objects.create(
        persona=personas[n],
        matricula=str(randint(100000,999999)),
        semestre=randint(1,12),
        contacto_emergencia = "datos contacto",
        area=areas[randint(0,2)]
    ) for n in range(10)
]

profesores = [
    Profesor.objects.create(
        persona=personas[n],
        no_cuenta=randint(10000,999999),
        academia=areas[randint(0,2)],
        nivel=randint(1,7)
    ) for n in range(10,15)
]

asignaturas = [
    Asignatura.objects.create(
        nombre=f"{materias[randint(0,5)]} {randint(1,5)}",
        codigo=f"{n}_ASGN",
        area=areas[randint(0,2)],
        departamento=f"Depto {n}",
        creditos=randint(3,12)
    ) for n in range(10)
]

for alumno in alumnos:
    Alumnos_Asignaturas.objects.create(
        alumno=alumno,
        asignatura=asignaturas[randint(1,10)]
    )

for profesor in profesores:
    Profesores_Asignaturas.objects.create(
        profesor=profesor,
        asignatura=asignaturas[randint(1,10)]
    )

