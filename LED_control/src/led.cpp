#include <Arduino.h>
#include "led.h"
#include "led_config.h"
#include "config.h"
#include "WiFi.h"
#include <WiFiClient.h>


Led::Led() {
    pinMode(PIN0, OUTPUT);
    pinMode(PIN1, OUTPUT);
    pinMode(PIN2, OUTPUT);
    pinMode(PIN3, OUTPUT);
    _brightness = 0;
    set_pins();
    WiFiClient m_client;
    m_client.connect(IP, PORT);
    String msg = "GET /setup_led?ID="  + String(device_type)+ "&IP=" + (WiFi.localIP().toString()); 
    m_client.println(msg);
    m_client.stop();
    Serial.println(msg);
}

void Led::on(int brightness) {
    _brightness = brightness;
    Serial.println("Brightness is " + String(_brightness));
    set_pins();
    
}

void Led::off() {
    _brightness = 0;
    set_pins();
}

void Led::blink(int delay_) {
    for (int i = 0; i < 10; i++) {
        _brightness = 15;
        set_pins();
        delay(delay_);
        _brightness = 0;
        set_pins();
        delay(delay_);
    }
}

void Led::status() {
    Serial.print("Brightness: ");
    Serial.println(_brightness);
}

void Led::set_pins() {      
    if (_brightness & 0b0001) {    
        digitalWrite(PIN0, HIGH);  //LSB for DAC 
        Serial.print(PIN0);
        Serial.println(" is HIGH");
    } else {
        digitalWrite(PIN0, LOW);
    }
    if (_brightness & 0b0010) {     
        digitalWrite(PIN1, HIGH);
        Serial.print(PIN1);
        Serial.println(" is HIGH");
    } else {
        digitalWrite(PIN1, LOW);
    }
    if (_brightness & 0b0100) {
        digitalWrite(PIN2, HIGH);
        Serial.print(PIN2);
        Serial.println(" is HIGH");
    } else {
        digitalWrite(PIN2, LOW);
    }
    if (_brightness & 0b1000) {
        digitalWrite(PIN3, HIGH);      //MSB for DAC
        Serial.print(PIN3);
        Serial.println(" is HIGH");
    } else {
        digitalWrite(PIN3, LOW);
    }
}