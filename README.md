# Car-Networking Simulation Using Android
Using Android-Mobile in-built Sensor, tried to simulate the netwokring of cars.

## Pre-requisites:
  - Python version 3.8.5
  - Termux version 0.101
  - Android version 7.0 or above
## Tags:
[![Python](https://img.shields.io/badge/-Python-black?style=flat&logo=python&link=https://github.com/Anuragkar234)](https://github.com/Anuragkar234)
[![Bash](https://img.shields.io/badge/-Bash-black?style=flat&logo=bash&link=https://github.com/Anuragkar234)](https://github.com/Anuragkar234)
## How to get stared:
  - Install Termux and Termux api using playstore in android.
  - Open Termux and update it through ` pkg apt update `
  - Incase upgradation is required, use ` pkg apt upgrade `
  - Install termux api using ` pkg install termux-api `
  - Install the requirements:
    - ` pkg install python `
    - ` pkg install neofetch `
    - ` pkg install figlet `
    - ` pkg install vim ` or you can use `nano`
  - Using termux-sensor -l check all the available sensors.
  - Check for Light, Accelerometer, gyroscope, and Proximity sensor.
  - Using ` termux-sensor -s "SensorName" `, you can check the values, use `termux-sensor --help` to check more methods to display.
  - Since android does not allow us to run executable files inside internal file system we need to copy the contents to termux home directory which is an emulatorm hence we can run executable files, run the following commands:
    - ` termux-storage-setup`, this will grant access to internal storage.
    - move to the directory where you have saved the files, check `pwd` and copy it.
    - Come to home directory using ` cd ~/ `
    - copy the files using ` cp -r /paste/the/directory/copied/ ~/destination `
  - Open client's bash script and chnage the sensors variables you want to use as mentioned above.
  - Make the bash executable using ` chmod +x model-s.sh  ` or ` chmod +x model-y.sh `
  - Run the script using ` ./model-y.sh ` or ` ./model-y.sh `
  - TO BE CONTINUED...
   
## ScreenShots:
  - ![demo4](./4.jpeg?raw=true "IOT")
  - ![demo2](./2.jpeg?raw=true "IOT")
  - ![demo2](./1.png?raw=true "IOT")

