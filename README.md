Speech-to-Text Transcriber App

A simple and aesthetic command-line application that converts `.wav` audio files into text using Python's `SpeechRecognition` library.

🎯 Features

- 🎧 Converts recorded `.wav` audio to text
- 🧠 Uses Google's Speech Recognition API
- 🎨 Styled CLI interface with pastel peach colors
- 📁 Organized folder structure and secure API key handling with `.env`
- 🌐 Easy to extend with GUI or web interface later

 📁 Folder Structure

speech_to_text/
├── audio_samples/
│ └── sample.wav # Your input audio file
├── uploads/ # (Optional) For storing additional audio files
├── venv/ # Python virtual environment
├── .env # API keys and environment variables
├── .gitignore # Hides venv and .env from git
├── transcriber.py # Main transcription script
└── README.md # This file

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/kruteedeepa/speech-to-text-transcriber.git
cd speech_to_text
2. Setup Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
You can create requirements.txt using:

bash
Copy
Edit
pip freeze > requirements.txt
🔑 Environment Setup
Create a .env file:

ini
Copy
Edit
GOOGLE_API_KEY=your_google_api_key_here
📝 How to Use
Place your .wav file inside the audio_samples folder.

Rename it to sample.wav or update the path in transcriber.py.

Run the script:

bash
Copy
Edit
python transcriber.py
🛡️ Technologies Used
Python 3.10

SpeechRecognition

Colorama

dotenv

📸 Preview
bash
Copy
Edit
╔════════════════════════════════════════════╗
║      🍑 Speech-to-Text Transcriber App     ║
╚════════════════════════════════════════════╝

📂 Loading audio file from: audio_samples/sample.wav
🎧 Listening to the audio...
🧠 Processing speech...

📝 Transcription Result:
This is a sample audio being converted to text.
🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first.

📩 Contact
Kruteedeepa Sahoo
GitHub • Email
