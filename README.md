# 📚 Bibliotech - Controle de Leitura Pessoal & IA

Sistema web desenvolvido com Django para gerenciamento de biblioteca pessoal. Além de permitir o cadastro de autores, livros e criação de resenhas, o projeto evoluiu para uma arquitetura moderna com **Inteligência Artificial Generativa (RAG)**, permitindo que os usuários "conversem" com os livros indexados via IA.

A infraestrutura é 100% orquestrada em contêineres Docker, contando com processamento assíncrono e banco de dados vetorial para as buscas semânticas.

---

## 🚀 Tecnologias Utilizadas

**Backend & API**
* **Python 3.12** e **Django 5.0**
* **Django REST Framework (DRF)** (APIs em JSON)
* **JWT (Simple JWT)** (Autenticação baseada em tokens)
* **django-filter** (Filtragem avançada nas consultas da API)
* **drf-spectacular** (Documentação automática com Swagger e Redoc)

**Inteligência Artificial & Dados Vetoriais**
* **Google Gemini API** (Modelo `gemini-2.0-flash-lite`)
* **LangChain** (Framework de orquestração de IA)
* **ChromaDB** (Banco de dados vetorial para embeddings dos livros)

**Infraestrutura & Background Tasks**
* **Docker & Docker Compose** (Orquestração de microsserviços)
* **PostgreSQL** (Banco de dados relacional principal)
* **Redis** (Broker de mensageria em memória)
* **Celery** (Processamento de tarefas assíncronas e ingestão de PDFs)

---

## ⚙️ Funcionalidades

* [x] Cadastro de Autores, Livros e Resenhas.
* [x] **API REST Integrada** com suporte a paginação e filtros complexos.
* [x] **Segurança:** Autenticação via JWT (Access e Refresh tokens).
* [x] **Documentação Dinâmica:** Swagger UI embutido.
* [x] **IA / RAG (Retrieval-Augmented Generation):** Chat interativo com o conteúdo dos livros em PDF armazenados na plataforma.
* [x] **Processamento Assíncrono:** Ingestão de arquivos pesados delegada para workers do Celery via Redis.

---

## 🌐 Endpoints Principais da API

A API segue o padrão REST e retorna dados em JSON.

**Autenticação e Documentação**
| Método | Endpoint | Descrição |
|---|---|---|
| `POST` | `/api/token/` | Gera tokens JWT de acesso e refresh |
| `POST` | `/api/token/refresh/` | Atualiza o token de acesso |
| `GET` | `/api/docs/` | Abre a documentação interativa (Swagger) |

**Recursos Literários**
| Método | Endpoint | Descrição |
|---|---|---|
| `GET/POST` | `/api/autores/` | Lista/Cadastra autores |
| `GET/POST` | `/api/livros/` | Lista/Cadastra livros |
| `GET/POST` | `/api/resenhas/` | Lista/Cadastra resenhas |

**Inteligência Artificial (RAG)**
| Método | Endpoint | Descrição |
|---|---|---|
| `POST` | `/bibli/livros/<id>/chat/` | Faz uma pergunta sobre o conteúdo de um livro específico. Retorna a resposta gerada pela IA e a fonte (página do PDF). |

---

## 🔎 Filtros disponíveis (django-filter)

As consultas da API suportam filtros via query params.
Exemplos: `GET /api/livros/?titulo=Python` ou `GET /api/livros/?nota__gte=4`

| Parâmetro | Função |
|---|---|
| `titulo` | Filtra por nome do livro |
| `autor` | Filtra por autor |
| `status` | Filtra por status de leitura |
| `nota__gte` | Livros com nota maior ou igual a um valor |

---

## 🔧 Como rodar o projeto localmente (Docker)

Como o projeto utiliza múltiplos serviços (Banco, Redis, Celery, ChromaDB), a execução local foi simplificada com Docker.

**1. Clone o repositório:**
```bash
git clone [https://github.com/renatodesouza/Bibliotech.git](https://github.com/renatodesouza/Bibliotech.git)
cd Bibliotech

2. Configure as variáveis de ambiente:
Crie um arquivo .env na raiz do projeto contendo as credenciais do banco e a sua chave da API do Google AI:

Snippet de código
GOOGLE_API_KEY=sua_chave_aqui_gerada_no_google_ai_studio
# (Adicione outras variáveis de banco de dados conforme necessário)
3. Suba a infraestrutura completa:

Bash
docker-compose up -d --build
4. Execute as migrations e crie o superusuário:

Bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
5. Acesse os serviços:

API/Aplicação Web: http://localhost:8000/

Swagger (Documentação): http://localhost:8000/api/docs/

ChromaDB (API Local): http://localhost:8000 (Porta interna do container, exposta pelo docker-compose)

📌 Observações de versionamento
A main contém apenas código estável.

Novas implementações são enviadas por branches no padrão:

feat/ai-<escopo>

feat/api-<escopo>

fix/<escopo>

A pasta venv/ e arquivos sensíveis como .env não são versionados.

👤 Autor

Desenvolvido por Renato de Souza 🚀

Em transição de carreira e aprimorando estudos em Desenvolvimento Backend, APIs com Django, Arquitetura Docker e Integração com Inteligência Artificial.
