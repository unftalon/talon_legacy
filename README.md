# RoboSub
## this repository is here for archival purposes only. it is currently in the process of being converted to the main repository and modified for ROS.

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


## Installing Dependencies 

 - Prior to installing depedencies for running the code it is recommended that your OS is updated. 
 
 #### Ubuntu Linux 14.04 

  - Ensure that your system is up to date by entering the following commands in terminal: 

    `sudo apt-get update && sudo apt-get upgrade`

  - To install the dependencies required for OpenCV, just run the following commands:
	  
	  ```
      sudo apt-get install build-essential libgtk2.0-dev libjpeg-dev libtiff4-dev libjasper-dev libopenexr-dev cmake  python-dev    
	  python-numpy python-tk libtbb-dev libeigen3-dev yasm libfaac-dev libopencore-amrnb-dev                        
	  libopencore-amrwb-dev libtheora-dev    libvorbis-dev   libxvidcore-dev libx264-dev libqt4-dev libqt4-opengl-dev              
	  sphinx-common texlive-latex-extra libv4l-dev    libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev    
	  default-jdk ant libvtk5-qt4-dev
	  ```

  - You can download manually or run the commands below to get OpenCV
    
	  ```
	  cd ~                                                                                                                        
	  wget http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.9/opencv-2.4.9.zip                                  
	  unzip opencv-2.4.9.zip                                                                                                       
	  cd opencv-2.4.9
	  ```

  - Now we have to generate the Makefile by using cmake
     
	  ```
      mkdir build cd build cmake -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D         
	  INSTALL_PYTHON_EXAMPLES=ON  -D BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON -D WITH_VTK=ON .. 
	  ```

  - Now, you are ready to compile and install OpenCV 2.4.9:
     `make sudo make install`
	
 #### Windows  

  1. Ensure that system is up to date prior to installing software: 
  
  2. Download and install [Python 2.7](https://www.python.org/getit/releases/2.7.2). You need to install the 32 bit version of Python. Opencv currently doesn't work with the 64 bit version 
  
  3. Install [Numpy](http://sourceforge.net/projects/numpy/files/NumPy/1.6.1/numpy-1.6.1-win32-superpack-python2.7.exe/download).  Numpy is an extension to the Python programming language, adding support for large, multi-dimensional arrays and matrices. 
  
  4. Install [Scipy](http://sourceforge.net/projects/scipy/files/scipy/0.9.0/scipy-0.9.0-win32-superpack-python2.7.exe/download).  SciPy is a scientific computing library for python.
  
  5. Download [Opencv](http://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.4.11/opencv-2.4.11.exe/download) 
		
		1. The exe will extract opencv. Exact to C:/
		2. copy the content of C:/opencv/build/python2.7 to C:/Python27/Lib/site-packages
		
  6. Add "C:/Python2.7;C:/OpenCV2.2/bin" to PATH variable
		
		1. Hold Win and press Pause.
		2. Click Advanced System Settings.
		3. Click Environment Variables.
		4. Append ;C:\python27;C:/OpenCV2.2/bin; to the Path variable.
		
## Running the current code
   
   1. Download zip file containing [code](https://github.com/OspreyRobotics/RoboSub/archive/master.zip)
   2. Unzip file 
   3. Go to cameraTrackingAPI folder and delete cv2.so file (Note the cv2.so is a compiled code that was generated on a Raspiberry PI. Code will not work unless these file are generated again)
   4. Delete the cv2.so file in cameraTrackingAPI/ospery_diver folder
   5. Run the code:
		1. The driver program, colorDetector.py is located in the cameraTrackingAPI
		2. To run the progam:
		
		C:\Users\Coder\Documents\RoboSub\cameraTrackingAPI>python colorDetector.py

		
		



