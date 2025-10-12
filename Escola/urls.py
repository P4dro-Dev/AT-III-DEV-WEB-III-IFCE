# escola/urls.py

from rest_framework import routers
from .views import TurmaViewSet, AlunoViewSet

# Instancia o DefaultRouter
router = routers.DefaultRouter()

# Registra os ViewSets. O prefixo ('turmas' e 'alunos') define o caminho da URL.
router.register(r'turmas', TurmaViewSet) # Gera /turmas/ e /turmas/{id}/
router.register(r'alunos', AlunoViewSet) # Gera /alunos/ e /alunos/{id}/

# As URLs finais que serão incluídas no projeto principal
urlpatterns = router.urls