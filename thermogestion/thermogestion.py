
from ConfigParser.ConfigParser import ConfigParser


class thermogestion:

    def __init__(self) -> None:
        self.config = ConfigParser()
        print(self.config.get_config())
        
thermogestion()