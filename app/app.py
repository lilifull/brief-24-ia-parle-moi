from flask import Flask, render_template
import azure.cognitiveservices.speech as speechsdk
from utils import recognize_from_microphone, response_ia, azure_speek

app = Flask(__name__)

questions_responses = []

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/chat")
def chat():
    question = recognize_from_microphone()
    response = response_ia(question)
    azure_speek(response)
    questions_responses.append({ 'question': question, 'response': response})
    return render_template('chat.html', questions_responses=questions_responses)

# verify that the app is running correctly
@app.route('/health')
def health():
    return 'App is running correctly'

if __name__ == ("__main__"):
    app.run(debug=True)
