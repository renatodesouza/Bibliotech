import google.generativeai as genai
import os

# Se você já tiver a chave no .env ou no sistema, ele pega automático
# Caso contrário, substitua 'SUA_CHAVE_AQUI' pela sua chave real
api_key = os.getenv("GOOGLE_API_KEY") or "SUA_CHAVE_AQUI"
genai.configure(api_key=api_key)

print("--- Modelos que suportam Embeddings na sua conta ---")
try:
    for m in genai.list_models():
        if 'embedContent' in m.supported_generation_methods:
            print(f"Nome técnico: {m.name}")
            print(f"Versão: {m.version}")
            print("-" * 30)
except Exception as e:
    print(f"Erro ao conectar na API: {e}")