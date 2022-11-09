from tkinter import *
from PIL import Image, ImageTk
from paho.mqtt import client as mqtt_client
import json
from random import randint
 
# https://mntolia.com/10-free-public-private-mqtt-brokers-for-testing-prototyping/ 

broker = 'broker.hivemq.com'
port = 1883
topic = "api/request"
#topic_sub = "api/notification/37/#"
# generate client ID with pub prefix randomly
client_id = 'ID'+str(randint(0,1000))
#username = 'your username'
#password = 'your password'
deviceId = 'ID'+str(randint(0,1000))
 
 
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
 
def publish(client,status):
    # msg = f"messages: {msg_count}"
    msg = "{\"action\":\"command/insert\",\"deviceId\":\""+deviceId+"\",\"command\":{\"command\":\"LED_control\",\"parameters\":{\"led\":\""+status+"\"}}}"
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Mensamge `{msg}` enviada para o topico `{topic}`")
    else:
        print(f"Erro eu enviar mensagem para o topico {topic}")
 
 
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Recieved '{msg.payload.decode()}' from '{msg.topic}' topic")
        y = json.loads(msg.payload.decode())
        if y["action"] == "notification/insert" :
            temp = str(y["notification"]["parameters"]["temp"])
            hum = str(y["notification"]["parameters"]["humi"])
            print("temperature: ",temp,", humidity:",hum)
            temp_label.config(text=temp+" °C",
                            fg="black")
    
            hum_label.config(text=hum + "  %",
                            fg="black")
 
 
 
    client.subscribe(topic)
    client.on_message = on_message
 
 
window = Tk()
window.title("MQTT Dashboard")
window.geometry('395x675')
window.resizable(False,False)
window.configure(bg="white")
canvas = Canvas(window, bg="white", width=395,height=135)
canvas.place(x=0,y=0)
image = Image.open("logo.png")
image = image.resize((395,135), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
canvas.create_image(0,0,anchor=NW,image=img)
 
canvas2 = Canvas(window,width=100,height=100)
canvas2.place(x=50,y=165)
image = Image.open("tmp.png")
image = image.resize((100,100), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(image)
canvas2.create_image(0,0,anchor=NW,image=img2)
 
canvas3 = Canvas(window,width=100,height=100)
canvas3.place(x=50,y=295)
image = Image.open("hum.png")
image = image.resize((100,100), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(image)
canvas3.create_image(0,0,anchor=NW,image=img3)
 
is_on = False
 
 
# Create Label
my_label = Label(window,
                 text="OFF!",
                 bg="white",
                 fg="grey",
                 font=("Helvetica", 32))
my_label.place(x=180,y=430)
 
def switch():
    global is_on
    if is_on:
        on_button.config(image=off)
        my_label.config(text="OFF!",
                        fg="grey")
        print("LED is off now")
        publish(client,"0")
        is_on=False
    else:
        on_button.config(image=on)
        my_label.config(text="ON!",
                        fg="red")
        print("LED is On now")
        publish(client,"1")
        is_on=True
 
# Define Our Images
image = Image.open("on.png")
image = image.resize((100,60), Image.ANTIALIAS)
on = ImageTk.PhotoImage(image)

image = Image.open("off.png")
image = image.resize((100,60), Image.ANTIALIAS)
off = ImageTk.PhotoImage(image)
 
# Create A Button
on_button = Button(window, image=off, bd=0,
                   command=switch)
on_button.place(x=50,y=420)
 
 
# Create Label
temp_label = Label(window,
                 text=" °C",
                 bg="white",
                 fg="black",
                 font=("Helvetica", 32))
 
temp_label.place(x=180,y=190)
 
# Create Label
hum_label = Label(window,
                 text="  %",
                 bg="white",
                 fg="black",
                 font=("Helvetica", 32))
 
hum_label.place(x=180,y=325)
client = connect_mqtt()
subscribe(client)
client.loop_start()
 
 
window.mainloop()
client.loop_stop()