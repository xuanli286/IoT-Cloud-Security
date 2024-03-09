import paho.mqtt.client as mqtt
import ssl

def on_connect(client, userdata, flags, rc):
    print("Connected to AWS IoT: " + str(rc))
    publishData()

client = mqtt.Client()
client.on_connect = on_connect
client.tls_set(ca_certs='./rootCA.pem', certfile='./certificate.pem.crt', keyfile='./private.pem.key', tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("a1u7o7eqy96ipy-ats.iot.us-east-1.amazonaws.com", 8883, 60)

def publishData():
    print("Publishing data...")
    with open("./data.cpabe", "rb") as file:
        file_content = file.read()
        client.publish("raspi/data", payload=file_content, qos=0, retain=False)
    print("Data published")

client.loop_forever()