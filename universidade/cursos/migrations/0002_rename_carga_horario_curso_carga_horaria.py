# Generated by Django 5.1.5 on 2025-01-14 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='carga_horario',
            new_name='carga_horaria',
        ),
    ]
