#include "imu_raw.h"

/*=========================================================================
    REGISTERS
    -----------------------------------------------------------------------*/


// High and Low bytes of temperature sensors 
const byte TEMP_OUT_L         = 0B00000101;
const byte TEMP_OUT_H         = 0B00000110;


// High and Low bytes of mag X Value 
const byte OUT_X_L_M          = 0B00001000;
byte OUT_X_H_M          = 0B00001001;


// High and Low bytes of mag Y Value 
const byte OUT_Y_L_M          = 0B00001010;
const byte OUT_Y_H_M          = 0B00001011;

// High and Low bytes of mag Z Value 
const byte OUT_Z_L_M          = 0B00001100;
const byte OUT_Z_H_M          = 0B00001101;

// Accelerometer and Magnetometer's identification register
const byte ACC_MAG_ID         = 0B00001111; 


const byte ACC_MAG_CTRL[] = {0B00011111, 0B00100000, 
                      0B00100001, 0B00100010, 
                      0B00100011, 0B00100100,
                      0B00100101, 0B00100110};

const byte GYRO_CTRL[] =  {0B100000, 0B100001, 
                      0B100010, 0B100011, 
                      0B100100};

// Accelerometer axes's registers
const byte OUT_X_L_A          = 0B00101000;
const byte OUT_X_H_A          = 0B00101001;
const byte OUT_Y_L_A          = 0B00101010;
const byte OUT_Y_H_A          = 0B00101011;
const byte OUT_Z_L_A          = 0B00101100;
const byte OUT_Z_H_A          = 0B00101101;



// GYRO axes's registers
const byte OUT_X_L_G          = 0B101000;
const byte OUT_X_H_G          = 0B101001;
const byte OUT_Y_L_G          = 0B101010;
const byte OUT_Y_H_G          = 0B101011;
const byte OUT_Z_L_G          = 0B101100;
const byte OUT_Z_H_G          = 0B101101;


const byte READ    = 0B00000001;
const byte WRITE   = 0B00000000;


const byte ACC_MAG_ADDRESS  = 0B01101011;


const byte GYRO_ADDRESS     = 107;

imu_raw::imu_raw()
{

  Wire.begin(); //start the Wire library;
  
  init_LSM303();
  init_L3G();

}

void imu_raw::init_LSM303() 
{
  //activate accelerometer/magnetometer  
  writeRegister(ACC_MAG_ADDRESS, ACC_MAG_CTRL[1],0B00001111);



}

void imu_raw::init_L3G()
{
  
  //activate gyroscope
  writeRegister(GYRO_ADDRESS, GYRO_CTRL[0], 0B1101111);
  writeRegister(GYRO_ADDRESS, GYRO_CTRL[4], 0B0000000);
}


void imu_raw::writeRegister(byte address, byte reg, byte value) 
{
  
  Wire.beginTransmission((address | WRITE) );


  Wire.write(reg);
  Wire.write(value);
  Wire.endTransmission();
  
}

byte imu_raw::readRegister(byte address, byte reg) 
{
  
  byte result = 0;
  Wire.beginTransmission((address | WRITE) ); 

  Wire.write(reg);
  
  Wire.endTransmission(0); //complete the send
  

  Wire.requestFrom((address | READ) , 1); // Request 1 byte
  
 
  while( Wire.available() == 0);  //wait for info
  
  result = Wire.read();  
 
  Wire.endTransmission();  
  
  return result ;  
}



void imu_raw::readAccelerometer() 
{
  
  byte X_L_A = readRegister(ACC_MAG_ADDRESS, OUT_X_L_A);
  byte X_H_A = readRegister(ACC_MAG_ADDRESS, OUT_X_H_A);
  byte Y_L_A = readRegister(ACC_MAG_ADDRESS, OUT_Y_L_A);
  byte Y_H_A = readRegister(ACC_MAG_ADDRESS, OUT_Y_H_A);
  byte Z_L_A = readRegister(ACC_MAG_ADDRESS, OUT_Z_L_A);
  byte Z_H_A = readRegister(ACC_MAG_ADDRESS, OUT_Z_H_A);

  aX = X_H_A <<8 | X_L_A;
  aY = Y_H_A <<8 | Y_L_A;
  aZ = Z_H_A <<8 | Z_L_A;

}

void imu_raw::readMagnetometer() 
{
  
  byte X_L_M = readRegister(ACC_MAG_ADDRESS, OUT_X_L_M);
  byte X_H_M = readRegister(ACC_MAG_ADDRESS, OUT_X_H_M);
  byte Y_L_M = readRegister(ACC_MAG_ADDRESS, OUT_Y_L_M);
  byte Y_H_M = readRegister(ACC_MAG_ADDRESS, OUT_Y_H_M);
  byte Z_L_M = readRegister(ACC_MAG_ADDRESS, OUT_Z_L_M);
  byte Z_H_M = readRegister(ACC_MAG_ADDRESS, OUT_Z_H_M);

  mX = X_H_M <<8 | X_L_M;
  mY = Y_H_M <<8 | Y_L_M;
  mZ = Z_H_M <<8 | Z_L_M;

  
}

void imu_raw::readGyro() 
{
  
  byte X_L_G = readRegister(GYRO_ADDRESS, OUT_X_L_G);
  byte X_H_G = readRegister(GYRO_ADDRESS, OUT_X_H_G);
  byte Y_L_G = readRegister(GYRO_ADDRESS, OUT_Y_L_G);
  byte Y_H_G = readRegister(GYRO_ADDRESS, OUT_Y_H_G);
  byte Z_L_G = readRegister(GYRO_ADDRESS, OUT_Z_L_G);
  byte Z_H_G = readRegister(GYRO_ADDRESS, OUT_Z_H_G);

  gX = X_H_G <<8 | X_L_G;
  gY = Y_H_G <<8 | Y_L_G;
  gZ = Z_H_G <<8 | Z_L_G;

}

void imu_raw::update() 
{
  readAccelerometer();
  readMagnetometer();
  readGyro();
}


