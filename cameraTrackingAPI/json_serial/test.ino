#include <ArduinoJson.h>

String incoming;
char buffer[512];
StaticJsonBuffer<512> jsonBuffer;



 
void setup(){
  // Open serial connection.
  Serial.begin(9600);

}
 
void loop(){
  
  if (Serial.available() > 0) {

    // read the incoming
    incoming = Serial.readString();
 
    incoming.toCharArray(buffer,512);
 
    JsonObject& job = jsonBuffer.parseObject(buffer);
  
    if (!job.success()) {
        Serial.println("parseObject() failed");
        return;
    }else {

      // say what you got:
      int success = job["success"];
      
      if (success == 0) {
         job["success"] = 1;
      }
      job.prettyPrintTo(Serial);
    }
  
  }
}


  

  

  



