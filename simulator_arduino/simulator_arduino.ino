
#include <Stepper.h>



#define m1_IN1 8
#define m1_IN2 9
#define m1_IN3 10
#define m1_IN4 11
#define m2_IN1 4
#define m2_IN2 5
#define m2_IN3 6
#define m2_IN4 7


int steps_per_rev=32;
int state;

Stepper mystepper(steps_per_rev, m1_IN1,m1_IN3,m1_IN2,m1_IN4);

Stepper mystepper2(steps_per_rev, m2_IN1,m2_IN3,m2_IN2,m2_IN4);

int step_count=0;
int val;


void setup() {
	Serial.begin(9600); //baud rate
  mystepper.setSpeed(512);
  mystepper2.setSpeed(512);
  while(true) {
    if(Serial.available()>0) {
      state=Serial.read();
      Serial.write(state);
      if(state==65) {
        mystepper.step(-2048);
      }
      if(state==66) {
        mystepper2.step(-2048);
      }
    }
  }
}


void loop() {
  
	if(Serial.available()>0) {
		state=Serial.read();
    Serial.write(state);
		if(state==65) {
			mystepper.step(2048);
		}
		if(state==66) {
			mystepper2.step(2048);
		}
	}
}
