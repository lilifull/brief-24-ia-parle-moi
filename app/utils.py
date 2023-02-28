import os
import azure.cognitiveservices.speech as speechsdk
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.getenv('SPEECH_KEY'), region=os.getenv('SPEECH_REGION'))
    speech_config.speech_recognition_language="fr-FR"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    word_list = ['Sophana', 'C#', 'Scikit-learn', 'scipy', 'R', 'serverless', 'pytorch', 'seaborn', 'simplonien', 'simplonienne','Sirine','Lakhbir','Simplonline']
    phrase_list_grammar = speechsdk.PhraseListGrammar.from_recognizer(speech_recognizer)
    for word in word_list:       
        phrase_list_grammar.addPhrase(word)

    print("Poses ta question.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    return speech_recognition_result.text



def response_ia(question, tchat_list) :
    mode_tchat = f"Si j étais un humain du nommé Lily et que j étais dans la conversation suivante : '{tchat_list}' et qu une personne rajoutais cela {question} je lui dirai :" 
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt=mode_tchat,
  temperature=0.8,
  max_tokens=300,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)
    response = response.choices[0].text
    return response

def azure_speek(response):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name="fr-FR-EloiseNeural"
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    speech_synthesizer.speak_text_async(response).get()
  

if __name__ == ("__main__"):
    question= recognize_from_microphone()
    print(recognize_from_microphone())
    response = response_ia(question)
    print(response)
    azure_speek(response)
    
