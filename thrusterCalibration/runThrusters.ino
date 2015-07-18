#include <Servo.h>
Servo servo9;
Servo servo10;
Servo servo11;
Servo servo12;

int run = 1;

Servo thrusterGroup1[] = { servo9, servo10 }; // groups of 2 pins
Servo thrusterGroup2[] = { servo11, servo12 };
Servo allThrusters[] = { servo9, servo10, servo11, servo12 };

int commands = {
  0, // thruster pause
  1, // thruster forward
  2, // thruster back
  3, // left forward, right backward
  4  // left backward, right forward
}

int currentGroup = 0; // currently active group
int currentCommand = 0;

void setup() {
  setupServo(servo9,   9);
  setupServo(servo10, 10);
  setupServo(servo11, 11);
  setupServo(servo12, 12);
  setupServo(servo10, 10);
}

void setupServo(Servo servo, int pin) {
  // attach to pin, with small delay and send init status
  servo.attach(pin);
  delay(2);
  servo.writeMicroseconds(500); // init servo command (needs to be a value less than 1000);
}

void loop() {
  if(Serial.available()) {
     // send the group to control and then the command.
     currentGroup = currentGroup(Serial.parseInt());
     currentCommand = Serial.parseInt();
  }
  
  // send the current group the current command.
  groupControl(currentGroup, currentCommand);
 
  pauseThrusters();
}

void groupControl(currentGroup, currentCommand) {
    swtich(currentCommand) {
    case 1:
      commandGroup(currentGroup, forwardValue, forwardValue);
      break;
    case 2:
      commandGroup(currentGroup, backwardValue, backwardValue);
      break;
    case 3:
      commandGroup(currentGroup, forwardValue, backwardValue);
      break;
    case 4:
      commandGroup(currentGroup, backwardValue, forwardValue);
      break;
    default:
      pauseThrusters();
  }
}

void commandGroup(int theGroup, int value1, int value2) {
  // Send commands to a Servo group
  Servo group[] = getCurrentGroup(theGroup);
  group[0].writeMicroseconds(value1);
  group[1].writeMicroseconds(value2);
  delay(2);
}

void pauseThrusters() {
  // stop all thrusters!
  for(int i = 0; i < allThrusters.length(); i++) {
    allThrusters[i].writeMicroseconds(1500);
   }
   currentCommand = 0;
}

void runThroughRange() {
  int pos = 0;
  for(pos = 1500; pos < 1900; pos += 1) {
    myservo.writeMicroseconds(pos);
    delay(15);
  }
  for(pos = 1900; pos>=1500; pos-=1) {
    myservo.writeMicroseconds(pos);
    delay(15);
  }
}

int[] getCurrentGroup(int group) {
  return group == 1 ? thrusterGroup1 : thrusterGroup2;
}
