import argparse
from datetime import datetime
import struct
import sys
import time
import traceback
import requests
import pigpio
from nrf24 import *


#
# A simple NRF24L receiver that connects to a PIGPIO instance on a hostname and port, default "localhost" and 8888, and
# starts receiving data on the address specified.  Use the companion program "simple-sender.py" to send data to it from
# a different Raspberry Pi.
#
url = "http://152.228.213.48:8081"
#url = "http://192.168.1.12:8081"

class radioProtocol(object):

    nrf = None
    pi = None
    
    
    def __init__(self) -> None:

        super().__init__()
        print("Python NRF24 Simple Receiver Example.")
        # Parse command line argument.
        parser = argparse.ArgumentParser(prog="simple-receiver.py", description="Simple NRF24 Receiver Example.")
        parser.add_argument('-n', '--hostname', type=str, default='localhost', help="Hostname for the Raspberry running the pigpio daemon.")
        parser.add_argument('-p', '--port', type=int, default=8888, help="Port number of the pigpio daemon.")
        parser.add_argument('address', type=str, nargs='?', default='1SNSR', help="Address to listen to (3 to 5 ASCII characters)")

        args = parser.parse_args()
        hostname = args.hostname
        port = args.port
        address = args.address
        
        
        # Verify that address is between 3 and 5 characters.
        if not (2 < len(address) < 6):
            print(f'Invalid address {address}. Addresses must be between 3 and 5 ASCII characters.')
            sys.exit(1)
        
        # Connect to pigpiod
        print(f'Connecting to GPIO daemon on {hostname}:{port} ...')
        self.pi = pigpio.pi(hostname, port)
        if not self.pi.connected:
            print("Not connected to Raspberry Pi ... goodbye.")
            sys.exit()

        # Create NRF24 object.
        # PLEASE NOTE: PA level is set to MIN, because test sender/receivers are often close to each other, and then MIN works better.
        self.nrf = NRF24(self.pi, ce=25, payload_size=RF24_PAYLOAD.DYNAMIC, channel=100, data_rate=RF24_DATA_RATE.RATE_250KBPS, pa_level=RF24_PA.MIN)
        self.nrf.set_address_bytes(len(address))

        # Listen on the address specified as parameter
        self.nrf.open_reading_pipe(RF24_RX_ADDR.P1, address)
        
        # Display the content of NRF24L01 device registers.
        self.nrf.show_registers()
    
    
    def catch(self):
        now = datetime.now()
        
        # Read pipe and payload for message.
        pipe = self.nrf.data_pipe()
        payload = self.nrf.get_payload()    

        # Resolve protocol number.
        protocol = payload[0] if len(payload) > 0 else -1            

        hex = ':'.join(f'{i:02x}' for i in payload)

        # Show message received as hex.
        print(f"{now:%Y-%m-%d %H:%M:%S.%f}: pipe: {pipe}, len: {len(payload)}, bytes: {hex}")

        # If the length of the message is 9 bytes and the first byte is 0x01, then we try to interpret the bytes
        # sent as an example message holding a temperature and humidity sent from the "simple-sender.py" program.
        if len(payload) == 9 and payload[0] == 0x01:
            values = struct.unpack("<Bff", payload)
            # print(f'Protocol: {values[0]}, temperature: {values[1]}, humidity: {values[2]}')
            # print("Send to cloud....")
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            bodySensor = {
                "bodyConnexion":{
                    "token" : self.bodySensor.token
                },
                "idTerrarium": self.bodySensor.idTerrarium,
                "date": date,
                "value": round(values[1],2),
                "idSensor" : self.bodySensor.idSensor,
                "Type": "temp"
                }

            # response = requests.post(url + '/addTerrariumData', json=query)
            
            return bodySensor
    
    def _prepare_request(self):
        pass
        
    def close(self):
        traceback.print_exc()
        self.nrf.power_down()
        self.pi.stop()

