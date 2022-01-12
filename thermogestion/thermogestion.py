from protocol.ProtocolManager import protocolManager

from ConfigParser.ConfigParser import ConfigParser
import logging
import threading
 
 
class thermogestion:

	def __init__(self)-> None:
		logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,  datefmt="%H:%M:%S")
		self.config = ConfigParser()
		logging.info("Starting protocol manager...")
		x = threading.Thread(target=protocolManager(self.config.get_config()), args=(1,))

thermogestion()
