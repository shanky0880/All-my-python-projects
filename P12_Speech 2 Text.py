import speech_recognition as sr

print('Say something...')
r = sr.Recognizer()

with sr.Microphone() as  source:
    audio = r.listen(source)


try:
    print('Recognizer :'+ r.recognize_google(audio) )
except Exception:
    print('Oops something went Wrong')
