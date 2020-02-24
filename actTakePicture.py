import requests
import wget
import os

url = 'http://192.168.122.1:10000/sony/camera'

json_data = {"method": "actTakePicture", "params": [], "id": 1, "version": "1.0"}

r = requests.post(url, json = json_data)

data = r.json()
image_url = data["result"][0][0]
print (image_url)

local_file = wget.download(image_url)

print()
print (local_file)

os.system("blueman-sendto " + local_file + " -d 2C:FD:AB:D0:C5:A9")
