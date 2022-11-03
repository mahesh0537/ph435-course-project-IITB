#include <Arduino.h>
#include "sensor.h"
#include "sensor_config.h"
#include "config.h"
#include "WiFi.h"
#include <WiFiClient.h>


Sensor::Sensor() {
    pinMode(PIN0, INPUT);
    _status = 0;
    WiFiClient m_client;
    m_client.connect(IP, PORT);
    String msg = "GET /add_plot?ID="  + String(device_type)+ "&IP=" + (WiFi.localIP().toString()); 
    m_client.println(msg);
    m_client.stop();
    Serial.println(msg);
}


int Sensor::status() {
    read();
    Serial.print("Status: ");
    Serial.println(_status);
    return _status;
}

void Sensor::read() {
    _status = analogRead(PIN0);
}