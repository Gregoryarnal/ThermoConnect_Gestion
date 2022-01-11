from protocol.Radio.RadioProtocol import radioProtocol
import configparser


class protocolManager(object):
    radio = None
    config = None

    def __init__(self, config):
        self.config = config
        while True:
            if self.config['Protocol']['Radio']:
                print("oui")
                # Modifier quand le catch retournera un bodySensor
                #if self.radio is None:
                #    self.radio = radioProtocol()
                #self.radio.catch()
