# Generated by Django 4.2.1 on 2023-05-12 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0005_person_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='death',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='fname',
            field=models.TextField(blank=True, null=True),
        ),
    ]
