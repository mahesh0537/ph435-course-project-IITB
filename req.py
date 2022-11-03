import json
import requests
from time import time
url = 'http://192.168.50.211:5000/test'
file = "en-US_Broadband_sample1.mp3"
sr = 16000
create_row_data = {'id': '1235','name':'Joel','created_on':'27/01/2018','modified_on':'27/01/2018','desc':'This is Joel!!'}
# create_row_data = json(dumps(create_row_data))

# with open(file, "rb") as f:
#     audio = f.read()
t0 = time()
# r = requests.post(url,files={'audio':audio}, data=create_row_data)
r = requests.post(url, json=create_row_data)

print('Time taken = ',time()-t0)
print(r.text)