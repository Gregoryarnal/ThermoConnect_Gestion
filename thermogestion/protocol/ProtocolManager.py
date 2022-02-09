# from protocol.Radio.RadioProtocol import radioProtocol
# import configparser
import logging
from time import sleep, time

# from SensorGesture.SensorManager import SensorManager
from protocol.Wifi.Tuya import Tuya
from protocol.Rest.RestServer import RestServer
from protocol.MQTT.mqtt import mqtt

class protocolManager(object):
	radio = None
	wifi = None
	config = None
	rest = None
	mqtt = None
 
	def __init__(self, config):
		logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,  datefmt="%H:%M:%S")
		self.config = config
  		# sensorManager = SensorManager(config)
  
		while True:
			if self.rest is None:
				self.rest = RestServer(self)
				self.rest.start()
    
			if self.mqtt is None:
				self.mqtt = mqtt(self)
				self.mqtt.run()
				
			if self.config['Protocol']['wifi']:
				if self.wifi is None:
					self.wifi = Tuya()
					self.rest.add_listener(self.wifi)
				# self.wifi.change_status()
				# sleep(1)
