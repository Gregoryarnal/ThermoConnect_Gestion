from protocol.Radio.RadioProtocol import radioProtocol
import configparser
import logging

class protocolManager(object):
	radio = None
	config = None

	def __init__(self, config):
		logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,  datefmt="%H:%M:%S")
		self.config = config
		while True:
			if self.config['Protocol']['radio']:
				logging.info("Starting Radio protocol ... ")
				
				if self.radio is None:
					self.radio = radioProtocol()
				bs = self.radio.catch()
				if bs is not None:
					print(bs)
