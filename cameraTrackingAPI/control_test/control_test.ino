bool waiting = false;
int taskNum = 0;
int ledPin = 13;
int taskAmount = 1;

void setup(){
  // Open serial connection.
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT); 

}
 
void loop(){

  if (!waiting) {
    Serial.println(taskNum, DEC);
    waiting = true;
  }
  
  if (Serial.parseInt() == 1) {
    waiting = false;
    blink();
    taskNum = (taskNum+1)%taskAmount;
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


  

  

  



