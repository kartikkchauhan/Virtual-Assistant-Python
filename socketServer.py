#Imports Modules
import socket
import time
import pyttsx3
from dbConnection import *
from plyer import notification


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('rate', 130)     # setting up new voice rate
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def socketServer():
    listensocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Port = 9876
    maxConnections = 1
    IP = socket.gethostname() #Gets Hostname Of Current Macheine

    listensocket.bind(('',Port))

    #Opens Server
    listensocket.listen(maxConnections)
    print("Server started at " + IP + " on port " + str(Port))

    #Accepts Incomming Connection
    # (clientsocket, address) = listensocket.accept()
    # print("New connection made!")

    # running = True


    #Main
    while True:
        (clientsocket, address) = listensocket.accept()
        message = clientsocket.recv(1024).decode() #Receives Message
        msgArray=message.split('#')
        if msgArray[0]=="call incoming":
            caller=checkExistingContact(msgArray[1])
            if caller == None:
                speak(f"call incomming from unknown number.")
                updateCallLogs(msgArray[1],"incomming")
            else:
                speak(f"call incomming from {caller}.")
                updateCallLogs(caller,"incomming")

            

        elif msgArray[0]=="call started":
            caller=checkExistingContact(msgArray[1])
            if caller == None:
                speak(f"call connected with unknown number.")
                updateCallLogs(msgArray[1],"outgoing")
            else:
                speak(f"call connected with {caller}.")
               
                updateCallLogs(caller,"outgoing")

        elif msgArray[0]=="call ended":
            caller=checkExistingContact(msgArray[1])
            if caller == None:
                speak(f"call ended")
                
                updateCallLogs(msgArray[1],"outgoing")
            else:
                speak(f"call ended.")
               

        else:
            speak(f"Incomming messege on your mobile from{msgArray[1]}")
           
        # print(f"New Message From {address} : {message}") #Prints Message

        # if not message == "":
        #    print(message) #Prints Message
        
        #Closes Server If Message Is Nothing (Client Terminated)
        # elif message =="":
        #     clientsocket.close()
        #     # running = False

if __name__ == "__main__":
    socketServer()