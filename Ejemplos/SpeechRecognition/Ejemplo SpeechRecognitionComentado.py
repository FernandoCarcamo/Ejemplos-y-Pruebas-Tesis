import speech_recognition as sr  # Importa la biblioteca de reconocimiento de voz

# Crear un objeto reconocedor
recognizer = sr.Recognizer()  # Inicializa el reconocedor de voz

# Definir la función para reconocer voz
def recognize_speech():
    with sr.Microphone() as source:  # Usa el micrófono como fuente de audio
        print("Habla:")  # Indica al usuario que comience a hablar
        recognizer.adjust_for_ambient_noise(source)  # Ajusta el reconocedor al nivel de ruido ambiental para mejorar la captura del audio
        audio = recognizer.listen(source)  # Escucha y captura el audio hasta que detecta una pausa

    try:
        # Intenta reconocer el habla en el audio capturado utilizando el servicio Google Speech Recognition
        text = recognizer.recognize_google(audio, language="es-ES")  # Especifica el idioma español
        print("Dijiste:", text)  # Imprime el texto reconocido
    except sr.UnknownValueError:
        # Maneja el error cuando el reconocedor de voz no puede entender lo que fue dicho
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        # Maneja errores en la solicitud al servicio de Google, como problemas de conexión
        print("Error al solicitar resultados; {0}".format(e))

# Llamar a la función para reconocer voz
recognize_speech()  # Ejecuta la función para iniciar el proceso de reconocimiento de voz
