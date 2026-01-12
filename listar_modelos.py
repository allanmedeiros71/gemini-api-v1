from google import genai
import os

# Load environment variables from a local .env file (if present)
from dotenv import load_dotenv
load_dotenv()
# Obtém a chave da API do ambiente
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY não definida. Defina em .env ou nas variáveis de ambiente.")

client = genai.Client(api_key=API_KEY)

print("--- Modelos Disponíveis ---")
try:
    # Vamos iterar e imprimir apenas o nome, que é garantido existir
    for model in client.models.list():
        print(f"Nome encontrado: {model.name}")
except Exception as e:
    print(f"Erro crítico: {e}")
