import speech_recognition as sr
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Define a peach color substitute (orange-pink shade)
PEACH = Fore.LIGHTRED_EX  # Soft warm pink (close to peach)
HEADER = Fore.LIGHTMAGENTA_EX
BOLD = Style.BRIGHT

def show_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(HEADER + BOLD + """
╔════════════════════════════════════════════╗
║      🍑 Speech-to-Text Transcriber App     ║
╚════════════════════════════════════════════╝
""")


def transcribe_audio_file(file_path):
    recognizer = sr.Recognizer()
    show_header()

    if not os.path.exists(file_path):
        print(Fore.RED + "❌ File not found. Make sure your .wav file is placed correctly.")
        return

    print(PEACH + f"📂 Loading audio file from: {file_path}")
    
    with sr.AudioFile(file_path) as source:
        print(PEACH + "🎧 Listening to the audio...")
        audio = recognizer.record(source)

    print(PEACH + "🧠 Processing speech...")

    try:
        text = recognizer.recognize_google(audio)
        print("\n" + HEADER + BOLD + "📝 Transcription Result:\n")
        print(PEACH + text)
    except sr.UnknownValueError:
        print(Fore.RED + "❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(Fore.RED + f"⚠️ Request failed: {e}")


# --------- MAIN CALL ---------
if __name__ == "__main__":
    transcribe_audio_file("audio_samples/sample.wav")
