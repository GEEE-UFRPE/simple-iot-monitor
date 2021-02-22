import requests

# Before running this code, make sure that:
# 1) the server is already running
# 2) your Raspberry PI is connected to the same network of the server

# Configuration
IP_ADDRESS = '192.168.1.7' # IP address of the server. Example: '192.168.1.1'
SENSOR_NAME = 'sensor1' # Sensor username
SENSOR_PASSWORD = 'badpass1' # Sensor password

# This code will make 10 requests to the server, sending the values from 1 to 10
for x in range(1, 11):
    r = requests.post('http://' + IP_ADDRESS + ':8000/iotmonitor/readings',
                      data={'sensor': SENSOR_NAME, 'password': SENSOR_PASSWORD, 'value': str(x)})
    print(r.text)