/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/AnalogReadSerial
*/
const int motorPin = 11;
const int potpin = A0;
int pot;
int speed;
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  /*
  int sensorValue = analogRead(A0);
  float voltage = sensorValue*(5.0/1023.0);
  float anlg = sensorValue*(255.0/1023.0);
  // print out the value you read:
  int frequency = map(sensorValue, 0, 1023, 0, 255);
  Serial.println(sensorValue);
  analogWrite(10, anlg);
  delay(1);  // delay in between reads for stability
  */
  pot = analogRead(potpin);
  //Serial.println(pot);
  speed = map(pot, 0, 1023, 0, 255);
  Serial.println(speed);
  analogWrite(motorPin, speed);
}
