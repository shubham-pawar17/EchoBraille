int pins[6] = {8, 9, 10, 11, 12, 13};

void setup() {
  Serial.begin(9600);
  for(int i=0;i<6;i++){
    pinMode(pins[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available()) {
    String pattern = Serial.readStringUntil('\n');

    for(int i=0;i<6;i++){
      digitalWrite(pins[i], pattern[i] == '1');
    }
  }
}