# Generated by Django 4.2.1 on 2023-05-22 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tree", "0012_family"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hist",
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
                ("date", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Log_Info",
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
                ("ip", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "device_type",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "browser_type",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "browser_version",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("os_type", models.CharField(blank=True, max_length=200, null=True)),
                ("os_version", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "location_country",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "location_city",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("history", models.ManyToManyField(blank=True, to="tree.hist")),
            ],
        ),
    ]
