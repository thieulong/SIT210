const int light_sensor = A0;
const int led = D7;
const int light_threshold = 50;

int analogValue;

boolean sunlight_detected_flag = false;
boolean sunlight_not_detected_flag = false;

void setup() {
    pinMode(led, OUTPUT);
}

void loop() {
    analogValue = analogRead(light_sensor);
    if(analogValue > light_threshold){
        digitalWrite(led, HIGH);
        if (sunlight_detected_flag == false){
            sunlight_detected_flag = true;
            sunlight_not_detected_flag = false;
            String data = String(10);
            Particle.publish("sunlight_detected", data, PRIVATE);
            }
    } else if (analogValue < light_threshold){
        digitalWrite(led, LOW);  
        if (sunlight_not_detected_flag == false){
            sunlight_not_detected_flag = true;
            sunlight_detected_flag = false;
            String data = String(10);
            Particle.publish("sunlight_not_detected", data, PRIVATE);
            }
    }
    delay(1000);
}