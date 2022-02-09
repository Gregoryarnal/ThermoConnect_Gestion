from glob import glob
from flask import Flask, json
import threading
import time
companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

tuya = None
class RestServer(threading.Thread):
    
    api = Flask(__name__)
    
    def __init__(self, manager) -> None:
        threading.Thread.__init__(self)
        self.manager = manager
       
        
    def run(self):
        # self.api.run(host="192.168.1.13", port=5000) 
        self.api.run(host="172.20.10.3", port=5000) 
        
    def add_listener(self, newtuya):
        global tuya
        tuya = newtuya
        
        
    @api.route('/tuya', methods=['GET'])
    def get_socket_tuya():
        if tuya is not None:
            tuya.change_status()
            return "OK"
        else:
            return "Any Device connected..."
        
    @api.route('/getTuyaDevice', methods=['GET'])
    def get_list_device_tuya():
        if tuya is not None:
            return tuya.device_list()
        else:
            return "Any Device connected..."

