from google import genai
import os

# Load environment variables from a local .env file (if present)
from dotenv import load_dotenv
load_dotenv()
# Obtém a chave da API do ambiente
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY não definida. Defina em .env ou nas variáveis de ambiente.")
MODEL = os.getenv("GEMINI_MODEL")
if not MODEL:
    raise RuntimeError("GEMINI_MODEL não definido. Defina em .env ou nas variáveis de ambiente.")

# Instancia o cliente (novo padrão)
client = genai.Client(api_key=API_KEY)


def consultar_gemini(prompt):
    try:
        # A sintaxe de chamada mudou: client.models.generate_content
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Erro na requisição: {e}"


# Teste
ideia = "um script que organiza arquivos por contexto"
print(consultar_gemini(f"Me dê um nome criativo para um projeto python que faz: {ideia}"))
