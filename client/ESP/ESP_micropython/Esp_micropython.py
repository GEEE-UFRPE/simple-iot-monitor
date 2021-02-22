import network
import urequests

# Wifi configuration
SSID = 'WIFI_NAME'  # Name of the wifi network to connect
NETWORK_PASSWORD = 'WIFI_PASSWORD'  # Password of the wifi network
IP_ADDRESS = 'SERVER_IP_ADRESS'  # IP address of the server. Example: '192.168.1.1'

# Sensor authentication
SENSOR_NAME = 'sensor1'  # Sensor username
SENSOR_PASSWORD = 'badpass1'  # Sensor password

# Connecting to wifi
url = "http://" + IP_ADDRESS + ":8000/iotmonitor/readings"
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
while not wlan.isconnected():
    print('connecting to network...')
    wlan.connect(SSID, NETWORK_PASSWORD)
print('network config:', wlan.ifconfig())


def send_value(sensor_username, sensor_pass, value):
    # Send data to the server
    parameters = "sensor=" + sensor_username + "&password=" + sensor_pass + "&value=" + value
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = urequests.post(url, headers=headers, data=parameters)
    print(response.text.encode('utf8'))


# Actually send the data to the server. This example sends the value 5.2.
# If you have multiple sensors on this device, you can use the sendValue function multiple times,
# with different sensor names and passwords.
send_value(SENSOR_NAME, SENSOR_PASSWORD, str(5.2))
