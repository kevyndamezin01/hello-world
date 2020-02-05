#define STEPPER_PIN_1 7   // Red Wire     Pin 1 
#define STEPPER_PIN_2 8   // Purlple Wire Pin 2
#define STEPPER_PIN_3 12  // Grey Wire    Pin 3
#define STEPPER_PIN_4 13  // Orange Wrire Pin 4

int step_number = 0;

void setup() {
  // put your setup code here, to run once:

  pinMode(STEPPER_PIN_1, OUTPUT);
  pinMode(STEPPER_PIN_2, OUTPUT);
  pinMode(STEPPER_PIN_3, OUTPUT);
  pinMode(STEPPER_PIN_4, OUTPUT);


}

void loop() {
  // put your main code here, to run repeatedly:

    OneStep(false);
  delay(2);
  

}


void OneStep(bool dir){
    if(dir){
switch(step_number){
  case 0:
  digitalWrite(STEPPER_PIN_1, HIGH);
  delay(2);
  digitalWrite(STEPPER_PIN_2, LOW);
  delay(2);
  digitalWrite(STEPPER_PIN_3, LOW);
  delay(2);
  digitalWrite(STEPPER_PIN_4, LOW);
  delay(2);
  break;
  case 1:
  digitalWrite(STEPPER_PIN_1, LOW);
  delay(2);
  digitalWrite(STEPPER_PIN_2, HIGH);
  delay(2);
  digitalWrite(STEPPER_PIN_3, LOW);
  delay(2);
  digitalWrite(STEPPER_PIN_4, LOW);
  delay(2);
  break;
  case 2:
  digitalWrite(STEPPER_PIN_1, LOW);
  delay(2);
  digitalWrite(STEPPER_PIN_2, LOW);
  delay(2);
  digitalWrite(STEPPER_PIN_3, HIGH);
  delay(2);
  digitalWrite(STEPPER_PIN_4, LOW);
  delay(2);
  break;
  case 3:
  digitalWrite(STEPPER_PIN_1, LOW);
  digitalWrite(STEPPER_PIN_2, LOW);
  digitalWrite(STEPPER_PIN_3, LOW);
  digitalWrite(STEPPER_PIN_4, HIGH);
  break;
} 
  }else{
    switch(step_number){
  case 0:
  digitalWrite(STEPPER_PIN_1, LOW);
  digitalWrite(STEPPER_PIN_2, LOW);
  digitalWrite(STEPPER_PIN_3, LOW);
  digitalWrite(STEPPER_PIN_4, HIGH);
  break;
  case 1:
  digitalWrite(STEPPER_PIN_1, LOW);
  digitalWrite(STEPPER_PIN_2, LOW);
  digitalWrite(STEPPER_PIN_3, HIGH);
  digitalWrite(STEPPER_PIN_4, LOW);
  break;
  case 2:
  digitalWrite(STEPPER_PIN_1, LOW);
  digitalWrite(STEPPER_PIN_2, HIGH);
  digitalWrite(STEPPER_PIN_3, LOW);
  digitalWrite(STEPPER_PIN_4, LOW);
  break;
  case 3:
  digitalWrite(STEPPER_PIN_1, HIGH);
  digitalWrite(STEPPER_PIN_2, LOW);
  digitalWrite(STEPPER_PIN_3, LOW);
  digitalWrite(STEPPER_PIN_4, LOW);
 
  
} 
  }
step_number++;
  if(step_number > 3){
    step_number = 0;
  }
}
