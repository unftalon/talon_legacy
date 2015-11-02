# RoboSub

Welcome to the fun times at RoboSub! Visit us at [unfauv.org](http://unfauv.org)

Pull requests welcome! (Message me if you are not comfortable with git)

**If you do not submit code through github, we have no way to credit you for it**

## Current Proposed technology Stack

- [Arduino](https://www.arduino.cc/) with [firmatta](https://www.arduino.cc/en/Reference/Firmata) using [Johnny-Five](https://github.com/rwaldron/johnny-five)

- Computer vision happens with existing python code

## Getting started

- Please visit the Johnny-Five link above, and go through the blink-led tutorials. There are plenty.
- Play around with circuits with [123d.circuits.io](https://123d.circuits.io/lab)

- Join us on Slack! Message for an invite.

## Future plans

- Calibration based software for the following:
  - vision
  - thrusters
  - stabilization
  - PID
- Need to improve vision detection software. Resources available in software/electrical slack channels
- Currently have some proof of concept code for stabilization code

## Running the current code

### Installing Dependencies 

 - Prior to installing depedencies for running the code it is recommended that your OS is updated. 
 
 #### Ubuntu Linux 14.04 

  - Ensure that system is up to date by entering the following commands in terminal: 

  `sudo apt-get update
   sudo apt-get upgrade`

  - To install the dependencies required for OpenCV, just run the following commands:

  `sudo apt-get install build-essential libgtk2.0-dev libjpeg-dev libtiff4-dev libjasper-dev libopenexr-dev cmake python-dev    python-numpy python-tk libtbb-dev libeigen3-dev yasm libfaac-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev    libvorbis-dev   libxvidcore-dev libx264-dev libqt4-dev libqt4-opengl-dev sphinx-common texlive-latex-extra libv4l-dev      libdc1394-22-dev       libavcodec-dev libavformat-dev libswscale-dev default-jdk ant libvtk5-qt4-dev`

  - You can download manually or run the commands below to get OpenCV
  `cd ~ 
   wget http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.9/opencv-2.4.9.zip
  unzip opencv-2.4.9.zip
  cd opencv-2.4.9`

  - Now we have to generate the Makefile by using cmake
   `mkdir build cd build cmake -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D         INSTALL_PYTHON_EXAMPLES=ON     -D BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON -D WITH_VTK=ON .. `

  - Now, you are ready to compile and install OpenCV 2.4.9:
    `make sudo make install`



- more documentation coming soon! Contact me for now!
