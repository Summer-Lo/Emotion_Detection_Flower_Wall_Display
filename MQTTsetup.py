import paho.mqtt.client as mqtt
import time
import json

def mqtt_client_setup(server):
    client = mqtt.Client()
    client.connect(server,1883,60) # server = 'ia.ic.polyu.edu.hk'
    return client


def mqtt_publish(client,topic,mqtt_message): #topic = "iot/sensor"
    result = client.publish(topic, mqtt_message)
    status = result[0]
    if status == 0:
        print(f"Send `{mqtt_message}` to topic `{topic}`")      # Print the published message and topic
    else:
        print(f"Failed to send message to topic {topic}")    
