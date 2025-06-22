const uint8_t signal[] = {
  127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 
  127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 126, 124, 132, 131, 131, 
  126, 128, 127, 126, 129, 128, 126, 129, 128, 127, 127, 127, 128, 127, 128, 128, 
  126, 129, 127, 127, 127, 128, 126, 126, 128, 127, 127, 127, 127, 127, 127, 127
};
//examples of frequencies above
int signalLength = sizeof(signal) / sizeof(signal[0]);

void setup() {
  pinMode(9, OUTPUT);

}

void loop() {
  for (int i = 0; i < signalLength; i++) {
    analogWrite(9, signal[i]);
    delay(10);
  }

}
