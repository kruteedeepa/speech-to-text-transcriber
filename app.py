from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import speech_recognition as sr
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
TRANSCRIPTS_FOLDER = 'transcriptions'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TRANSCRIPTS_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = None
    audio_file = None
    download_link = None

    if request.method == "POST":
        if "audio" not in request.files:
            return redirect(request.url)
        file = request.files["audio"]
        if file.filename == "":
            return redirect(request.url)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}_{file.filename}"
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        recognizer = sr.Recognizer()
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)

        try:
            transcript = recognizer.recognize_google(audio)
            txt_file = f"{filename}.txt"
            txt_path = os.path.join(TRANSCRIPTS_FOLDER, txt_file)
            with open(txt_path, "w") as f:
                f.write(transcript)
            download_link = txt_file
        except Exception as e:
            transcript = f"Error: {e}"

        audio_file = filename

    return render_template("index.html", transcript=transcript, audio_file=audio_file, download_link=download_link)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/download/<filename>')
def download_transcript(filename):
    return send_from_directory(TRANSCRIPTS_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
