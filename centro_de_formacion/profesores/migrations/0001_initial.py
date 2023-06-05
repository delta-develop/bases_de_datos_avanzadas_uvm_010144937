# Generated by Django 4.2.1 on 2023-06-05 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("personas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profesor",
            fields=[
                (
                    "persona_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="personas.persona",
                    ),
                ),
                ("no_cuenta", models.PositiveIntegerField()),
                ("academia", models.TextField()),
                ("nivel", models.TextField()),
            ],
            bases=("personas.persona",),
        ),
    ]