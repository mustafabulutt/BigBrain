

from datetime import datetime
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import webbrowser
import random
import os
import time
from pygame import mixer


r = sr.Recognizer() 

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
            return voice
        except sr.UnknownValueError:
            speak('anlayamıyorum')
        except sr.Recognizer:
            speak('sistem çalışmıyor')
        return voice


def response(voice):
    print("dinliyorum:"+ voice)
    if 'yapıştır' in voice:
        speak('Yapıştırmam için önce kopyalamam lazım ahahah')
    if 'kopyala' in voice:
        speak('Babanın uşağımı var')    
    if 'kapan' in voice:
        speak('İşin bitince kapan tabi, Görüşürüz.')
        exit() 


def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)
  
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while mixer.music.get_busy():  
        time.sleep(1)
    # os.remove(file)

speak('Kopyala Yapıştırı ben yaparım sen yorulma')
while True:
    voice = record()
    print(voice)
    response(voice)
