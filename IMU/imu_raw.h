#ifndef __IMU_RAW_H__
#define __IMU_RAW_H__

#include <Wire.h>
#include "Arduino.h"


class imu_raw
{

  public: 
    imu_raw();
    void update();

    int gX=0, gY=0, gZ=0;
    int aX=0, aY=0, aZ=0;
    int mX=0, mY=0, mZ=0;
  private:
    void init_LSM303();
    void init_L3G();
    void writeRegister(byte address, byte reg, byte value);
    byte readRegister(byte address, byte reg);
    void readAccelerometer(); 
    void readMagnetometer();
    void readGyro();
  
};

#endif
