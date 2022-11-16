from basicsFunctions import *
import urllib.request
import sys


if __name__ == "__main__":
    
    try:
        url="https://www.google.co.in"
        data=urllib.request.urlopen(url)
    except Exception:
        speak("Internet Not available, please try again later.")
        systemQuit()
    
    startAi() #Wishing function in basicsFunctions
    
