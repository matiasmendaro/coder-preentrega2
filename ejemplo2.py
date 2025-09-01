from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
generate_content_config = types.GenerateContentConfig(
    temperature=0,
    thinking_config = types.ThinkingConfig(
        thinking_budget=-1,
    ),
)

user_profile = {
    "plazo": "Corto Plazo (1 a 2 meses)",
    "perfil_riesgo": "Agresivo",
    "monto": "1500000 ARS"
}
print(f"Perfil de Usuario:")
print(f" - Perfil: {user_profile['perfil_riesgo']}")
print(f" - Plazo: {user_profile['plazo']}")
print(f" - Monto: {user_profile['monto']}")

print("Ejecutando Ejemplo 2: Prompt con Fast Prompting")
prompt_avanzado = f"Actúa como un experto financiero en Argentina. Tu objetivo es crear una propuesta de cartera de inversión educativa y clara para un usuario con un perfil {user_profile['perfil_riesgo']} que quiere invertir {user_profile['monto']} a {user_profile['plazo']}. Da una respuesta resumida y concisa en no mas de 5 renglones."

contents = [
    types.Content(
        role="user",
        parts=[
            types.Part.from_text(text=prompt_avanzado),
        ],
    ),
]

for chunk in client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents=contents,
    config=generate_content_config,
):
    print(chunk.text, end="")
