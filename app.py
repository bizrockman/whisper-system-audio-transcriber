import os
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import keyboard
from openai import OpenAI

def callback(indata, frames, time, status):
    if status:
        print("Status: ", status)  # Zeigt mögliche Fehler oder Warnungen während der Aufnahme an
    frames.append(indata.copy())  # Sammle alle Daten, die indata enthält


def record_audio_on_keypress(filename, samplerate):
    print("Drücke und halte die Leertaste zum Aufnehmen...")
    frames = []

    try:
        keyboard.wait('space')
        print("Aufnahme beginnt...")
        with sd.InputStream(samplerate=samplerate, channels=2, dtype='int16',
                            callback=lambda indata, frame_count, time_info, status: callback(indata, frames, time_info, status)):
            keyboard.wait('space')  # Warte auf das Loslassen der Leertaste

        recording = np.vstack(frames)
        write(filename, samplerate, recording.astype(np.int16))  # Konvertieren zu int16 beim Schreiben der Datei
        print("Aufnahme gespeichert als:", filename)
        return filename
    except KeyboardInterrupt:
        print("Aufnahme beendet durch Benutzer.")
    except Exception as e:
        print("Ein Fehler ist aufgetreten:", e)  # Zeigt unerwartete Fehler an


def transcribe_audio(filename):
    client = OpenAI()

    audio_file = open(filename, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    print(transcription.text)

def main():
    from dotenv import load_dotenv
    load_dotenv(".env.local")
    OPENAI_API_KEY= os.getenv('OPENAI_API_KEY')
    samplerate = 44100  # Abtastrate
    filename = 'output.wav'  # Dateiname für die gespeicherte Aufnahme
    recorded_file = record_audio_on_keypress(filename, samplerate)
    transcribe_audio(recorded_file)
    if recorded_file:
        print("Datei wurde erfolgreich aufgenommen.")


if __name__ == '__main__':
    main()
