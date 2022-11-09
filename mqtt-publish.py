from paho.mqtt import client as mqtt_client
from random import randint
import time
import json

broker = 'broker.hivemq.com'
port = 1883
topic = "api/request"
# generate client ID with pub prefix randomly
client_id = 'ID'+str(randint(0,1000))
#username = 'your username'
#password = 'your password'
deviceId = 'D1'+str(randint(0,1000))

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc==0:
            print("Conectado ao MQTT broker")
        else:
            print("Falha ao conectar, codigo de erro: %d", rc)
 
 
    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
 
def publish(client):
    
    temp = str(randint(20,40))
    hum = str(randint(0,100))

    msg = "{\"action\":\"notification/insert\",\"deviceId\":\""+deviceId+"\",\"notification\":{\"notification\": \"temperature\",\"parameters\":{\"temp\":" + temp + ",\"humi\":" + hum + "}}}"
    result = client.publish(topic,msg)
    msg_status = result[0]
    if msg_status ==0:
        print(f"Mensagem : {msg} enviada para o topico {topic}")
    else:
        print(f"Falha ao enviar a mensagem para o topico {topic}")
 

def main():
    client = connect_mqtt()
    client.loop_start()
    while(1):
        publish(client)
        time.sleep(2)
    

if __name__ == '__main__':
    main()