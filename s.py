import socket
from time import time
import numpy as np
 
s = socket.socket()         
 
s.bind(('0.0.0.0', 5001 ))
s.listen(0)                 
print('started')
client, addr = s.accept()


while True:   
    content = client.recv(100)
    if len(content) > 0:    
        data = str(content)
        if data == "start":
            print('start')
            break

