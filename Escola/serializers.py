# escola/serializers.py

from rest_framework import serializers
from .models import Turma, Aluno

# Serializer para Turma (Passo 3.1)
class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

# Serializer para Aluno (Passo 5.1)
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'