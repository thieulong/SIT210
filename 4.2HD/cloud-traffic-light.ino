const int redLed = D2;
const int yellowLed = D3;
const int greenLed = D4;

void setup() {
    pinMode(redLed, OUTPUT);
    pinMode(yellowLed, OUTPUT);
    pinMode(greenLed, OUTPUT);
    Particle.function("light", changeLight);
}

void loop() {

}

int changeLight(String color) {
    // digitalWrite(redLed, LOW);
    // digitalWrite(yellowLed, LOW);
    // digitalWrite(greenLed, LOW);
    
    //Particle.publish("light", color);
    
    if (color == "red") {
        digitalWrite(redLed, HIGH);
        digitalWrite(yellowLed, LOW);
        digitalWrite(greenLed, LOW);
        return 1;
    } else if (color == "yellow") {
        digitalWrite(redLed, LOW);
        digitalWrite(yellowLed, HIGH);
        digitalWrite(greenLed, LOW);
        return 1;
    } else if (color == "green") {
        digitalWrite(redLed, LOW);
        digitalWrite(yellowLed, LOW);
        digitalWrite(greenLed, HIGH);
        return 1;
    }
    return -1;
}