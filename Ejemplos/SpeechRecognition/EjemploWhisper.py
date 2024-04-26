import sounddevice as sd
import numpy as np
import whisper
import wave
import tempfile

def record_audio(duration=5, sample_rate=16000):
    """Graba audio del micrófono."""
    print("Grabando...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Espera hasta que la grabación termine
    print("Grabación terminada.")
    return recording

def save_wav(file_path, data, samplerate):
    """Guarda los datos de numpy array a un archivo WAV."""
    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # los samples son de int16, por lo tanto 2 bytes
        wf.setframerate(samplerate)
        wf.writeframes(data)

def transcribe_audio(file_path):
    """Transcribe el audio a texto utilizando Whisper."""
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result['text']

# Configuración inicial
duration = 5  # Duración de la grabación en segundos

# Proceso de grabación y transcripción
audio_data = record_audio(duration)
temp_file = tempfile.mktemp(".wav")  # Crea un archivo temporal
save_wav(temp_file, audio_data, 16000)  # Guarda la grabación en un archivo WAV

# Usar Whisper para transcribir el audio
transcription = transcribe_audio(temp_file)
print("Transcripción:", transcription)
