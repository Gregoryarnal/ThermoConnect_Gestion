from protocol.Radio.RadioProtocol import radioProtocol


class protocolManager(object):
    radio = None
    config = None

    def __init__(self, config):
        self.config = config
        while True:
            if self.config['Protocol']['radio']:
            #if True:
                # Modifier quand le catch retournera un bodySensor
                if self.radio is None:
                    self.radio = radioProtocol()
                self.radio.catch()
