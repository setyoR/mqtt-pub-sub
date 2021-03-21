import csv
import paho.mqtt.client as mqtt
import time
import numpy as np
suhu = ["TC1", "TC2", "TC3", "TC4", "TC5"]

TC = np.zeros(5)
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, message):
    global TC
    temp =float(message.payload.decode("utf-8"))
    for j in range(5):
        if str(message.topic)=="TC("+str(j+1)+")":
            TC[j] = temp
                                    

broker_IP = "127.0.0.1"
client = mqtt.Client("P2")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_IP, 1883, 60)
client.subscribe("#")
rc = 0
while rc ==0 :
    client.loop()
    print(TC)

    time.sleep(1)

