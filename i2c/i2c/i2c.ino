/**
* ReadSHT1xValues
*
* Read temperature and humidity values from an SHT1x-series (SHT10,
* SHT11, SHT15) sensor.
*
* Copyright 2009 Jonathan Oxer <jon@oxer.com.au>
* www.practicalarduino.com
*/

#include <Wire.h>



// Specify data and clock connections and instantiate SHT1x object

void setup()
{
  Serial.begin(115200); // Open serial connection to report values to host
  Serial.println("Starting up");
 
  Wire.begin(0x04); // join i2c bus

    Serial.println("Ready!");
    
}

void loop()
{

  Wire.requestFrom(1, 6);    // request 6 bytes from slave device #2

  while(Wire.available())    // slave may send less than requested
  { 
    char c = Wire.read();    // receive a byte as character
    Serial.print(c);         // print the character
  }

  delay(500);
}
