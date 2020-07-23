#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>

const char[] SSID = ""; //name of the wifi network to connect
const char[] NETWORK_PASSWORD = ""; //network password
const char[] IP_ADDRESS = ""; //ip address of server. Example: "192.168.1.1"
const char[] DEVICE_NAME = ""; //name that was registered for this device
const char[] DEVICE_PASSWORD = ""; //password that was registered for this device

int count = 0;

void setup() {
    Serial.begin(9600); //Starts serial connection, to use the Serial Monitor
    connectToWiFi(); //Connects to the wi-fi - it keeps trying until it is connected
}

void loop() {
    //sends a value to the monitor system, where SENSOR_ID is the id of the sensor that generated the value
    //if you have multiple sensors on this device, you can use the sendValue function multiple times, with different ids
    sendValue("SENSOR_ID", String(count));

    count += 1;
    delay(2000); //wait 2 seconds before sending a new value, just to make it easier to visualize. This is not mandatory
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
        http.begin("http://" + IP_ADDRESS + ":8000/new/");
        http.addHeader("content-type", "application/x-www-form-urlencoded");

        String body = "device=" + DEVICE_NAME + "&password=" + DEVICE_PASSWORD; //device authentication info
        body += "&id=" + sensorId + "&value="  + value; //sensor information

        Serial.println(body); //prints the http request in the Serial Monitor
        int httpCode = http.POST(body); //actually sends the request to the server

        String payload = http.getString(); //get the response payload

        http.end(); //close connection
    } else {
        Serial.println("WiFi is not connected");
    }
}
