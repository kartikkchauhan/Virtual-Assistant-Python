from dbConnection import *
from mainFunctions import *

def checkQuestion(ques):
    if ques != 'none':
        answer=checkQues(ques)
        if answer !=None:
            speak(answer)

        elif answer == None:
            res=setQuestion(ques)
            if res >= 1:
                addAskedQues(ques)
            else:
                speak("Seems i dont have answer for this.")

def tellAnswer(ques):
    loopCount = 0
    speak('okay, tell me the answer of,'+ques)
    answer=takeCommand().lower()
    if 'none' in answer:
        if loopCount > 3:
            speak("i think you dont want to answer.")

        loopCount+=1
        tellAnswer(ques)
    else:
        speak(answer+'. can i save this answer? or you want to change it? ')
        uRes=takeCommand().lower()
        if 'none' in uRes:
            speak('there is no reply from your side i am not saving this answer.')
        elif 'save' in uRes:
            addNewQuestion(ques,answer)
        elif 'change' in uRes:
            speak('do you want to write, or say answer again')
            uRes=takeCommand().lower()
            if 'write' in uRes:
                speak('okay write your answer now')
                answer=input('answer :')
                speak(answer+' can i save this answer now?')
                uRes=takeCommand().lower()
                if 'yes' in uRes:
                    addNewQuestion(ques,answer)
                else:
                    speak('answer not saved.')
            elif 'say' in uRes:
                speak('onaky, tell me the answer now.')
                answer=answer=takeCommand().lower()
                if 'none' in answer:
                    speak("i think you dont want to answer.")
                else:
                    speak(answer+' can i save this answer now? ')
                    uRes=takeCommand().lower()
                    if 'yes' in uRes:
                        addNewQuestion(ques,answer)
                    else:
                        speak('answer not saved.')

def addAskedQues(ques):
    loopCount=0
    speak("i dont have any answer of this command, would you like to tell me the answer?")
    uAnswer=takeCommand().lower()
    if 'none' in uAnswer:
        if loopCount > 3:
            speak("i think you dont want to answer.")
        
        loopCount+=1
        addAskedQues(ques)
    elif 'yes' in uAnswer:
        tellAnswer(ques)
    elif 'no' in uAnswer:
        speak('okay, no problem')
    else:
        speak('please answer YES or NO')
        addAskedQues(ques)