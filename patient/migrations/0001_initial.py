# Generated by Django 5.0.7 on 2024-11-07 05:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                    "profile_pic",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile_pic/Patient/"
                    ),
                ),
                ("age", models.PositiveIntegerField()),
                ("bloodgroup", models.CharField(max_length=10)),
                ("disease", models.CharField(max_length=100)),
                ("doctorname", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=40)),
                ("mobile", models.CharField(max_length=20)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]