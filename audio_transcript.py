import speech_recognition as sr
import noisereduce as nr
import os.path
from pydub import AudioSegment

def audioTranscript(audio, lang):
    r = sr.Recognizer()
    ext = getExtensionFile(audio)
    if(ext == ".mp3"):
        audio = mp3toWav(audio)
    if(ext == ".m4a"):
        audio = m4atoWav(audio)
    with sr.AudioFile(audio) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language=lang)
        return text
def getExtensionFile(file):
    extension = os.path.splitext(file)[1]
    return extension
def mp3toWav(audio):
    sound = AudioSegment.from_mp3(audio)
    audio = changeExtension(audio)
    sound.export(audio, format="wav")
    return audio
def m4atoWav(audio):
    sound = AudioSegment.from_file(audio, "m4a")
    audio = changeExtension(audio)
    sound.export(audio, format="wav")
    return audio
def changeExtension(url):
    tmp = os.path.splitext(url)[0]
    tmp += ".wav"
    return tmp

audio = "./assets/test3.m4a"
lang = "es"
audio_str = audioTranscript(audio, lang)
print(audio_str)