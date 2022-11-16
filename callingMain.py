import socket
from dbConnection import fetchContactsPhone
from mainFunctions import speak

IP=socket.gethostname()


def makeCall(phone):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.1.6', 9912))
    s.listen(5)

    clientsocket, address = s.accept()
    print(f"connection from {address} has been established!")
    clientsocket.send(phone.encode())
    clientsocket.close()

def getPhoneNumber(name):
    phone=fetchContactsPhone(name)
    return phone

def callingMain(query):
    task=query
    if 'with' in task:
        task=task.replace('with ','')
    elif 'to' in task:
        task=task.replace('to ','')
    
    print (task)

    phone=getPhoneNumber(task)

    if phone==None:
        speak("contact not found.")
    else:
        speak(f"calling {task}.")
        makeCall(phone)
        

    
    
