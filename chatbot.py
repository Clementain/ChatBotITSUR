import nltk
import unidecode
from nltk.chat.util import Chat, reflections

# Definir los patrones y respuestas del chatbot
pares = [
    [
        r"(.*) carreras ofertadas",
        ["En el ITSUR ofrecemos las siguientes carreras: \n\n- Gastronomía\n- Ing. S. Automotrices\n- Ing. Ambiental\n- Ing. Sistemas C.\n- Ing. Industrial\n- Ing. Electrónica\n- Ing. Gestión Empresarial"]
    ],
    [
        r"(.*) información sobre (.*)",
        ["Lo siento, actualmente no tengo información detallada sobre la carrera de %2. Te sugiero visitar la página oficial del ITSUR para obtener más detalles."]
    ],
    [
        r"(.*) ayuda",
        ["Puedes preguntarme sobre las carreras ofertadas en el ITSUR o pedir información específica sobre alguna carrera en particular."]
    ],
    [
        r"(.*)",
        ["Lo siento, no puedo proporcionar información sobre esa carrera en particular. ¿Te gustaría conocer más detalles sobre las carreras ofertadas en el ITSUR?"]
    ]
]

# Convertir a minúsculas y eliminar acentos


def preprocess_text(text):
    text = text.lower()
    text = unidecode.unidecode(text)
    return text

# Crear el chatbot


def crear_chatbot():
    print("¡Hola! Soy el chatbot del ITSUR. ¿En qué puedo ayudarte hoy?")
    chatbot = Chat(pares, reflections)
    # Sobrescribir método _preprocess para el procesamiento personalizado del texto
    chatbot._preprocess = preprocess_text
    chatbot.converse()


# Ejecutar el chatbot
crear_chatbot()
