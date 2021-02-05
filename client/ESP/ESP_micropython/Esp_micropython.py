import network
import urequests
import ujson

#Wifi configuration
ssid = '' #Your wifi name.
wifi_password = ''
your_ip = '' # Example: '192.168.0.1'

#Server configuration
url ="http://"+your_ip+":8000/iotmonitor/reading"

#Admin configuration
sensor_name = 'sensor1' #The name of superuser created in the tutorial.
sensor_password = 'senharuim'

#Sensor Configuration
value = ''   #This variable will be sent. you can move it if necessary.

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect(ssid, wifi_password)
    while not wlan.isconnected():
        pass
print('network config:', wlan.ifconfig())

payload = "sensor="+sensor_name+"&password="+sensor_password+"&value="+value

headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'csrftoken=eTG4ssEqH1itVNKLNCNhnjB4Fxvpo52teSA9QSx6zeag2oQDbXtM9oxjeSDLfT0k'
}

response = urequests.post(url, headers = headers , data = payload)

print(response.text.encode('utf8'))







