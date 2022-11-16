from mainFunctions import speak
from mainFunctions import takeCommand
from dbConnection import getphoneFromLogs
from dbConnection import saveContact
from dbConnection import getCountryCode

attempts = 0

def saveThisContact():
    global attempts

    speak("okay, tell me the name.")
    name = takeCommand().lower()

    speak(f"{name}, shoud i save this?")

    res = takeCommand().lower()

    if 'yes' in res:
        phone=getphoneFromLogs()
        result=saveContact(name,phone)

        if result == True:
            speak(f"contact added successfully as {name}")
    else:
        if attempts>2:
            speak("i think you dont want to save contact. Discarding changes.")
        else:
            attempts+=1
            saveThisContact()

def saveThisContactAs(name):
    phone=getphoneFromLogs()
    result=saveContact(name,phone)

    if result == True:
        speak(f"contact added successfully as {name}")

def takePhoneNumber():
    speak("tell me phone number")
    phone=takeCommand().lower()

    if phone==None:
        takePhoneNumber()
    speak(f"Please confirm the number, {phone}")

    res=takeCommand().lower()

    if 'confirm' in res or 'yes' in res:
        return phone
    elif 'again' in res or 'no' in res:
        takePhoneNumber()
    elif 'exit contacts' in res:
        speak("Okay discarding changes.")
    else:
        speak("sorry, Contacts service ran into some problem.")

def takeContactName():
    speak("Okay tell me the name")
    name=takeCommand().lower()
    if name==None:
        takeContactName()
    speak(f"Please confirm the name, {name}")

    res=takeCommand().lower()

    if 'confirm' in res or 'yes' in res:
        return name
    elif 'again' in res or 'no' in res:
        takeContactName()
    elif 'exit contacts' in res:
        speak("Okay discarding changes.")
    else:
        speak("sorry, Contacts service ran into some problem.")

def takeContactCountry(phone):
    speak("Okay tell me the country")
    country=takeCommand().lower()
    if country==None:
        takeContactCountry(phone)
    speak(f"Please confirm the country {country}")

    res=takeCommand().lower()

    if 'confirm' in res or 'yes' in res:
        code=getCountryCode(country)
        phone=code+phone
        return phone
    elif 'again' in res or 'no' in res:
        takeContactCountry(phone)
    elif 'exit contacts' in res:
        speak("Okay discarding changes.")
    else:
        speak("sorry, Contacts service ran into some problem.")

def createNewContact():
    phone=takePhoneNumber()
    name=takeContactName()
    phone=phone.replace(' ','')
    finalContact=takeContactCountry(phone)

    phone=getphoneFromLogs()
    result=saveContact(name,finalContact)

    if result == True:
        speak(f"contact added successfully as {name}")


mainAttempt=0

def contactMain(query):
    global mainAttempt

    if 'save this contact as' in query:
        name=query.split('as')
        name=name[1]
        saveThisContactAs(name)
    elif 'save this contact' in query:
        saveThisContact()
    elif 'create new contact' in query:
        createNewContact()
    elif 'exit contacts' in query:
        speak("Okay.")
    else:
        if mainAttempt>2:
            speak("closing contacts.")
        else:
            mainAttempt+=1
            speak("please say again what i have to do in contacts.")
            query=takeCommand().lower()
            contactMain(query)