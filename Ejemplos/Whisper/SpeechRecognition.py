import speech_recognition as sr

# Crear un objeto reconocedor
recognizer = sr.Recognizer()

# Definir la función para reconocer voz
def recognize_speech():
    with sr.Microphone() as source:
        print("Habla:")
        recognizer.adjust_for_ambient_noise(source)  # Ajusta el ruido de fondo
        audio = recognizer.listen(source)  # Escucha el audio del micrófono

    try:
        text = recognizer.recognize_google(audio, language="es-ES")  # Reconoce el audio usando Google Speech Recognition
        print("Dijiste:", text)
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print("Error al solicitar resultados; {0}".format(e))

# Llamar a la función para reconocer voz
recognize_speech()
