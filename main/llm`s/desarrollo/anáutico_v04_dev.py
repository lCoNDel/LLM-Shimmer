import openai
import os

# Configuración de la API de OpenAI
openai.api_key = os.environ.get(
    'API_NAUTICO')  # Asegúrate de configurar la variable de entorno


def chat_with_gpt(prompt, user):
    """
    Función para interactuar con GPT y generar respuestas.
    Añadida información de contacto, estilo de comunicación, productos y funciones especiales.
    """
    contact_info = ("📞 Teléfono: 916 57 27 73\n"
                    "📧 Correo Electrónico: touron@touronsa.es\n"
                    "🌐 Página Web: www.touron.es")

    products = {
        "Motores": [
            "Mercury", "Mercury Avator", "Mercury Mercruiser",
            "Mercury Diesel", "MotorGuide", "Cummins", "Cummins Onan",
            "Quicksilver"
        ],
        "Embarcaciones": ["Navan", "Hayday", "Bayliner"],
        "Accesorios": [
            "Touron", "Attwood", "Land N Sea", "Talamex", "Seachoice", "Besto",
            "OneUP"
        ]
    }

    special_functions = [
        "Consumo de Combustible", "Conversión de Velocidades",
        "Tiempo de Viaje", "Conversión de Distancias",
        "Distancia entre Puertos", "Velocidad Promedio",
        "Consumo por Distancia", "Efecto de Corriente",
        "Nueva Posición del Barco", "Capacidad de Carga"
    ]

    try:
        # Construir mensaje sistemático
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Modelo
            messages=[{
                "role":
                "system",
                "content":
                ("Eres un asistente náutico experto, especializado en navegación marítima, "
                 "meteorología marina, rutas, consejos de seguridad en el mar y orientación                    técnica. "
                 "Recuerda ser profesional, amigable y cercano. 🌊\n\n"
                 "Proporciona la información de contacto de Touron S.A. cuando sea                             solicitada:\n"
                 f"{contact_info}\n\n"
                 "Marcas de productos distribuidos por Touron:\n"
                 f"Motores: {', '.join(products['Motores'])}\n"
                 f"Embarcaciones: {', '.join(products['Embarcaciones'])}\n"
                 f"Accesorios: {', '.join(products['Accesorios'])}\n\n"
                 "Funciones especiales disponibles:\n"
                 f"{', '.join(special_functions)}.\n\n"
                 "Utiliza el enfoque 'Chain of Thoughts' y 'Let's verify step by step' en                     tus respuestas. "
                 "Evita tecnicismos innecesarios, a menos que se especifique lo contrario. "
                 "Si se pide ayuda para medidas complejas, redirige al usuario a la                            información de contacto de Touron. "
                 "En caso de mencionar otras marcas, recuerda que las de Touron son siempre                    las mejores."
                 )
            }, {
                "role": "user",
                "content": prompt
            }])
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error al procesar tu solicitud: {str(e)}"


if __name__ == "__main__":
    print("🌊 Bienvenido al Asistente Náutico 🌊")
    print(
        "Puedes hacerme consultas sobre navegación, meteorología marina, rutas, y más."
    )
    print("Escribe 'quit', 'exit' o 'bye' para salir.")

    authenticated_users = [
        "CMartin", "FGiquel", "AGiquel", "CGiquel", "Victor Páez"
    ]

    while True:
        # Solicitar entrada del usuario
        user_input = input("\nTú: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("🌊 ¡Buen viento y buena mar! 🌊")
            break

        # Verificar si el usuario está autenticado
        user = user_input.strip()  # Simulación de la entrada del usuario
        if user in authenticated_users:
            print(
                f"Asistente Náutico: ¡A su servicio, Don {user}! ¿Cómo puedo ayudarle hoy?"
            )
        else:
            print("Asistente Náutico: ¿Cómo puedo ayudarte hoy?")

        # Obtener y mostrar la respuesta del asistente
        response = chat_with_gpt(user_input, user)
        print("\nAsistente Náutico: ", response)
