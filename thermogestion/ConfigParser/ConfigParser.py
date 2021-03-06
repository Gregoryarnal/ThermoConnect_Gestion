from configparser import ConfigParser as CP

class ConfigParser(object):
    
    config = {}
    
    def __init__(self) -> None:
        print("log")
        
        super().__init__()
        config = CP()
        
        
        config.read('Config.ini')

        for el in config.sections():
            if el == "Common":
                for key in config[el]:  
                    if key == 'ip':
                        self.config["ip"] = config[el][key]
                    if key == 'port':
                        self.config["port"] = config[el][key]
            elif el == "Protocol":
                for key in config[el]:  
                    if key == 'radio':
                        test = {}
                        test[key] = config[el][key]
                        self.config["Protocol"] = test

        print("self.config")
        print(self.config)
    
    def get_config(self):
        return self.config