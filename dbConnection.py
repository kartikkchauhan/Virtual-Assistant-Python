import mysql.connector
import json
from mainFunctions import speak
from mainFunctions import takeCommand
import datetime


try:
    con=mysql.connector.connect(host='localhost',user='root',password='',database='ai')
    cur=con.cursor()
except Exception as e:
    print("ERROR :", e)



def setAlarm(name,time):
    try:
        output=time.split()
        tme=str(output[0])
        timeSp=tme.split(':')
        spHr=str(timeSp[0])
        if output[1] == 'p.m.' and int(spHr) < 12:

            spHr=int(spHr)+12

        elif output[1] == 'a.m.' and int(spHr) == 12:

            spHr=int(spHr)-12

        elif output[1] == 'p.m.' and int(spHr) == 12:

            spHr=int(spHr)
        

        fTime=str(spHr)+":"+timeSp[1]
        query="insert into alarms(name,time)values('"+name+"','"+fTime+"')"
        cur.execute(query)
        con.commit()
        return True
    except Exception as error:
        print("ERROR :", error)

def getAlarm():
    try:
        minutes=datetime.datetime.now().minute
        hour=datetime.datetime.now().hour
        cTime=str(hour)+":"+str(minutes)
        alaramTime=None
        query="select * from alarms where time='"+cTime+"'"
        cur.execute(query)
        for data in cur:
            alaramTime=data[2]
        return alaramTime
    except Exception as error:
        print("ERROR :",error)

def deleteAlarm(time):
    query="delete from alarms where time='"+time+"'"
    cur.execute(query)
    con.commit()

def checkQues(ques):
    answer=None
    query="select * from general_questions where question='"+ques+"'"
    cur.execute(query)
    for data in cur:
        answer=data[2]
    return answer

def setQuestion(ques):
    ans_count=0
    counts= 0
    query="select * from asked_questions where question='"+ques+"'"
    cur.execute(query)
    for data in cur:
        ans_count+=1
        counts=data[2]

    if ans_count == 1:
        counts=int(counts)+1

        query="update asked_questions set count='"+str(counts)+"' where question='"+ques+"'"
        cur.execute(query)
        con.commit()
        return counts

    elif ans_count == 0:
        ans_count=str(ans_count)
        query="insert into asked_questions(question,count)values('"+ques+"','"+ans_count+"')"
        cur.execute(query)
        con.commit()
        return counts

def addNewQuestion(ques,answer):
    answer=answer.replace("'",'')
    
    query="insert into general_questions(question,answer)values('"+ques+"','"+answer+"')"
    cur.execute(query)
    con.commit()
    speak('thanks for helping me in increasing my knowledge.')

def updateCallLogs(phone,callType):
    dateTime=None
    ids=None
    rings=None

    if callType=="outgoing":
        query="insert into call_logs(phone,call_type)values('"+phone+"','"+callType+"')"
        cur.execute(query)
        con.commit()
    else:
        check="select * from call_logs where phone='"+phone+"' and call_type='"+callType+"' order by id desc limit 1"
        cur.execute(check)
        for data in cur:
            ids=data[0]
            dateTime=data[3]
            rings=data[4]

        
        now = datetime.datetime.now().replace(microsecond=0)
        
        nowArray=str(now).split(' ')
        if dateTime !='' and dateTime!=None:
            dateTime=str(dateTime).split(' ')
            if dateTime[0]==nowArray[0]:
                time1=nowArray[1]
                time2=dateTime[1]
                FMT = '%H:%M:%S'    
                diff = datetime.datetime.strptime(time1, FMT).date()- datetime.datetime.strptime(time2, FMT).date()
                diff=str(diff).split(':')
                if int(diff[0])==0 and int(diff[1])<=10:
                    rings+=1
                    query="update call_logs set ring_counts='"+str(rings)+"' where id='"+str(ids)+"'"
                    cur.execute(query)
                    con.commit()

                    speak(f"This caller called you {rings} times in last 10 minutes.")
                else:
                    query="insert into call_logs(phone,call_type)values('"+phone+"','"+callType+"')"
                    cur.execute(query)
                    con.commit()
            else:
                query="insert into call_logs(phone,call_type)values('"+phone+"','"+callType+"')"
                cur.execute(query)
                con.commit()
        else:
            query="insert into call_logs(phone,call_type)values('"+phone+"','"+callType+"')"
            cur.execute(query)
            con.commit()

def checkExistingContact(phone):
    name=None
    query="select * from contacts where phone='"+phone+"'"
    cur.execute(query)
    for data in cur:
        name=data[1]
    return name

def getphoneFromLogs():
    phone=None
    query="select * from call_logs order by id desc limit 1"
    cur.execute(query)
    for data in cur:
        phone=data[1]
    return phone

def saveContact(name,phone):
    query="insert into contacts(name,phone)values('"+name+"','"+phone+"')"
    cur.execute(query)
    con.commit()

    query="update call_logs set phone='"+name+"' where phone='"+phone+"'"
    cur.execute(query)
    con.commit()

    return True

def getCountryCode(name):
    name="%"+name+"%"
    code=None
    query="select * from countries where name like '"+name+"' limit 1"
    cur.execute(query)
    for data in cur:
        code=data[2]
    return code

def fetchContactsPhone(name):
    phone=None
    name="%"+name+"%"

    print(name)

    query="select * from contacts where name like '"+name+"' limit 1"
    cur.execute(query)
    for data in cur:
        phone=data[2]
    return phone