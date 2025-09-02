# AUTOR: MATIAS MENDARO 
# CURSO: Inteligencia Artificial Generación de Prompts 
# N° COMISIÓN: 84180 
# NOMBRE PROYECTO: Asistente Virtual de Inversión 

# PRESENTACIÓN DEL PROBLEMA 
Las personas que quieren realizar alguna inversión con su dinero no saben por dónde 
iniciar. La falta de educación financiera hace que no conozcan los instrumentos 
existentes para invertir su dinero, de acuerdo con sus metas personales.  
Muchas veces terminan no realizando ninguna inversión, perdiendo dinero frente a la 
inflación, por ejemplo. 

# PROPUESTA DE SOLUCIÓN 
Asistente Virtual que en base a información del inversionista (monto de dinero a 
invertir, si su objetivo es a corto, mediano o largo plazo, y si tiene un perfil 
conservador o más arriesgado), brinda información breve y concisa sobre qué 
instrumento financiero es el más adecuado para cumplir su objetivo. También brinda 
una imagen gráfica simulando sus ganancias estimadas a lo largo de un tiempo 
específico. 

# VIABILIDAD DEL PROYECTO 
El proyecto es viable ya que atiende una necesidad real, y brinda una guía útil. 
Tampoco debe realizar cálculos financieros complejos, es meramente informativo y 
educativo. Técnicamente se basa en 3 inputs del inversor: monto a invertir, plazo, 
perfil. Se genera un prompt dinámicamente en base a estos datos iniciales, que 
interactúe con la api del modelo de IA tanto con modelo texto-texto como texto
imagen, brindando una respuesta útil, simple y clara al usuario/inversor.


# METODOLOGÍA
Primero, implementamos un prompt simple (Zero-Shot) para obtener una respuesta inicial del modelo.
Luego aplicamos técnicas de Fast Prompting, asignando un Rol al modelo y definiendo un Formato en la Respuesta. Se comparan los resultados de ambos casos para demostrar una mejora en calidad y formato de la respuesta.

# TECNOLOGÍAS QUE SE UTILIZAN
Lenguaje: Python 3
Modelo de IA: Google Gemini

# POC: DESCRIPCION DE LAS PRUEBAS DE CONCEPTO
El repositorio contiene dos demostraciones:

PoC 1: (ejemplo1.py) Prompt con Zero-Shot
Demuestra una interacción simple y directa con el modelo de IA. Se le da una instrucción sin rol específico ni formato de respuesta. El objetivo es mostrar cómo una falta de guía produce resultados genéricos y poco fiables para una aplicación real.

PoC 2: (ejemplo2.py) Prompt con Fast Prompting
La segunda prueba implementa un prompt que utiliza técnicas de Fast Prompting:
Rol modelo: Se le asigna al modelo el rol de "experto financiero en Argentina".
Formato de respuesta: Se le exige al modelo un formato de respuesta resumida y concisa en no mas de 5 renglones.

Este ejemplo demuestra cómo una única llamada a la API bien diseñada y con mayor nivel de guía, puede generar una respuesta consistente y de mejor calidad, siendo mas aplicable a la realidad.


👉 **[Ver Prueba de Concepto (POC) en Google Colab](https://colab.research.google.com/drive/1_bFP7rpBpZmxDZu2XvtOD_GOO_y4sHrh?usp=sharing#scrollTo=BnNpQzIytivi)**
