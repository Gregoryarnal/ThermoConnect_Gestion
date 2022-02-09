# python3.6

import random
import threading
from flask import Flask
import tinytuya


from paho.mqtt import client as mqtt_client


class mqtt(object):
    
    api = Flask(__name__)
    
    def __init__(self, manager) -> None:
        # threading.Thread.__init__(self)
        self.t=threading.Thread(target=self._run)
        self.broker = '152.228.213.48'
        self.manager = manager
        self.port = 1883
        self.topic = "python/mqtt"
        self.topic = "test"
        self.client_id = f'python-mqtt-{random.randint(0, 100)}'
        self.username = 'test'
        self.password = 'test'


    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        self.client = mqtt_client.Client(self.client_id)
        self.client.username_pw_set(self.username, self.password)
        self.client.on_connect = on_connect
        self.client.connect(self.broker, self.port)
        return self.client

    def test(self, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        self.manager.wifi.change_status()

    def subscribe(self, sclient: mqtt_client):
        def on_message(client, userdata, msg):
            # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            self.test(msg)
            # self.device.turn_on(switch=1)

        self.client.subscribe(self.topic)
        self.client.on_message = on_message

    def _run(self):
        client = self.connect_mqtt()
        self.subscribe(client)
        client.loop_forever()
        
    def run(self):
        self.t.start()
