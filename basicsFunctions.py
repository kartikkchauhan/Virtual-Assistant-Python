import datetime
import os
import sys
import requests
import search_google.api
import json
from socketServer import*
from threading import *
from mainFunctions import *
from gettingJokes import *
from openingWebLinks import *
from searchGoogle import *
import dbConnection as dataBase
import getpass
from settingAlarams import *
from devMode import *
from checkingDB import *
from musicSection import *
from motionDetector import *
from webcamFace import *
from setReminder import *
from contacts import contactMain
from playYoutube import playMain
from callingMain import callingMain
from motionDetector import movementDetection

sessionUser=None

def splitString(query):
    output=query.split()
    return output

def systemQuit():
    sys.exit(0)

def startAi():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir,")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir,")   

    else:
        speak("Good Evening Sir,")  

    # faceVerification()
    usersCall()
    
camCount=0
#Verify users face
def faceVerification():
    global camCount
    global sessionUser
    speak("Let me verify your face")
    name=face_verify()
    if name == "Kartik":
        sessionUser= name
        speak("Welcome "+ name + " how can i assist you.")
        usersCall()
    elif name == False:
        camCount+=1

        if camCount>2:
            speak("I cant find your system Camera, System is shutting down.")
            systemQuit()

        speak("I cant find your system Camera, I am trying again")
        faceVerification()
    elif name == "unknown":
        speak("Please dont try to enter in someone's system, go play somewhere else.")
        systemQuit()
    elif name == "error":
        systemQuit()

def computerToSleep():
    speak("Do you really want machine to sleep")
    query = takeCommand().lower()
    if 'yes' in query:
        speak("Processing")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0 ")
    elif 'no' in query:
        speak('making rollback')
        usersCall()

def computerShutdown():
    speak("Do you really want machine to Shut down")
    query = takeCommand().lower()
    if 'yes' in query:
        speak("Processing")
        os.system('shutdown -s')
    elif 'no' in query:
            speak('making rollback')
            usersCall()


WAKE_WORDS = ['hey computer', 'okay computer','computer']

def wakeWord(text):
    global WAKE_WORDS
    text = text.lower()  # Convert the text to all lower case words
  # Check to see if the users command/text contains a wake word    
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
  # If the wake word was not found return false
    return False
def removeWakeWords(text):
    global WAKE_WORDS
    for i in range(len(WAKE_WORDS)):
        if WAKE_WORDS[i] in text:
            text=text.replace(WAKE_WORDS[i]+" ","")
    return text

#recognize the user call
def usersCall():
    trainImages=threading.Thread(target=trainFaceDectector)
    trainImages.daemon=True
    trainImages.start()

    while True:
        checkAlarm()
        query = takeCommand().lower()
        if wakeWord(query) == True:   
            query=removeWakeWords(query)
            if 'hello' in query:
                speak("hey "+sessionUser)

            elif query=='quit':
                speak('okay, Hope you like me. Bye')
                
                systemQuit()
                
            elif 'set machine state to sleep' in query:
                computerToSleep()

            elif 'computer to sleep' in query:
                computerToSleep()

            elif 'sleep this computer' in query:
                computerToSleep()

            elif 'shutdown this computer' in query:
                computerShutdown()

            elif 'search google' in query:
                searchGoogle()
                
            elif 'tell me a joke' in query:
                getJokes()

            elif 'monitor my room' in query:
                movementDetection()

            elif 'open website' in query:
                res=splitString(query)
                try:
                    name=str(res[2])
                    callWebsite(name)
                except:
                    speak("Tell ne the website name also, along with Keyword")
            elif 'set alarm' in query:
                addAlarm()
            elif 'music section' in query:
                musicHome()
            elif 'open developer mode' in query:
                openDev()
            elif 'set reminder' in query:
                blockWords=['hey','please','hello','can','you','for me']

                for i in range(len(blockWords)):
                    if blockWords[i] in query:
                        query=query.replace(blockWords[i],'')

                setRem(query)
            elif 'contact' in query:
                contactMain(query)

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'who is' in query or 'what is' in query:
                query = query.replace("who is ", "")
                query = query.replace("what is ", "")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to results")
                    speak(results)
                except Exception as e:
                    pass
            elif 'play' in query and 'on youtube' in query:
                query = query.replace("play ", "")
                query = query.replace("on youtube", "")
                playMain(query)

            elif 'connect call' in query or 'make call' in query:
                query=query.replace('connect call ','')
                query=query.replace('make call ','')
                callingMain(query)
            
            else:
                checkQuestion(query)

        
            

