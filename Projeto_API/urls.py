# projeto_api/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclui as URLs do app 'escola' sob o prefixo 'api/'
    path('api/', include('escola.urls')),
]