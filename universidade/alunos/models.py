from django.db import models
from cursos.models import Curso

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True, default=1)
    email = models.EmailField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome