#include <Arduino.h>
#include "WiFi.h"
#include "config.h"
#include "sensor.h"
#include <WiFiClient.h>
#include <WebServer.h>

WiFiServer server(80);
WebServer server1(80);
Sensor *s = NULL;

void connectToWiFi() {

  Serial.print("Connecting to WiFi network: ");
  WiFi.mode(WIFI_STA);      // Connect to WiFi network
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD); // Enter SSID and Password of your WiFi network
  Serial.print("Connecting to WiFi");   // Wait for connection
  unsigned long start = millis();   
  while (WiFi.status() != WL_CONNECTED) {   
    delay(500);
    Serial.print(".");
    if (millis() - start > WIFI_TIMEOUT) {
      Serial.println("Connection timed out");   // If connection fails, restart 
      return;
    }
  }

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("Connected"); 
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());   // Print IP address
  }
  else{
    Serial.println("Connection failed");
  }
}

int last_status=0;

void showstatus(){
  String status_msg = "Current Status: " ;
  status_msg += String(s->status());
  last_status = s->status();
  server1.send(200, "text/plain", status_msg);

}


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  connectToWiFi();    //Connect to WiFi network
  Serial.println("Going into while loop");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    connectToWiFi();
  }
  Serial.println("Wifi Connected Successfully");
  s = new Sensor();
  Serial.println("Led Controller Initialized");

  server1.on("/status", showstatus);
  server1.begin();                      //Start server
}

void loop() {

	delay(1000);
	WiFiClient client = server.available();  // listen for incoming clients
	server1.handleClient();    //Handling of incoming requests
}