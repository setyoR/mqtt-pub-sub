import csv
import paho.mqtt.client as mqtt
import time



with open('C:/Users/Asus/thornhill-Copy1.csv', newline = '')as f:
    reader =csv.reader(f)
    data =[tuple(row[:]) for row in reader]

broker_IP = "127.0.0.1"
port = 1883
Start=0
topik = data[0]
nilai = data[1:]
jumlah = len(data)
banyak_topik = len(topik)


def on_connect(client, userdata, flags,rc):
    print("Connected with result code"+str(rc))
    if rc == 0:
        print("connected OK")
    else :
        print("Bad Connecttion Returned code", rc)
def on_disconnect(client, userdata, flagas, rc=0):
    print("Disconnect, result code:", str(rc))
def on_message(client, userdata, message):
    global Start
    temp = float(message.payload.decode("utf-8"))
    if str(message.topic) == "Start":
        Start = temp            

client = mqtt.Client("P1")
client.connect(broker_IP, port,60)
client.on_message = on_message
client.on_connect = on_connect
client.loop_start()

a=int(0)
while True :
    client.subscribe("Start")
    if Start == 1 :
        #for k in nilai:
        k = nilai[a]
        for j in range(banyak_topik):
            client.publish(topik[j],k[j])
        a=a+1
    if a == len(nilai) :
        print("done")
        break
        
    time.sleep(1)

        #client.loop_stop()
        #client.disconnect()
