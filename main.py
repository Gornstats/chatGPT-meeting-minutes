import openai
from docx import Document

def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe('whisper-1', audio_file)
    return transcription['text']


#transcribe_audio("audio/EarningsCall.wav")