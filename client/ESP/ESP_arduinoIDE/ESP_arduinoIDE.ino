#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>

String SSID = "WIFI_NAME"; //name of the wifi network to connect
String NETWORK_PASSWORD = "WIFI_PASSWORD"; //network password
String IP_ADDRESS = "IP_ADRESS"; //ip address of server. Example: "192.168.1.1"

//login and password (modification optional)
String SENSOR_NAME = "sensor1"; //name that was registered for this device
String SENSOR_PASSWORD = "senharuim"; //password that was registered for this device


void setup() {
    Serial.begin(115200); //Starts serial connection, to use the Serial Monitor
    connectToWiFi(); //Connects to the wi-fi - it keeps trying until it is connected
}

void loop() {
    //sends a value to the monitor system, where SENSOR_ID is the id of the sensor that generated the value
    //if you have multiple sensors on this device, you can use the sendValue function multiple times, with different ids
    sendValue("","VALUE");


  
    delay(4000); //wait 4 seconds before sending a new value, just to make it easier to visualize. This is not mandatory
}

void connectToWiFi() {
    WiFi.begin(SSID, NETWORK_PASSWORD); //request a WiFi connection

    //Wait for the WiFI connection to be completed
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.println("Waiting for connection");
    }
}

void sendValue(String sensorId, String value) {
    //Check WiFi connection status
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
        http.begin("http://"+IP_ADDRESS+":8000/iotmonitor/reading");
        http.addHeader("content-type", "application/x-www-form-urlencoded");

        String body = "sensor=" + SENSOR_NAME + "&password=" + SENSOR_PASSWORD; //device authentication info
        body += "&value="  + value; //sensor information

        Serial.println(body); //prints the http request in the Serial Monitor
        
        int httpCode = http.POST(body); //actually sends the request to the server

        String payload = http.getString(); //get the response payload
  
        http.end(); //close connection
        Serial.println("##[RESPONSE]## ==> " + payload);
        
    } else {
        Serial.println("WiFi is not connected");
    }
}
