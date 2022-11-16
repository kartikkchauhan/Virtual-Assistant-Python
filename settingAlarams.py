import datetime
from dbConnection import *
from basicsFunctions import *
import string
import soundfile as sf
import soundcard as sc

def setName():
    length=7
    CONSONANTS = "".join(set(string.ascii_lowercase))
    word = ""
    for i in range(length):
            word += random.choice(CONSONANTS)
    return word

def setTime():
    count=0
    speak("tell me the time of alarm")
    atime=takeCommand().lower()
    if atime == None:
        if count > 3:
            speak("canceling alaram")
            usersCall()
        count+=1
        setName()
    elif  'none' in atime:
        if count > 3:
            speak("canceling alaram")
            usersCall()
        count+=1
        setName()
    else:
        return atime

def addAlarm():
    aName=setName()
    aTime=setTime()
    res=setAlarm(aName,aTime)
    if res == True:
        output=aTime.split()
        tme=str(output[0])
        timeSp=tme.split(':')
        speak("Got it! your alarm is set for "+str(timeSp[0])+" "+str(timeSp[1])+" "+str(output[1]))
    else:
        speak("Error")

def checkAlarm():
    data=getAlarm()
    minutes=datetime.datetime.now().minute
    hour=datetime.datetime.now().hour
    cTime=str(hour)+":"+str(minutes)
    if cTime == data:
        alarm=threading.Thread(target=alarmTone)
        alarm.daemon=True
        alarm.start()
        deleteAlarm(data)


def alarmTone():
    try:
        default_speaker = sc.default_speaker()
        samples, samplerate = sf.read('tones/alarm.wav')

        for i in range(5):
            default_speaker.play(samples, samplerate=samplerate)

    except Exception as e:
        print(e)

