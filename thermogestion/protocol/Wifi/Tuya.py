import tinytuya


class Tuya(object):
    
    def __init__(self) -> None:
        self.device = tinytuya.OutletDevice('bf26b01596ec63efd3xejb', '192.168.1.20', '38d03ddef9ec6765')
        self.device.set_version(3.3)
        
    def on(self):
        self.device.turn_on(switch=1)
    
    
    def heartbeat(self):
        self.device.heartbeat()
        
    def off(self):
        self.device.turn_off(switch=1)
        
    def device_list(self):
        return tinytuya.deviceScan(maxretry=2)
        
    def change_status(self):
        # pass
        self.device.set_status(not self.device.status()["dps"]["1"], switch=1)