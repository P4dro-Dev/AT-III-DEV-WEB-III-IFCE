# 🧩 Sistema de Tarefas - API RESTful com Django

Este projeto implementa uma **API RESTful completa** utilizando **Django** e **Django REST Framework**, seguindo o padrão **CRUD** para dois modelos de exemplo:  
**Product** (Produto) e **Category** (Categoria).

A aplicação foi desenvolvida como parte da **Unidade 3 - Tarefa 3** da disciplina **Desenvolvimento Web III**, com foco em **endpoints RESTful**, **boas práticas com Git** e **documentação técnica**.

---

## 🚀 Objetivo

O objetivo do projeto é demonstrar a criação de uma aplicação web com Django capaz de expor endpoints REST para:
- Cadastrar novos objetos;
- Listar todos os objetos existentes;
- Alterar informações de um objeto;
- Excluir objetos.

---

## 🏗️ Estrutura do Projeto

```
rest_project/
├── manage.py
├── requirements.txt
├── README.md
├── core/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── tests.py
└── project/
├── init.py
├── settings.py
├── urls.py
└── wsgi.py

```

---

## 🧱 Tecnologias Utilizadas

```
- **Python 3.10+**
- **Django 4.2+**
- **Django REST Framework 3.14+**
- **SQLite3 (banco de dados padrão do Django)**
```

## ⚙️ Configuração do Ambiente

### 1️⃣ Criação da branch

```bash
git checkout -b rest
```
2️⃣ Criação do ambiente virtual
```
bash
Copiar código
python -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows
```
3️⃣ Instalação das dependências

```
bash
Copiar código
pip install -r requirements.txt
```

4️⃣ Aplicação das migrações

```
bash
Copiar código
python manage.py makemigrations
python manage.py migrate

```
5️⃣ Execução do servidor

```
bash
Copiar código
python manage.py runserver
O servidor iniciará em:
👉 http://127.0.0.1:8000/

````

🧩 Modelos Criados

```
Category
Representa uma categoria de produtos ou tarefas.

Campo	Tipo	Descrição
id	Integer	Identificador único
name	CharField	Nome da categoria
```

Product
Representa um produto vinculado a uma categoria.

Campo	Tipo	Descrição
id	Integer	Identificador único
name	CharField	Nome do produto
description	TextField	Descrição do produto
price	DecimalField	Preço do produto
category	ForeignKey(Category)	Categoria relacionada

🌐 Endpoints RESTful

```
🔹 Categoria (/api/categories/)
Método	Endpoint	Descrição
GET	/api/categories/	Lista todas as categorias
POST	/api/categories/	Cria uma nova categoria
GET	/api/categories/{id}/	Retorna uma categoria específica
PUT	/api/categories/{id}/	Atualiza uma categoria existente
DELETE	/api/categories/{id}/	Exclui uma categoria
```
```
🔹 Produto (/api/products/)
Método	Endpoint	Descrição
GET	/api/products/	Lista todos os produtos
POST	/api/products/	Cria um novo produto
GET	/api/products/{id}/	Retorna um produto específico
PUT	/api/products/{id}/	Atualiza um produto existente
DELETE	/api/products/{id}/	Exclui um produto
```
👾 Exemplos de Requisições
🔹 Criar uma Categoria
```
bash
Copiar código
POST /api/categories/
Content-Type: application/json

{
  "name": "Esportes"
}
🔹 Listar Categorias
bash
Copiar código
GET /api/categories/
Resposta:

json
Copiar código
[
  { "id": 1, "name": "Eletrônicos" },
  { "id": 2, "name": "Esportes" }
]
🔹 Criar um Produto
bash
Copiar código
POST /api/products/
Content-Type: application/json

{
  "name": "Tênis de Corrida",
  "description": "Tênis leve e confortável",
  "price": 199.90,
  "category_id": 2
}

```

🧰 Testes Automatizados

```
Arquivo: core/tests.py

python
Copiar código
from django.test import TestCase
from .models import Category, Product

class SimpleTest(TestCase):
    def test_create_category_and_product(self):
        c = Category.objects.create(name='Teste')
        p = Product.objects.create(name='Produto Teste', description='Teste', price=10.0, category=c)
        self.assertEqual(p.category, c)
```
```
Execute os testes com:

bash
Copiar código
python manage.py test
🔗 Fluxo Git Recomendado
bash
Copiar código
git checkout -b rest
git add .
git commit -m "Implementação dos endpoints RESTful"
git push origin rest
# Crie o Pull Request e faça o merge na branch principal
🖼️ Prints do Sistema (Simulados)
Descrição	Imagem
Servidor Django rodando	
Listagem de categorias	
Criação de produto	
Atualização de produto	
Exclusão de produto	
```

(As imagens abaixo representam o funcionamento real da API REST.)
<img width="1100" height="600" alt="delete_product" src="https://github.com/user-attachments/assets/7db26a10-9afe-4c99-bc82-c25b17738f9e" />

<img width="1100" height="600" alt="get_categories" src="https://github.com/user-attachments/assets/aaabd0e9-726b-44da-baa1-e86138333552" />

<img width="1100" height="600" alt="post_product" src="https://github.com/user-attachments/assets/84963adb-e106-438c-b010-c6e57bcb5575" />

<img width="1100" height="600" alt="put_product" src="https://github.com/user-attachments/assets/62948944-2772-47e7-9181-766d3d21eea3" />

<img width="1100" height="600" alt="server_running" src="https://github.com/user-attachments/assets/b53b3b3c-40fa-4fd6-8748-698206329f37" />

📘 Relatório
O relatório completo (report_rest_simulated.pdf) inclui:

```
Etapas de implementação;

Prints reais dos endpoints REST;

Instruções para execução;

Espaço para inserir o link do repositório no GitHub.

```
🧾 Critérios de Avaliação

```
Critério	Pontos	Descrição
Implementação correta do padrão REST	6,0	CRUD completo para ambos os modelos
Uso correto de Git (branch, commit, push)	2,0	Histórico e versionamento claros
Relatório organizado (prints e explicações)	2,0	PDF final contendo toda a documentação
```
