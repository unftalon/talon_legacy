int pinRelay = 13;
int pinMagnet = 12;
int pinMega = 11;
int val=0;
void setup(){
  setupRelay();
  pinMode(pinMagnet,INPUT);
  pinMode(pinMega,OUTPUT);
  Serial.begin(9600);
}

void loop(){
  val = digitalRead(pinMagnet);
  Serial.println(val);
  
  if(val == HIGH){
    digitalWrite(pinMega,HIGH);
    digitalWrite(pinRelay,HIGH);

  }else{
    digitalWrite(pinMega,LOW);    
    digitalWrite(pinRelay,HIGH);

  }
  
}

void setupRelay() {
  pinMode(13, OUTPUT);
  delay(500);
  digitalWrite(13, LOW);
  delay(500);
  digitalWrite(13, HIGH);
  delay(2000);
}
