import datetime
import os
from threading import *
import sys
import requests
import search_google.api
import json
from tkinter import *
from mainFunctions import *
from basicsFunctions import *
import random 

hjokes=None
class tkinterThread(Thread):
    def run(self):
        window = Tk()
        window.geometry("569x320")
        window.title("Hindi Joke")
        
        lbl = Label(window, text=hjokes)
        #lbl = Label(window, text="Hello", font=("Arial Bold", 50))
        lbl.grid(column=0, row=0)
        
        window.mainloop()


def englishJoke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/jokes/random")
        # Print the status code of the response.
        print(response.status_code)
        data=response.json()
        speak(data["setup"])
        speak(data["punchline"])
    except:
        print("Unkown error in this command please try again later.")
    oneMoreEnglishJoke()

def oneMoreEnglishJoke():
    speak("Do you to hear one more ?")
    query = takeCommand().lower()

    if 'yes' in query:
        englishJoke()

    elif 'no' in query:
        speak("Ok fine, But call me again if you want to hear jokes.")

    else:
        speak("i cant under stand please anser yes or no")
        oneMoreEnglishJoke()

def hindiJokes():
    try:
        #getting  category id of jokes from API
        jcat=requests.get("https://gofugly.in/api/sub_categories/23")
        print(jcat.status_code)
        jcatData=jcat.json()
        jcategory=[]
        for ids in jcatData["result"]:
            id=ids["id"]
            jcategory.append(id)
        
        #getting random joke using category id
        response = requests.get("https://gofugly.in/api/content/"+random.choice(jcategory))
        # Print the status code of the response.
        print(response.status_code)
        data=response.json()
        speak('i cant speak hindi properly but i can print all hindi jokes for you. Hope you like them')
        myJokes=[]
        tkThread = tkinterThread()
        for jokes in data["result"]:
            joke=jokes["joke"]
            myJokes.append(joke)
        print(len(myJokes))
        global hjokes
        hjokes = myJokes[random.randrange(0, len(myJokes))]
        tkThread.daemon=True
        tkThread.start()

    except:
        print("Unkown error in this command please try again later.")

choiceCount=0
def getJokes():
    global choiceCount
    speak("which joke do you need. Hindi joke , or English Joke.")
    query = takeCommand().lower()
    if 'english' in query:
        choiceCount=0
        englishJoke()

    elif 'hindi' in query :
        choiceCount=0
        hindiJokes()

    else:
        choiceCount+=1
        if choiceCount >3:
            speak('I think you dont want to hear jokes')
            choiceCount=0
            return False
        getJokes()