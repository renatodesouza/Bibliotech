# 📚 Bibliotech - Controle de Leitura Pessoal

Sistema web desenvolvido com Django para gerenciamento de biblioteca pessoal, permitindo o cadastro de autores, livros e criação de resenhas com sistema de avaliação.  
Nesta fase, o projeto evoluiu para expor os dados também via **API REST (JSON)** e recebeu uma camada profissional de filtros nas consultas com **django-filter**.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.12**
* **Django 5.0**
* **Django REST Framework** (APIs em JSON)
* **django-filter** (Filtragem avançada nas consultas da API)
* **SQLite** (Banco de dados de desenvolvimento)
* **Git & GitHub** (Versionamento)

---

## ⚙️ Funcionalidades

* [x] Cadastro de Autores e Livros
* [x] Status de leitura (Lendo, Finalizado, Para Ler)
* [x] Sistema de Resenhas com nota (1-5)
* [x] Painel Administrativo do Django customizado
* [x] **API REST para consulta e manipulação dos dados (JSON)**
* [x] **CRUD via API para Livros e Autores**
* [x] **Filtragem de consultas na API usando django-filter**
* [x] **Suporte a parâmetros de filtro nas requisições**
* [x] **API com paginação e backends configurados para filtros**

---

## 🌐 Endpoints da API

A API segue o padrão REST e retorna dados em JSON.

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/api/autores/` | Lista todos os autores |
| `GET` | `/api/livros/` | Lista todos os livros |
| `GET` | `/api/resenhas/` | Lista todas as resenhas |
| `POST` | `/api/livros/` | Cadastra um novo livro |
| `POST` | `/api/autores/` | Cadastra um novo autor |
| `POST` | `/api/resenhas/` | Cadastra uma nova resenha |
| `PUT/PATCH` | `/api/livros/<id>/` | Atualiza um livro |
| `PUT/PATCH` | `/api/autores/<id>/` | Atualiza um autor |
| `PUT/PATCH` | `/api/resenhas/<id>/` | Atualiza uma resenha |
| `DELETE` | `/api/livros/<id>/` | Remove um livro |
| `DELETE` | `/api/autores/<id>/` | Remove um autor |
| `DELETE` | `/api/resenhas/<id>/` | Remove uma resenha |

---

## 🔎 Filtros disponíveis (django-filter)

As consultas da API `/api/livros/`, `/api/autores/` e `/api/resenhas/` (quando aplicável) suportam filtros via query params.

Exemplos de uso:

GET /api/livros/?titulo=Python
GET /api/livros/?autor=Asimov
GET /api/livros/?status=Lendo
GET /api/livros/?nota__gte=4

Filtros habilitados nos principais campos:

| Parâmetro | Função |
|---|---|
| `titulo` | Filtra por nome do livro |
| `autor` | Filtra por autor |
| `data` | Filtra por data |
| `status` | Filtra por status de leitura |
| `nota__gte` | Livros com nota maior ou igual a um valor |
| `nota__lte` | Livros com nota menor ou igual a um valor |

> O backend de filtros foi configurado globalmente com `DjangoFilterBackend` no DRF.

---

## 🔧 Como rodar o projeto localmente

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/bibliotech.git](https://github.com/renatodesouza/Bibliotech.git)

-----------------------------------
📌 Acesse o projeto:

cd Bibliotech

📌 Crie o ambiente virtual:

python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

-----------------------------------
📌 Instale as dependências:

pip install -r requirements.txt

📌 Execute as migrations do banco:

python manage.py migrate

📌 Inicie o servidor local:

python manage.py runserver

📌 Acesse o navegador:

http://127.0.0.1:8000/

-------------------------------------
Para acessar a API:

http://127.0.0.1:8000/api/livros/


📌 Observações de versionamento

A main contém apenas código estável.

Novas implementações são enviadas por branches no padrão:

feature/api-<escopo>
feature/filter-<escopo>
fix/<escopo>
docs/<escopo>


Pull Requests são revisados antes do merge.

A pasta venv/ e arquivos sensíveis como .env não são versionados.

👤 Autor

Desenvolvido por Renato Souza 🚀
Projeto em evolução contínua para estudos de Backend e APIs com Django.
