from datetime import *
from dbConnection import *
from basicsFunctions import *
import time
import pandas as pd
import pendulum 

count=0
import time

def isTimeFormat(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except ValueError:
        return False
        
def setDate():
    global count
    if count >=3:
        speak('Are you playing with me? If you are, then please stop it.')

    speak('okay tell me the date.')
    date=takeCommand().lower()
    fdate=''
    if date == None:
        count+=1
        setDate() 

    if 'today' in date:
        fdate=pd.to_datetime('today').strftime('%d-%m-%y')
    elif 'tommorow' in date:
        fdate=pendulum.tomorrow().strftime('%d-%m-%y')
    
    
    print(fdate)

def setRem(query):
    print(query)
    manQuery=query.split()
    if len(manQuery) == 4:
        if 'tomorrow' in manQuery:
            if manQuery[len(manQuery)-1]=='tomorrow':
                speak("can you please tell me the time of reminder, because without time i cant set any reminder.")
                timeQuery = takeCommand().lower()
                findingTime=timeQuery.split()
                print(findingTime)
                time=""
                for t in findingTime:
                    if isTimeFormat(t):
                        time=t
                print(time)
                if time !="":
                    if 'a.m.' in findingTime:
                        speak("setting reminder for tomorrow "+ time +"a.m.")
                    elif 'p.m.' in findingTime:
                        speak("setting reminder for tomorrow "+ time +"p.m.")
                else:
                    speak("Sorry, unable to set reminder.")

        elif 'today' in manQuery:
            if manQuery[len(manQuery)-1]=='today':
                 speak("Do yo want to set reminder for today ?")

    elif len(manQuery) == 2:
        if all(word in 'set reminder' for word in manQuery):
            speak("set reminder is the command which i understand for setting reminder , for example, please set reminder for today.")

    elif len(manQuery) == 6:
        if all(word in 'day after tomorrow' for word in manQuery):
            speak("Do yo want to set reminder for day after tomorrow")
        elif 'tomorrow' in manQuery:
            if isTimeFormat(manQuery[4]):
                speak("Do yo want to set reminder for tomorrow "+manQuery[4] + manQuery[5])
            elif isTimeFormat(manQuery[3]):
                speak("Do yo want to set reminder for tomorrow "+manQuery[3] + manQuery[4])
        elif 'today' in manQuery:
            if isTimeFormat(manQuery[4]):
                qtime=manQuery[4].split(':')
                if manQuery[5] =='p.m.':
                    hr=int(qtime[0])+12
                elif  manQuery[5] =='a.m.':
                    hr=int(qtime[0])

                mint=qtime[1]
                cHr=datetime.datetime.now().hour
                cMint=datetime.datetime.now().minute
                if int(hr)>int(cHr):
                    speak("Do yo want to set reminder for today "+manQuery[4] + manQuery[5])
                if int(hr)==int(cHr):
                    if int(mint) > int(cMint):
                        speak("Do yo want to set reminder for today "+manQuery[4] + manQuery[5])
                    elif int(mint) < int(cMint):
                        speak("Please tell me the valid time.")
                    elif int(mint) == int(cMint):
                        speak("you cant set reminder for current time.")
                if int(hr)<int(cHr):
                    speak("Please tell me the valid time.")

            elif isTimeFormat(manQuery[3]):
                qtime=manQuery[3].split(':')
                if manQuery[4] =='p.m.':
                    hr=int(qtime[0])+12
                elif  manQuery[4] =='a.m.':
                    hr=int(qtime[0])
                mint=qtime[1]
                cHr=datetime.datetime.now().hour
                cMint=datetime.datetime.now().minute
                if int(hr)>int(cHr):
                    speak("Do yo want to set reminder for today "+manQuery[3] + manQuery[4])
                if int(hr)==int(cHr):
                    if int(mint) > int(cMint):
                        speak("Do yo want to set reminder for today "+manQuery[3] + manQuery[4])
                    elif int(mint) < int(cMint):
                        speak("Please tell me the valid time.")
                    elif int(mint) == int(cMint):
                        speak("you cant set reminder for current time.")
                if int(hr)<int(cHr):
                    speak("Please tell me the valid time.")
            
    elif len(manQuery)== 8:
        if 'day' and 'after' and 'tomorrow' and (('a.m.' or 'p.m.') or ('am'or'pm')) in manQuery:

            if isTimeFormat(manQuery[6]):
                speak("Do yo want to set reminder for day after tomorrow "+manQuery[6] + manQuery[7])
            elif isTimeFormat(manQuery[3]):
                speak("Do yo want to set reminder for day after tomorrow "+manQuery[3] + manQuery[4])