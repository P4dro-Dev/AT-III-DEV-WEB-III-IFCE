# escola/views.py

from rest_framework import viewsets
from .models import Turma, Aluno
from .serializers import TurmaSerializer, AlunoSerializer

# ViewSet para Turma (Passo 3.2)
class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

# ViewSet para Aluno (Passo 5.2)
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer