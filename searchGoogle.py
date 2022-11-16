import datetime
import os
import webview
import threading
import sys
import requests
import search_google.api
import json
import basicsFunctions as bf
from threading import *
from mainFunctions import *

countWantMore = 0

def wantMore():
    global countWantMore

    speak("Do you want to search more?")
    query=takeCommand().lower()
    if 'yes' in query:
        searchGoogle() 
    elif 'no' in query:
        speak("Closing google search")
        bf.usersCall()
    else:
        if countWantMore > 2:
            bf.usersCall()

        countWantMore +=1
        speak("please answer yes or no")
        wantMore()

def searchGoogle():
    speak('What do you want to search?')
    query=takeCommand().lower()

    if 'none' in query:
        searchGoogle()
    elif 'cancel search' in query:
        speak("google search canceled.")
        bf.usersCall()
    try:
        buildargs = {
        'serviceName': 'customsearch',
        'version': 'v1',
        'developerKey': 'Paste Your Key'
        }

        # Define cseargs for search
        cseargs = {
        'q': query,
        'cx': '007882365152320759672:ooqwztudn8q',
        'num': 3
        }
        results = search_google.api.results(buildargs, cseargs)
        links = results.links
        speak("here are your results")
        #print(links)
        
        for link in links:
            webview.create_window(link, link)
        webview.start()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        
    wantMore()