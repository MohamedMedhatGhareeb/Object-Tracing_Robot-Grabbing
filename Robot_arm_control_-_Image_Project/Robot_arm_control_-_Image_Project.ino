#include <VarSpeedServo.h>

char x;

VarSpeedServo BASE ;
VarSpeedServo LINK_1 ;
VarSpeedServo LINK_2 ;
VarSpeedServo GRIBBER ;


void setup() {
  Serial.begin(38400);
  BASE.attach(5);
  LINK_1.attach(6);
  LINK_2.attach(7);
  GRIBBER.attach(8);

  Position_1();

}

void loop() {

  if (Serial.available()>0) {
     
  char x = Serial.read();
   switch (x) {
      case 'S' :  Position_2(); 
                  Position_3(); 
                  Position_4(); 
                  Position_5(); 
                  Position_6(); 
                  Position_7();
      break;

      case 'P' :  Position_1();
      break;

      default : break;
    }
  }
}

void Position_1(){
  BASE.write(105, 35);
  LINK_1.write(105, 35);
  LINK_2.write(170, 35);
  GRIBBER.write(80, 35);

  BASE.wait();
  LINK_1.wait();
  LINK_2.wait();
  GRIBBER.wait();

  
  delay(300);
}

void Position_2(){
  BASE.write(95, 35);
  LINK_1.write(105, 35);
  LINK_2.write(170, 35);
  GRIBBER.write(140, 35);

  BASE.wait();
  LINK_1.wait();
  LINK_2.wait();
  GRIBBER.wait();
  
  delay(300);
  
  
}

void Position_3(){
  BASE.write(95, 35);
  LINK_1.write(45, 35);
  LINK_2.write(165, 35);
  GRIBBER.write(140, 35);

  BASE.wait();
  LINK_1.wait();
  LINK_2.wait();
  GRIBBER.wait();

  
  delay(300);
}


void Position_4(){
  BASE.write(95, 35);
  LINK_1.write(45, 35);
  LINK_2.write(165, 35);
  GRIBBER.write(80, 35);

  BASE.wait();
  LINK_1.wait();
  LINK_2.wait();
  GRIBBER.wait();

  
  delay(300);
}


void Position_5(){
  BASE.write(105, 35);
  LINK_1.write(100, 35);
  LINK_2.write(160, 35);
  GRIBBER.write(80, 35);

  BASE.wait();
  LINK_1.wait();
  LINK_2.wait();
  GRIBBER.wait();

  
  delay(300);
}


void Position_6(){
  BASE.write(20, 35);
  LINK_1.write(10, 35);
  LINK_2.write(80, 35);
  GRIBBER.write(80, 35);

  BASE.wait();
  LINK_1.wait();
  LINK_2.wait();
  GRIBBER.wait();

  
  delay(300);
}


void Position_7(){
  
  BASE.write(20, 35);
  LINK_1.write(10, 35);
  LINK_2.write(80, 35);
  GRIBBER.write(140, 35);

  BASE.wait();
  LINK_1.wait();
  LINK_2.wait();
  GRIBBER.wait();

  
  delay(300);
}
