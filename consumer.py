import time
import paho.mqtt.client as mqtt
import ssl
import json

def on_connect(client, userdata, flags, rc):
    print("Connected to AWS IoT: " + str(rc))
    client.subscribe("raspi/data")  # Subscribe to the desired topic upon connection

def on_message(client, userdata, msg):
    print("Received message: " + msg.payload.decode())
    write_to_file(msg.payload.decode())  # Call function to write message to a text file

def write_to_file(message):
    with open("received_data.txt", "a") as file:
        file.write(message + "\n")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message  # Assign the on_message callback function
client.tls_set(ca_certs='./rootCA.pem', certfile='./certificate.pem.crt', keyfile='./private.pem.key', tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("a1u7o7eqy96ipy-ats.iot.us-east-1.amazonaws.com", 8883, 60)

client.loop_forever()