#include <Servo.h>
//Intialize Servos
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
Servo servo7;
//Group Servos int pairs
Servo thrusterGroup1[] = { servo2, servo3 };
Servo thrusterGroup2[] = { servo4, servo5 };
Servo thrusterGroup3[] = { servo6, servo7 };
//array of trusters for all the ones on the robot
Servo allThrusters[] = { servo2, servo3, servo4, servo5, servo6, servo7 };
//stop value for thrushtes
int thrusterStop = 1500;
//commands
/*
Enums are just constants with predefined values if not defined it gose from 0 to n-1. n being the # of values
*/
enum Commands {
  PAUSE             , // 0
  FORWARD           , // 1
  BACKWARD          , // 2
  LEFT              , // 3
  RIGHT             , // 4
  FORWARDSPEEDUP    , // 5
  FORWARDSPEEDDOWN  , // 6
  BACKWARDSPEEDUP   , // 7
  BACKWARDSPEEDDOWN   // 8
};
//intialize ??
int currentGroup1   = 0;
int currentCommand1 = PAUSE;
int currentGroup2   = 0;
int currentCommand2 = PAUSE;
int currentGroup3   = 0;
int currentCommand3 = PAUSE;

/*
Thurster Value Range
1500 +/- 30 is stop
1900 - 1500 +/- 30 is forward
1500 - 1100 +/- is backward
*/
//Is this values there because the singal was noisy
int forwardValue1 = 1650;
int backwardValue1 = 1425;

int forwardValue2 = 1600;
int backwardValue2 = 1500;

int forwardValue3 = 1550;
int backwardValue3 = 1400;

char buffer[512];

int killSwitch = 0;
//this pin is for toggling on/off the robot
int starterPin = 28;

void setup() {
  //Sets USB Baud Rate - Serial Monitor must match
  /*
  Baud rate = rate in bits per second for communications
  */
  Serial.begin(9600);
  //Set up the starter pin to read input from a signal
  pinMode(starterPin, INPUT);
  //while robot not enaged wait for commad after staterpin is turned on
  while( digitalRead(starterPin) != HIGH ) {
    Serial.println("waiting");
  }
  //after enaged tell computer over serial it is ready and set kill switch to waiting mode
  Serial.println("starting..");
  killSwitch = 1;
  //wait 5 seconds
  delay(5000);
  //prepare the servos
  setupServo(servo2, 2);
  setupServo(servo3, 3);
  setupServo(servo4, 4);
  setupServo(servo5, 5);
//  setupServo(servo6, 6);
//  setupServo(servo7, 7);
  Serial3.begin(9600);
  Serial.begin(9600);
  delay(2000);
  
}
  
void loop() {
  //check that starter is not off
  if(digitalRead(starterPin) == LOW) {
    killSwitch = 0;
    Serial.println("detected starterPin off");
  }
  //if mismatch between killswitch starter reset robot
  if(digitalRead(starterPin) == HIGH && killSwitch == 0) {
    Serial.println("setting up again");
    setup();
  }
  //straight bot in water for the gate
  straight();
}

void straight() {
  //issues commands to a set robot
  commandGroup(1, 1750, 1750);
  commandGroup(2, 1650,1650);
  delay(700);
  commandGroup(2, 1500,1500);
  delay(500);
}

// we will interactively add or subtract to forward, backward values
int incrementOrDecrementValue = 1;

void setupServo(Servo servo, int pin) {
  // attach to pin, with small delay and send init status
  servo.attach(pin);
  servo.writeMicroseconds(500);
  delay(500);

  servo.writeMicroseconds(1500); // init for ESC.
  delay(500);
}

void setupRelay() {
  pinMode(52, OUTPUT);
  delay(500);
  digitalWrite(52, LOW);
  delay(500);
  digitalWrite(52, HIGH);
  delay(2000);
}

void myLoop() {

  setSerial3Buffer(); // set buffer from user input
  //What does 48 represent?
  Serial.println(buffer);
  currentGroup1 = buffer[0] - 48;
  currentCommand1 = buffer[2] - 48;
  currentGroup2 = buffer[4] - 48;
  currentCommand2 = buffer[6] - 48;
  currentGroup3 = buffer[8] - 48;
  currentCommand3 = buffer[10] - 48;
  
  // send the current group the current command.
  groupControl(1, 1);
  groupControl(currentGroup2, currentCommand2);
  groupControl(currentGroup3, currentCommand3);
  
  delay(50);
  // pauseThrusters();
}

