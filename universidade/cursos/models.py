from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    codigo = models.PositiveIntegerField(max_length=100, unique=True, default=1)
    descricao = models.TextField()
    carga_horaria = models.PositiveIntegerField()

    def __str__(self):
        return self.nome