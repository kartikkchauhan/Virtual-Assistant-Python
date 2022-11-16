import datetime
import os
import threading
import sys
import requests
import search_google.api
import json
from threading import *
from mainFunctions import *

websiteName=None
class openWebsites(Thread):
    def run(self):
        webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(websiteName)
        return super().run()

def callWebsite(name):
    global websiteName
    websiteName = name
    owObj=openWebsites()
    speak("Here is"+websiteName)
    owObj.start()
        
    