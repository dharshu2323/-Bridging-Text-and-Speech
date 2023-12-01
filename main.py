import speech_recognition as sr
import pyttsx3
import pyaudio
'''Speech to Text'''
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand.")
'''Text to Speech'''
engine = pyttsx3.init()
text = input("Enter the text:")
engine.setProperty("rate", 150)
engine.setProperty("volume", 0.8)
engine.say(text)
engine.runAndWait()
