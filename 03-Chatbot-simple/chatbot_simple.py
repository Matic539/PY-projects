def obtener_respuesta(mensaje, respuestas):
    mensaje = mensaje.lower()
    for pregunta, respuesta in respuestas.items():
        if pregunta in mensaje:
            return respuesta
    return "Lo siento, no entiendo tu pregunta."

def main():
    respuestas = {
        "hola": "¡Hola! ¿Cómo puedo ayudarte?",
        "¿cómo estás?": "Estoy bien, gracias por preguntar. ¿Y tú?",
        "¿cuál es tu nombre?": "Soy un chatbot, y estoy aquí para ayudarte.",
        "¿qué puedes hacer?": "Puedo responder preguntas simples y mantener una conversación básica contigo.",
        "¿qué es python?": "Python es un lenguaje de programación interpretado, de alto nivel y de propósito general.",
        "¿quién creó python?": "Python fue creado por Guido van Rossum y fue lanzado por primera vez en 1991.",
        "¿cuál es la capital de Francia?": "La capital de Francia es París.",
        "¿qué día es hoy?": "Hoy es un buen día para aprender algo nuevo.",
        "cuéntame un chiste": "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
        "adiós": "¡Adiós! Que tengas un buen día."
    }
    
    print("¡Hola! Soy un chatbot. Puedes hacerme preguntas simples.")
    print("Escribe 'salir' para terminar la conversación.")
    
    while True:
        mensaje = input("Tú: ")
        if mensaje.lower() == "salir":
            print("Chatbot: ¡Adiós! Que tengas un buen día.")
            break
        
        respuesta = obtener_respuesta(mensaje, respuestas)
        print(f"Chatbot: {respuesta}")

if __name__ == "__main__":
    main()
