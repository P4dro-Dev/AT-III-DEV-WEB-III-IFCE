# escola/models.py

from django.db import models

# PRIMEIRA CLASSE: Turma (Passo 2)
class Turma(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()

    def __str__(self):
        return f"Turma: {self.nome} ({self.ano})"

# SEGUNDA CLASSE: Aluno (Passo 4)
class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    matricula = models.CharField(max_length=20, unique=True)
    # Chave Estrangeira ligando Aluno a Turma
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Aluno: {self.nome} ({self.matricula})"