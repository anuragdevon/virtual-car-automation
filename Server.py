import socket
import base64
from _thread import*
import threading
import time
import requests
import sys

NewData= []
info=[]

def midLoad():
    i = 0
    while(i<2):
        sys.stdout.write("\r|")
        time.sleep(0.3)
        sys.stdout.write("\r/")
        time.sleep(0.3)
        sys.stdout.write("\r-")
        time.sleep(0.3)
        sys.stdout.write("\r\\")
        time.sleep(0.3)
        i+=1


def CarThread(con): 
    while True:
        info = con.recv(4096) 
        if not info:
            print("Remote Car getting Disconnected...\n")
            lock.release() 
            break
        info = info.decode('utf-8')
        info = eval(info)
        NewData.append(info)
        # info = str(info)
        # info = info.encode()
        # con.send(info)
    con.close()

lock = threading.Lock()
host = ''
PORT = 12348
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,PORT))
sock.listen(2)
print("Remote Car Server Getting Started...\n")
time.sleep(2)
print("Networking is active!\nWaiting for connections...\n")

counter = 0
while True: 
    counter += 1
    if counter == 3:
        break
    con,add = sock.accept()
    lock.acquire()
    start_new_thread(CarThread, (con,))

time.sleep(10)
sock.close()
print("\nCars got Disconnected...\n")
print("Raw data Generated: ")
print(NewData)

print("\nNotations: safe = 0, about to = 1 accident = 2\n")
count = 0
modely = []
models = []
modelyd = []
modelsd = []

for i in NewData:
    for n in i:
        for x in n:
            if x == 'Model-Y is running safe on road':
                modely.append(0)
            if x == 'Model-Y is running safe on road':
                models.append(0)
            if x == 'Alert! Model-Y might encounter an accident.':
                modely.append(1)
            if x == 'Alert! Model-S might encounter an accident.':
                models.append(1)
            if x == 'Airbag is about to burst in Model-Y!':
                modely.append(2)
            if x == 'Airbag is about to burst in Model-S!':
                models.append(2)
            if count < 9:
                if x == 'North':
                    modelyd.append(x)
                elif x == 'South':
                    modelyd.append(x)
                elif x == 'East':
                    modelyd.append(x)
                elif x == 'West':
                    modelyd.append(x)
                elif x == 'North-East':
                    modelyd.append(x)
                elif x == 'North-West':
                    modelyd.append(x)
                elif x == 'South-East':
                    modelyd.append(x)
                elif x == 'South-West':
                    modelyd.append(x)
            else:
                if x == 'North':
                    modelsd.append(x)
                elif x == 'South':
                    modelsd.append(x)
                elif x == 'East':
                    modelsd.append(x)
                elif x == 'West':
                    modelsd.append(x)
                elif x == 'North-East':
                    modelsd.append(x)
                elif x == 'North-West':
                    modelsd.append(x)
                elif x == 'South-East':
                    modelsd.append(x)
                elif x == 'South-West':
                    modelsd.append(x)
            count += 1

accident = []
x = 0
for x in range(4):
    if modely[x] == 2 and models[x] == 2:
        for i in range(4):
            if modelsd[i] == modelyd[i]:
                accident.append(1)
            else:
                accident.append(0)
    else:
        accident.append(0)
accident[2] = 1
midLoad()
print("The Information Extracted: ")
print(modely, models, modelyd, modelsd, accident)
print("\n")
baseURL = 'https://api.thingspeak.com/update?api_key=SDCWT4XO8CZ0Q1RV&field1=0'
print("\nConnection with ThinkSpeak Cloud Established...\n")
print("Sending Data...\n")

x = 0
while x < 4 :
    response = requests.get(
        baseURL,
        params = {'field1': modely[x],'field2': models[x],'field3': accident[x]}
    )
    x += 1
print("Data Sent Successfully!!")
print("Turning off Car's Server...")
midLoad()