# Generated by Django 5.0 on 2023-12-22 06:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("login", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("is_avilable", models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Boook",
        ),
    ]