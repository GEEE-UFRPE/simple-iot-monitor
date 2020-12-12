import network
import urequests
import ujson

#Wifi configuration
ssid = '' #Your wifi name.
wifi_password = ''

#Server configuration
url = "http:// YOUR IP HERE :8000/new/"   # Example:"http://192.168.0.1:8000/new/

#Admin configuration
admin_name = '' #The name of superuser created in the tutorial.
admin_password = ''

#Sensor Configuration
sensor_id = ''  #We explain how to find the sensor id in the tutorial if you don't know.
value = ''   #This variable will be sent. you can move it if necessary.

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect(ssid, wifi_password)
    while not wlan.isconnected():
        pass
print('network config:', wlan.ifconfig())
    



payload = f"device={admin_name}&password={admin_password}&id={sensor_id}&value={value}"

headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'csrftoken=eTG4ssEqH1itVNKLNCNhnjB4Fxvpo52teSA9QSx6zeag2oQDbXtM9oxjeSDLfT0k'
}

response = urequests.post(url, headers = headers , data = payload)

print(response.text.encode('utf8'))







