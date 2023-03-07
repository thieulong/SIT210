const int led = D7;

const long dit_duration = 100;
const long da_duration = 300;
const long intra_character_duration = 100;
const long inter_character_duration = 300;
const long space_duration = 700;

String name = "Paul"; 

const char* morse_codes[] = {
  ".-",   // A
  "-...", // B
  "-.-.", // C
  "-..",  // D
  ".",    // E
  "..-.", // F
  "--.",  // G
  "....", // H
  "..",   // I
  ".---", // J
  "-.-",  // K
  ".-..", // L
  "--",   // M
  "-.",   // N
  "---",  // O
  ".--.", // P
  "--.-", // Q
  ".-.",  // R
  "...",  // S
  "-",    // T
  "..-",  // U
  "...-", // V
  ".--",  // W
  "-..-", // X
  "-.--", // Y
  "--.."  // Z
};

void setup() {
  pinMode(led, OUTPUT);
}

void loop() {
  name = name.toLowerCase();
  for (int i = 0; i < name.length(); i++) {
    char c = name.charAt(i);
    if (c == ' ') { 
      delay(space_duration);
    } else {
      const char* morse = morse_codes[c - 'a'];
      for (int j = 0; morse[j] != '\0'; j++) {
        if (morse[j] == '.') {
          digitalWrite(led, HIGH);
          delay(dit_duration);
          digitalWrite(led, LOW);
          delay(intra_character_duration);
        } else if (morse[j] == '-') {
          digitalWrite(led, HIGH);
          delay(da_duration);
          digitalWrite(led, LOW);
          delay(intra_character_duration);
        }
      }
      delay(inter_character_duration); 
    }
  }
}