# Generated by Django 4.2.1 on 2023-06-05 07:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Asignatura",
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
                ("nombre", models.TextField()),
                ("codigo", models.TextField()),
                ("area", models.TextField()),
                ("departamento", models.TextField()),
                ("creditos", models.FloatField()),
            ],
        ),
    ]
