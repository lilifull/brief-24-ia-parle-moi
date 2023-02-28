from flask import Flask, render_template
import azure.cognitiveservices.speech as speechsdk
from utils import recognize_from_microphone, response_ia, azure_speek

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/chat")
def chat():
    question = recognize_from_microphone()
    response = response_ia(question)
    azure_speek(response)
    return render_template('chat.html', question=question, response=response)

# verify that the app is running correctly
@app.route('/health')
def health():
    return 'App is running correctly'

if __name__ == ("__main__"):
    app.run(debug=True)
