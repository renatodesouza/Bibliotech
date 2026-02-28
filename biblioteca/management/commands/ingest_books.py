import os
from django.core.management.base import BaseCommand
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings # Mudança aqui
from langchain_chroma import Chroma
from biblioteca.models import Livro
from pathlib import Path
from dotenv import load_dotenv

# Define o caminho para a pasta onde o .env realmente está
# Ajuste o caminho 'biblioteca/.env' conforme a sua estrutura real
env_path = Path('.') / 'biblioteca' / '.env'
load_dotenv(dotenv_path=env_path)
print(f"DEBUG: A chave da API foi carregada? {'Sim' if os.getenv('GOOGLE_API_KEY') else 'Não'}")

class BookIngestor:
    def __init__(self):
        # Aqui você já pode usar o os.getenv à vontade
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.model_name = os.getenv("EMBEDDING_MODEL_NAME")

    def run(self):
        print(f"Usando o modelo: {self.model_name}")
        # ... lógica de processar o livro

# 2. OU DENTRO DO BLOCO DE EXECUÇÃO
if __name__ == "__main__":
    ingestor = BookIngestor()
    ingestor.run()


class Command(BaseCommand):
    help = 'Processa PDFs da biblioteca e armazena no banco vetorial usando Gemini'

    def add_arguments(self, parser):
        parser.add_argument('book_id', type=int, nargs='?', help='ID do livro no Django')

    def handle(self, *args, **options):
        book_id = options.get('book_id')

        if book_id:
            livro = livro.objects.filter(id=book_id).first()
        else:
            livro = Livro.objects.last()

        if not livro or not livro.arquivo:
            self.stdout.write(self.style.ERROR('Livro não encontrado'))
            return
        # 2 Usa o caminho real do arquivo
        path = livro.arquivo.path

        if not os.path.exists(path):
            self.stdout.write(self.style.ERROR(f'Arquivo nao encontrado {path}'))
            return
        
        self.stdout.write(self.style.SUCCESS(f'Processando livro: {livro.titulo}'))

        # 3. Configuração do Banco Vetorial com Google Embeddings
        # O modelo 'embedding-001' é o padrão e muito eficiente
        # embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
        # embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        # embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
        
        vector_db = Chroma(
            persist_directory="./chroma_db",
            embedding_function=embeddings
        )

        # 4 Carregamento do pdf
        loader = PyPDFLoader(path)
        pages = loader.load()

        # Splitting
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = text_splitter.split_documents(pages)
        
        # 5. Vincula os trechos ao ID do livro (IMPORTANTE para a busca depois)
        for chunk in chunks:
            chunk.metadata["book_id"] = livro.id # Isso é vital para o ai_service.py filtrar
            chunk.metadata["titulo"] = livro.titulo

        
        # 6. Salvando no ChromaDB
        vector_db.add_documents(chunks)
        
        self.stdout.write(self.style.SUCCESS(f'Sucesso! {len(chunks)} trechos indexados com Gemini.'))