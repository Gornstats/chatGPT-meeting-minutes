import openai
from docx import Document
from private import API_KEY

openai.api_key = API_KEY

def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe('whisper-1', audio_file)
    return transcription['text']


result = transcribe_audio("audio/voicetest.m4a")

print(result)