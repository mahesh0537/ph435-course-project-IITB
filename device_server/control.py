import threading
import requests
import pyaudio
import wave
import numpy as np
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 5
url = 'http://localhost:5000/api'
import re



class light:
    def __init__(self):
        self.IP = ""
        self.port = ""
        self.status = False
        self.brighness = 0
        self.color = ""
        self.connected = False
        self.default_brightness = 3
    
    def turn_on(self):
        if self.connected:
            self.status = True
            self.brighness = self.default_brightness
        else:
            print("Device not connected")
    
    def turn_off(self):
        if self.connected:
            self.status = False
            self.brighness = 0
        else:
            print("Device not connected")
    
    def set_brightness(self, brightness):
        if self.connected:
            self.brighness = brightness
        else:
            print("Device not connected")

    def set_color(self, color):
        if self.connected:
            self.color = color
        else:
            print("Device not connected")

    def connect(self, IP, port = ''):
        self.IP = IP
        self.port = port
        self.connected = True

    def disconnect(self):
        self.IP = ""
        self.port = ""
        self.connected = False

    def get_status(self):
        url = 'http://'+self.IP+'/status'
        print(url)
        r = requests.get(url)
        self.status = r
        print(str(self.status.status_code))
        a = self.status.text
        a = re.split(':', a)
        return int(a[1])

    def __call__(self):
        url = 'http://'+self.IP+'/ledbright?brighness='+str(self.brighness)
        r = requests.get(url)

class sensor:
    def __init__(self):
        self.IP = ""
        self.port = ""
        self.connected = False
        self.status = False
        self.value = 0
        self.type = ""


    def connect(self, IP, port = ''):
        self.IP = IP
        self.port = port
        self.connected = True
    
    def get_status(self):
        url = 'http://'+self.IP+'/status'
        print(url)
        r = requests.get(url)
        self.status = r.json()
        return self.status



class device:
    def __init__(self):
        self.light = light()
        self.disconnect = False

    def connect_light(self, IP, port = ''):
        self.light.connect(IP, port)

    def __call__(self):
        pass



        


