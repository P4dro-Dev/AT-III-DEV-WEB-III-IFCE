# projeto_api/settings.py

INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    # ------------------ SEUS APPS AQUI ------------------
    'rest_framework',   # Adiciona o Django REST Framework
    'escola',           # Adiciona o seu App 'escola'
    # ----------------------------------------------------
]
# ... (restante do arquivo)