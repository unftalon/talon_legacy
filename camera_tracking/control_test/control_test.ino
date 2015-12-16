#include <ArduinoJson.h>

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


   
  if (Serial.available()) {

    int x = Serial.parseInt();
    int y = Serial.parseInt();

    if(x==0 && y==0) {
        waiting = false;
        blink(3);
        taskNum = (taskNum+1)%taskAmount;
        
    } else {
        Serial.println(x, DEC);
        Serial.println(y, DEC);
    }
    
  }
}

void blink(int amount){
  
  for(int i=0; i<amount; i++) {
    digitalWrite(ledPin, HIGH);   
    delay(1000);                  
    digitalWrite(ledPin, LOW);    
    delay(1000);   
  }              
}



  

  

  



