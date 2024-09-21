from django.db import models

class Paciente(models.Model):
    """Nome do Paciente"""
    nome = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.nome

class Dados(models.Model):
    """Dados do Paciente"""
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    contato = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'dados'

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.contato