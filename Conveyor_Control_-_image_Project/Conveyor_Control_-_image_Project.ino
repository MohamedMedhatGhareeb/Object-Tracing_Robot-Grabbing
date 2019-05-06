 char x ;
 int Motor_PIN = 12;
 int Buzzer = 7;

void setup() {
 Serial.begin(38400);
 pinMode( Motor_PIN, OUTPUT);
 pinMode( Buzzer, OUTPUT);
 digitalWrite( Motor_PIN, HIGH); // initialize the motor
 digitalWrite( Buzzer, LOW);
}

void loop() {
  if ( Serial.available ()>0) {
    x = Serial.read();

    switch (x) {
      case 'S' : digitalWrite( Motor_PIN, LOW); // when the centroid of the object with the specified color reaches
      // the specified position on the conveyor, stop the motor
      digitalWrite( Buzzer , HIGH);
      break;

      case 'P' : digitalWrite( Motor_PIN, HIGH); // otherwise motor stays on sweeping objects away!
      digitalWrite( Buzzer , LOW);
      break;

      default : break;
    }
  }
}
