#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
int count;
String string_count;

void setup() {
  Serial.begin(115200);//Serial connection
  WiFi.begin("SSID", "PASSWORD");//WiFi connection

  while (WiFi.status() != WL_CONNECTED) {//Wait for the WiFI connection completion
    delay(500);
    Serial.println("Waiting for connection");
  }
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
    HTTPClient http;
    http.begin("http://SEU_IP:8000/new/");//SEU_IP, IP where the server is hosted
    http.addHeader("content-type", "application/x-www-form-urlencoded");

    String body = "device=esp1&password=casa2121&id=1&value=";//String to send for server
    string_count = String("PUT YOUR DATA");//Data to send for server
    body = body + string_count;//Concatenate Strings
    Serial.println(body);//Send the request for Serial
    int httpCode = http.POST(body);//Send the request for Server

    String payload = http.getString();//Get the response payload

    http.end();//Close connection
  } else {
    Serial.println("Error in WiFi connection");
  }
  delay(2000);//Send a request every 2 seconds
}
