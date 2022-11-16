import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('rate', 130)     # setting up new voice rate
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    # print(sr.Microphone.list_microphone_names())
    with sr.Microphone(device_index=2) as source:
        
        # r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source)
        r.energy_threshold= 4000 
        r.dynamic_energy_threshold = True
        # r.dynamic_energy_adjustment_damping = 0.15
        # r.dynamic_energy_adjustment_ratio = 1.5
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
        
    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query