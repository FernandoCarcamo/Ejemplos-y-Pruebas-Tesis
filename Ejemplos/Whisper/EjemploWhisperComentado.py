import sounddevice as sd  # Importa la biblioteca sounddevice para la grabación de audio
import numpy as np       # Importa numpy para manipulación numérica (arrays)
import whisper           # Importa la biblioteca de OpenAI Whisper para la transcripción de voz a texto
import wave              # Importa la biblioteca wave para manejar archivos WAV
import tempfile          # Importa la biblioteca tempfile para crear archivos temporales

def record_audio(duration=5, sample_rate=16000):
    """Función para grabar audio del micrófono con una duración y frecuencia de muestreo definidas."""
    print("Grabando...")
    # Graba el audio desde el micrófono y lo almacena en un array de numpy
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Bloquea la ejecución hasta que la grabación haya terminado
    print("Grabación terminada.")
    return recording  # Devuelve el array de numpy con el audio grabado

def save_wav(file_path, data, samplerate):
    """Función para guardar un array de numpy como archivo WAV."""
    # Abre un nuevo archivo WAV en modo escritura
    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(1)  # Configura el archivo como mono
        wf.setsampwidth(2)  # Define el ancho de los samples a 2 bytes (16 bits)
        wf.setframerate(samplerate)  # Establece la frecuencia de muestreo del archivo
        wf.writeframes(data)  # Escribe los datos de audio en el archivo WAV

def transcribe_audio(file_path):
    """Función para transcribir el audio a texto utilizando el modelo Whisper."""
    model = whisper.load_model("base")  # Carga el modelo "base" de Whisper
    result = model.transcribe(file_path)  # Usa Whisper para transcribir el audio del archivo WAV a texto
    return result['text']  # Devuelve el texto transcrito

# Configuración inicial
duration = 5  # Establece la duración de la grabación en segundos

# Proceso de grabación y transcripción
audio_data = record_audio(duration)  # Graba el audio del micrófono
temp_file = tempfile.mktemp(".wav")  # Crea un archivo temporal para almacenar el audio
save_wav(temp_file, audio_data, 16000)  # Guarda el audio grabado en el archivo WAV temporal

# Usar Whisper para transcribir el audio
transcription = transcribe_audio(temp_file)  # Transcribe el audio a texto
print("Transcripción:", transcription)  # Imprime la transcripción obtenida
