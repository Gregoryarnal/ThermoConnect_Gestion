from protocol.Radio.RadioProtocol import radioProtocol
import configparser


class protocolManager(object):
    radio = None
    #config = configparser.ConfigParser()

    def __init__(self):

        while True:
            #if self.config['Type']['Radio']:
            if True:
                # Modifier quand le catch retournera un bodySensor
                if self.radio is None:
                    self.radio = radioProtocol()
                self.radio.catch()