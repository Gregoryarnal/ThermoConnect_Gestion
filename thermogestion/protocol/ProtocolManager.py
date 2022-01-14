from protocol.Radio.RadioProtocol import radioProtocol
import configparser
import logging

from SensorGesture.SensorManager import SensorManager

class protocolManager(object):
	radio = None
	config = None

	def __init__(self, config):
		logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,  datefmt="%H:%M:%S")
		self.config = config
		sensorManager = SensorManager(config)
  
		while True:
			if self.config['Protocol']['radio']:
				if self.radio is None:
					self.radio = radioProtocol()
				bs = self.radio.catch()
				sensorManager.set_bs(bs)
				
