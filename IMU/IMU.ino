#include <Wire.h>
#include "imu_raw.h"

imu_raw *imu;

const float ACC_BIAS = 3;
const float GYRO_BIAS = 32;
const float MAG_BIAS = 4;

// Assumming default settings
const double GYRO_GAIN = 0.008;



// loop period measured to be about 20ms
const double DT = 0.02;


float gyroRoll = 0;
float gyroPitch = 0;
float gyroYaw = 0;

void setup()
{
  Serial.begin(9600);
  imu = new imu_raw();

  delay(500);

}

void loop() 
{
  
  imu->update();
  

  float rateGyroX = imu->gX * GYRO_GAIN;
  float rateGyroY = imu->gY * GYRO_GAIN;
  double rateGyroZ = imu->gZ * GYRO_GAIN;

  gyroRoll  +=rateGyroX*DT;
  gyroPitch +=rateGyroY*DT;
  gyroYaw   +=rateGyroZ*DT;

  float accRoll =  (atan2(imu->aX,imu->aZ) +PI)*RAD_TO_DEG;
  float accPitch =  (atan2(imu->aY,imu->aZ) +PI)*RAD_TO_DEG;

  Serial.println(gyroRoll*0.5+accRoll*0.5);

}


