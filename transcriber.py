import speech_recognition as sr
import os
from colorama import Fore, Style, init
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize colorama
init(autoreset=True)

# Define a peach color substitute
PEACH = Fore.LIGHTRED_EX  # Close to pastel peach
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
        # Use API key from environment if available
        if GOOGLE_API_KEY:
            text = recognizer.recognize_google(audio, key=GOOGLE_API_KEY)
        else:
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
