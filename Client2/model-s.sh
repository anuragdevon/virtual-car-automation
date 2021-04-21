#!/bin/bash

# Basic Layout
figlet Car Networking Using Android
echo ""
echo "Checking Android Version..."
sleep 2
neofetch 
echo ""
figlet Model-S
echo ""
echo "Generating empty files..."
sleep 2
OUTPUT=model-s.txt
echo "Files Generated Successfully!"
echo ""
sleep 1
echo "Execution getting started... "
echo `date` > $OUTPUT
echo ""
sleep 2

# Reading in writing of sensors values
echo "Reading Light Values..."  
termux-sensor -s "ts12560 ambient light" -n 5 -d 1000 >> $OUTPUT
echo "Reading Proximity Values..."
termux-sensor -s "PROXIMITY" -n 5 -d 1000 >> $OUTPUT
echo "Reading Accelaration Value... "
termux-sensor -s "ACCELEROMETER" -n 5 -d 1000 >> $OUTPUT
echo "Reading Orientation Value... "
echo ""
termux-sensor -s "ORIENTATION" -n 5 -d 1000 >> $OUTPUT

sleep 1
echo "Saving the generated values..."
sleep 1
echo "Files Saved Successfully!"
sleep 2

echo "Extracting information from raw Data."
echo "Please wait..."
echo ""
sleep 2
python DataGenS.py
echo "Extraction Completed Successfully!"
sleep 1
echo "File saved as json format in the current directory"
sleep 2
echo ""
echo ""
echo "Starting Internal Model-S Execution..."
echo ""
sleep 1
python model-s.py

echo ""
figlet Model-S Terminates...

