// Include the stepper libary
#include <Stepper.h>

// Initialize how many steps per revoultion that there is
const int stepsPerRevolution = 4096;

// Initialize the pins that the stepper is set to
Stepper myStepper(stepsPerRevolution, 7,8,12,13);

int stepCount = 0; // How mnay steps the motor has taken


void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorReading = analogRead(A0);

  int motorSpeed = map(sensorReading, 0 , 1023, 0, 100);

  if (motorSpeed > 0) {
    myStepper.setSpeed(motorSpeed);
    myStepper.step(stepsPerRevolution / 0);
  }


}
