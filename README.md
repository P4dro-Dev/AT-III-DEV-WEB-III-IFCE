# Projeto RESTful - Desenvolvimento Web II

Este repositório contém um exemplo completo de implementação de endpoints RESTful usando Django e Django REST Framework.

## Estrutura do projeto

```
rest_project/
├── manage.py
├── requirements.txt
├── README.md
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
└── project/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Modelos criados
1. `Product` — representa um produto com nome, descrição e preço.
2. `Category` — representa uma categoria que pode ter vários produtos.

## Endpoints (RESTful)
- `GET /api/products/` — lista produtos
- `POST /api/products/` — cria produto
- `GET /api/products/{id}/` — obtém produto
- `PUT /api/products/{id}/` — atualiza produto
- `DELETE /api/products/{id}/` — apaga produto

- `GET /api/categories/` — lista categorias
- `POST /api/categories/` — cria categoria
- `GET /api/categories/{id}/` — obtém categoria
- `PUT /api/categories/{id}/` — atualiza categoria
- `DELETE /api/categories/{id}/` — apaga categoria

## Como executar (localmente)
1. Crie uma branch `rest`:
```bash
git checkout -b rest
```

2. Instale dependências:
```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate         # Windows (PowerShell)
pip install -r requirements.txt
```

3. Aplique migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Crie superuser (opcional):
```bash
python manage.py createsuperuser
```

5. Rode o servidor:
```bash
python manage.py runserver
```

6. Teste os endpoints com `curl` ou Postman:
```bash
# listar categorias
curl http://127.0.0.1:8000/api/categories/

# criar categoria
curl -X POST -H "Content-Type: application/json" -d '{"name":"Esportes"}' http://127.0.0.1:8000/api/categories/
```

## Git (exemplo de fluxo)
```bash
git add .
git commit -m "Implement endpoints REST for Product and Category"
git push origin rest
# Abra Pull Request e depois merge para main
```

## Observações
- O projeto usa Django e Django REST Framework. Caso prefira, faça as alterações para usar ViewSets/Router.
- Arquivos criados apenas para entrega da tarefa: adapte nomes, campos e validações conforme o seu problema.
