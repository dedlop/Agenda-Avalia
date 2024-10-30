from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    """Nome do Paciente"""
    nome = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.nome
   
class Consulta(models.Model):
    """Hora e data da consulta"""
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f'{self.data} {self.hora}'