from django.contrib import admin
from .models import Curso
# Register your models here.

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'descricao', 'carga_horaria')  # Ajuste os campos que deseja exibir no admin