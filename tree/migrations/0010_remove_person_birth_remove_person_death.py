# Generated by Django 4.2.1 on 2023-05-13 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0009_alter_person_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='birth',
        ),
        migrations.RemoveField(
            model_name='person',
            name='death',
        ),
    ]