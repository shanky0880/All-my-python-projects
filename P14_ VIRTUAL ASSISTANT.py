import speech_recognition as sr
import pyttsx3
import time
from time import ctime
import webbrowser
import playsound
import os
import random
from gtts import gTTS


print('Say something...')
r = sr.Recognizer()
speaker = pyttsx3.init()

def record_audio(ask = False):
#recording audio
    with sr.Microphone() as source:
        if ask:
            lee_voice(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print('Recognizer voice :'+ voice_data)

        except Exception:
            print('Oops something went Wrong')
            lee_voice('Oops something went Wrong')
        return voice_data

def lee_voice(audio_string):
    #voice modulation
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'who are you' in voice_data:
        lee_voice('My name is lena , made by Shashank')
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        lee_voice('Here is what i found' + search)

    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        lee_voice('Here is location' + location)

    if 'what is the time' in voice_data:
        lee_voice("Sir the time is :" + ctime())


    if 'exit' in voice_data:
        lee_voice('Thanks have a good day ')
        exit()

time.sleep(1)
lee_voice('How can i help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)



speaker.runAndWait()