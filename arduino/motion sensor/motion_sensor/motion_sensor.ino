// Motion Sensor input
int MOTION_INPUT = 7;
// Speaker Output
int SPEAKER = 8;
// Motion Detected value
int MOTION_DETECTED = 0;
// Pin Value
int PIN_VALUE;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  Serial.print("initializing the motion input pin\n");
  pinMode(MOTION_INPUT, INPUT);
  Serial.print("Motion input pin initialized\n");
  Serial.print("Initializing the speaker pin\n");
  pinMode(SPEAKER, OUTPUT);
  Serial.print("Speaker pin has been initialized\n");

  // Allow 1 minute rest for the sensor to adjust to the room 
  Serial.print("Begining 1 minute wait to allow the sensor to adjust to the room\n");
  delay(60000);
  digitalWrite(SPEAKER, LOW);

}

void loop() {
  // put your main code here, to run repeatedly:

  // Get motion from the sensor
  PIN_VALUE = digitalRead(MOTION_INPUT);
  if (PIN_VALUE == 1){
    // Set the speaker high if motion is detected
    digitalWrite(SPEAKER, HIGH);
    Serial.print("Motion Detected!!! INTRUGER!!\n");
    delay(1000);
    Serial.print(PIN_VALUE);
    MOTION_DETECTED = 1;
  } else {
    Serial.print(PIN_VALUE);
    Serial.print('\n');
  }
  if (MOTION_DETECTED == 1) {
    Serial.print("Switching alarm off\n");
    digitalWrite(SPEAKER, LOW);
    Serial.print("Allowing 1 minute wait to allow the sensor to re ajust to the room\n");
    delay(60000);
    MOTION_DETECTED = 0;
  }

  delay(1000);
  // Check what the value of the motion is
  // Triger the speaker if the motion is what we would expect

}
