bool waiting = false; // waiting for pi to return a success a '1'
int taskNum = 0;      // current task number
int ledPin = 13;      // internal orange LED located on the arduino
int taskAmount = 2;   // There are two task. Gate Detection and then buoy detection

void setup(){
  
  // Open serial connection.
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);  

}
 
void loop(){

  if (!waiting) {
    Serial.println(taskNum, DEC);     // send task number to pi
    waiting = true;                   // now wait for success from pi
  }
  
  if (Serial.parseInt() == 1) {       // 1 represents success
    waiting = false;                
    blink();                          // represent success by blinking 3 times
    performAction();                  // have arduino peform certain action. Just a delay for now
    taskNum = (taskNum+1)%taskAmount; // go to next task. If you taskNum goes beyond taskAmount reset to 0
  }
}

void blink(){
  
  for(int i=0; i<3; i++) {
    digitalWrite(ledPin, HIGH);   
    delay(1000);                  
    digitalWrite(ledPin, LOW);    
    delay(1000);   
  }              
}

void performAction() {

    // do something useful
    delay(5000);
}


  

  

  



