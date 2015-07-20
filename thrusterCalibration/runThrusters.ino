#include <Servo.h>

Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

Servo thrusterGroup1[] = { servo2, servo3 }; // groups of 2 Servos
Servo thrusterGroup2[] = { servo4, servo5 };
Servo allThrusters[] = { servo3, servo5, servo4, servo5 };

int thrusterStop = 1500;

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

int currentGroup = 0; // currently active group
int currentCommand = 0;
int forwardValue = 1575;
int backwardValue = 1425;

char buffer[512];

// we will interactively add or subtract to forward, backward values
int incrementOrDecrementValue = 1;

void setup() {
  setupRelay();
}

void setupServo(Servo servo, int pin) {
  // attach to pin, with small delay and send init status
  servo.attach(pin);
  servo.writeMicroseconds(500);
  delay(4);

  servo.writeMicroseconds(1500); // init for ESC.
  delay(300);
}

void setupRelay() {
  pinMode(52, OUTPUT);
  delay(500);
  digitalWrite(52, LOW);
  delay(500);
  digitalWrite(52, HIGH);
  delay(2000);
}

void loop() {
  
}

void loop2() {
  return;

  setupRelay();

  setupServo(servo2, 2);
  setupServo(servo3, 3);
  setupServo(servo4, 4);
  setupServo(servo5, 5);
  
  
  delay(2000);

  while (1) {
    myLoop();
  }
}

void myLoop() {
  Serial.begin(9600);
  setSerialBuffer(); // set buffer from user input
  // Serial.println(buffer); // print the user input
  currentGroup = buffer[0] - 48;
  currentCommand = buffer[2] - 48;

  // send the current group the current command.
  groupControl(currentGroup, currentCommand);
  delay(500);
  // pauseThrusters();

}

void groupControl(int currentGroup, int currentCommand) {
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

    // change thruster speed
    case FORWARDSPEEDUP:
      Serial.println("Case FORWARDSPEEDUP");
      forwardValue += incrementOrDecrementValue;
      break;
    case FORWARDSPEEDDOWN:
      Serial.println("Case FORWARDSPEEDDOWN");
      forwardValue -= incrementOrDecrementValue;
      break;
    case BACKWARDSPEEDUP:
      Serial.println("Case BACKWARDSPEEDUP");
      backwardValue += incrementOrDecrementValue;
      break;
    case BACKWARDSPEEDDOWN:
      Serial.println("Case BACKWARDSPEEDDOWN");
      backwardValue -= incrementOrDecrementValue;
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
  currentCommand = 0;
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
      return thrusterGroup32;
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
/*

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
*/
