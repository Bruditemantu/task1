# Generated by Django 5.0 on 2023-12-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Boook",
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
                ("name", models.CharField(max_length=50)),
                ("price", models.FloatField()),
                ("author", models.CharField(max_length=50)),
                ("is_avilable", models.BooleanField(verbose_name=True)),
            ],
        ),
    ]
