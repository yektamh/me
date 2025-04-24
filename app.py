from flask import Flask, request
from flask_cors import CORS
import whisper
import openai
from gtts import gTTS
import os

app = Flask(__name__)
CORS(app)

openai.api_key = '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'
model = whisper.load_model("base")

@app.route("/process", methods=["POST"])
def process_audio():
    file = request.files["audio"]
    file_path = "audio.wav"
    file.save(file_path)

    result = model.transcribe(file_path, language="fa")
    text = result["text"]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "i am gonna help you nicly "},
            {"role": "user", "content": text}
        ]
    )

    final_response = response.choices[0].message.content.strip()
    return final_response

if "__name__" == "__main__":
    app.run(host="0.0.0.0", port=5000)
