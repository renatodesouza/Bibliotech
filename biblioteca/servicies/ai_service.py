from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from django.conf import settings

class LibraryAIService:
    def __init__(self):
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

        self.vector_db = Chroma(
            persist_directory="./chroma_db",
            embedding_function=self.embeddings
        )

        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3)


        def ask_question(self, question):
            # Criamos uma "Chain" que busca no banco e responde
            qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=self.vector_db.as_retriever(search_kwargs={"k": 3}) # Busca os 3 trechos mais relevantes
            )
            
            response = qa_chain.invoke(question)
            return response["result"]