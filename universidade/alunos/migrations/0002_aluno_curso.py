# Generated by Django 5.1.5 on 2025-01-14 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='cursos.curso'),
        ),
    ]