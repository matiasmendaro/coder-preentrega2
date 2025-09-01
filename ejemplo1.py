from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

user_profile = {
    "plazo": "Largo Plazo (más de 5 años)",
    "perfil_riesgo": "Conservador",
    "monto": "100000 ARS"
}
print(f"Perfil de Usuario:")
print(f" - Perfil: {user_profile['perfil_riesgo']}")
print(f" - Plazo: {user_profile['plazo']}")
print(f" - Monto: {user_profile['monto']}")

print("Ejecutando Ejemplo 1: Prompt con Zero-Shot")
prompt_basico = f"Sugiere una cartera de inversión para alguien con un perfil {user_profile['perfil_riesgo']} que quiere invertir {user_profile['monto']} a {user_profile['plazo']}."

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt_basico,
)

print(response.text)