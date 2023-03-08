#include "Adafruit_DHT.h"

#define DHTPIN 2    

#define DHTTYPE DHT11		

DHT dht(DHTPIN, DHTTYPE);

void setup() {
	dht.begin();
}

void loop() {
	delay(2000);
	float t = dht.getTempCelcius();
    Particle.publish("temp", String(t), PRIVATE);
    delay(30000);
}