void groupControl(int currentGroup, int currentCommand) {

  int forwardValue = getForwardValueForGroup(currentGroup);
  int backwardValue = getBackwardValueForGroup(currentGroup);

  switch (currentCommand) {
    // thruster directions
    case PAUSE:
      Serial.println("Case PAUSE");
      pauseThrusters();
      break;
    case FORWARD:
      Serial.println("Case FORWARD");
      commandGroup(currentGroup, forwardValue, forwardValue);
      break;
    case BACKWARD:
      Serial.println("Case BACKWARD");
      commandGroup(currentGroup, backwardValue, backwardValue);
      break;
    case LEFT:
      Serial.println("Case LEFT");
      commandGroup(currentGroup, forwardValue, backwardValue);
      break;
    case RIGHT:
      Serial.println("Case RIGHT");
      commandGroup(currentGroup, backwardValue, forwardValue);
      break;
    default:
      pauseThrusters();
  }
}

void commandGroup(int theGroup, int value1, int value2) {
  // Send commands to a Servo group
  Servo* group = getCurrentGroup(theGroup);

  Serial.print(value1);
  Serial.print( ":");
  Serial.println(value2);


  group[0].writeMicroseconds(value1);
  group[1].writeMicroseconds(value2);
  delay(2);
}

void pauseThrusters() {
  Serial.println("Pause thrusters!");
  // stop all thrusters!
  for (int i = 0; i < (sizeof(allThrusters) / sizeof(Servo)); i++) {
    allThrusters[i].writeMicroseconds(thrusterStop);
  }
  currentCommand1 = 0;
  currentCommand2 = 0;
}

void runThroughRange(Servo myservo) {
  int pos = 0;
  for (pos = 1500; pos < 1900; pos += 1) {
    myservo.writeMicroseconds(pos);
    delay(15);
  }
  for (pos = 1900; pos >= 1500; pos -= 1) {
    myservo.writeMicroseconds(pos);
    delay(15);
  }
}

Servo* getCurrentGroup(int group) {
  switch(group) {
    case 1:
      return thrusterGroup1;
    case 2:
      return thrusterGroup2;
    case 3:
      return thrusterGroup3;
  }
}

int setSerialBuffer() {
  // FYI:
  // We can't replace this with serialPort.readString();
  // As much as I would like to...
  if (Serial.available()) {
    int c; // a single character
    int i = 0;
    for (i = 0; i < 100; i++) {
      c = Serial.read();
      if (c != '\n' && c != -1) {
        // This delay needs to be here or else garbage enters the buffer
        delay(2);
        buffer[i] = c;
      } else {
        buffer[i] = '\0';
      }
    }
  }
}

void relayDisconnect() {
  // emergency stop
  digitalWrite(52, LOW);
}

void commandServo(Servo theServo, int value) {
  theServo.writeMicroseconds(value);
  delay(2);
}

int getForwardValueForGroup(int theGroup) {
  switch(theGroup) {
    case 1:
      return forwardValue1;
    case 2:
      return forwardValue2;
    case 3:
      return forwardValue3;
    default: 
      return 1500;
  }
}

int getBackwardValueForGroup(int theGroup) {
    switch(theGroup) {
    case 1:
      return backwardValue1;
    case 2:
      return backwardValue2;
    case 3:
      return backwardValue3; 
    default: 
      return 1500;
  }
}

int setSerial3Buffer() {
  // FYI:
  // We can't replace this with serialPort.readString();
  // As much as I would like to...
  if(Serial3.available()) {
    int c; // a single character
    int i = 0;
    for(i = 0; i < 100; i++) {
      c = Serial3.read();
      if (c != '\n' && c != -1) {
        // This delay needs to be here or else garbage enters the buffer
        delay(2);
        buffer[i] = c;
      } else {
        buffer[i] = '\0';
      }
    }
  }
}
