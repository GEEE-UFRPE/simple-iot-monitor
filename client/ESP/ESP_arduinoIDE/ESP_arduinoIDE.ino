#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>

//Wifi configuration
String SSID = "WIFI_NAME"; //name of the wifi network to connect
String NETWORK_PASSWORD = "WIFI_PASSWORD"; //password of the wifi network
String IP_ADDRESS = "SERVER_IP_ADRESS"; //ip address of the server. Example: "192.168.1.1"

//sensor authentication
String SENSOR_NAME = "sensor1"; //sensor username
String SENSOR_PASSWORD = "badpass1"; //sensor password


void setup() {
    Serial.begin(115200); //Starts serial connection, to use the Serial Monitor
    connectToWiFi(); //Connects to the wifi - it keeps trying until it is connected
}

void loop() {
    //sends a value to the server. This example sends the value 5.2.
    //if you have multiple sensors on this device, you can use the sendValue function multiple times, with different sensor names and passwords
    sendValue(SENSOR_NAME, SENSOR_PASSWORD, String(5.2));



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

void sendValue(String sensorName, String sensorPassword, String value) {
    //Check WiFi connection status
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
        http.begin("http://"+IP_ADDRESS+":8000/iotmonitor/readings");
        http.addHeader("content-type", "application/x-www-form-urlencoded");

        String body = "sensor=" + sensorName + "&password=" + sensorPassword; //device authentication info
        body += "&value="  + value; //sensor information

        Serial.println(body); //prints the http request in the Serial Monitor

        int httpCode = http.POST(body); //actually sends the request to the server

        String response = http.getString(); //get the response from the server

        http.end(); //close connection
        Serial.println("##[RESPONSE]## ==> " + response);
        
    } else {
        Serial.println("WiFi is not connected");
    }
}
