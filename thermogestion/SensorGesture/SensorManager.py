from inspect import isdatadescriptor
import logging
import requests
from apscheduler.schedulers.background import BackgroundScheduler
import time
from apscheduler.triggers.cron import CronTrigger

class SensorManager(object):
    last_bs = None 
    def __init__(self, config) -> None:
        logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,  datefmt="%H:%M:%S")
        logging.info("SensorManger starting ... ")
        super().__init__()
        self.config = config
        print(config)
        self.bodySensor = []
        scheduler = BackgroundScheduler(timezone='Europe/Paris', job_defaults={'max_instances': 100, 'misfire_grace_time': 30})

        scheduler.add_job(self.send_next_iteration, "interval", seconds=10)
        scheduler.start()
        
    def set_bs(self, bs):
        if bs['idSensor'] not in (x['id'] for x in self.bodySensor):
            data = {}
            data['id'] = bs['idSensor']
            data['last_bs'] = bs
            data["sync_status"] = False
            self.bodySensor.append(data)
        else : 
            for el in self.bodySensor:
                if bs["idSensor"] == el['id']:
                    el["last_bs"] = bs
                    el["sync_status"] = False
            
    
    def send_next_iteration(self):
        logging.info("Sync last data")
        for el in self.bodySensor:
            if not el["sync_status"]:
                logging.debug("http://"+self.config["ip"]+":"+self.config["port"] + '/addTerrariumData')
                response = requests.post("http://"+self.config["ip"]+":"+self.config["port"] + '/addTerrariumData', json=el["last_bs"])
                if response.status_code == 200:
                    logging.info("send")
                    el["sync_status"] = True
                else:
                    logging.info("fail")