import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from django.conf import settings

class AIService:
    def __init__(self):
        # 1. Configuração dos Embeddings (Mesmo modelo usado na ingestão)
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
        
        # 2. Configuração do Modelo de Chat (Gemini Flash é rápido e barato)
        self.llm = ChatGoogleGenerativeAI(
                model="models/gemini-flash-latest", 
                version="v1",  # Forçamos a V1 em vez da v1beta que estava dando erro
                temperature=0.3
            )
        
        # 3. Conexão com o Banco Vetorial existente
        self.vector_db = Chroma(
            persist_directory="./chroma_db",
            embedding_function=self.embeddings
        )

    def ask_book(self, book_id, question):
        # 4. Criamos um "Retriever" que filtra apenas pelo book_id específico
        retriever = self.vector_db.as_retriever(
            search_kwargs={'filter': {'book_id': book_id},
                           'k':3
            }
        )

        # 5. Definimos um Prompt para a IA não "alucinar"
        template = """
        Você é um assistente acadêmico especializado. Use os seguintes trechos de contexto 
        extraídos de um livro para responder à pergunta do usuário. 
        Se você não souber a resposta com base no contexto, diga apenas que não encontrou 
        essa informação no livro. Não tente inventar fatos.

        Contexto:
        {context}

        Pergunta: 
        {question}

        Resposta útil e detalhada:"""

        prompt = PromptTemplate(
            template=template, 
            input_variables=["context", "question"]
        )

        # 6. Montagem da Chain de busca e resposta (RAG)
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": prompt}
        )

        # 7. Execução da pergunta
        response = qa_chain.invoke({"query": question})
        
        return {
            "answer": response["result"],
            "sources": [doc.metadata for doc in response["source_documents"]]
        }