# Generated by Django 4.2.1 on 2023-06-05 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("alumnos", "0001_initial"),
        ("asignaturas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Alumnos_Asignaturas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "asignatura",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="asignaturas.asignatura",
                    ),
                ),
                (
                    "profesor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="alumnos.alumno"
                    ),
                ),
            ],
        ),
    ]
