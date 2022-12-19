# Ultrasonic Sensor 

Microcontroller: Raspberry Pi Pico  
Sensor: HC-SR04  

## Connections

Sensor - Pico

- **Power:**  VCC - VBUS (As operating voltage is 5V)
- **Ground:** GND - GND  (Any GND)
- **Send:** TRIG - GP1 
- **Recieve:** ECHO - GP0

We can connect to any GPIO pins but remember to change in code.

## Setup

- **Sound waves**
  - Speed of sound : Varies with temprature, adiabatic const, molecutlar mass etc. Here i used an [approximation](http://hyperphysics.phy-astr.gsu.edu/hbase/Sound/souspe3.html) that varies only with temprature as pico has that capability.
- **Sensor**
  - If you set the trigger pin to high for 5-10 micro seconds it transmits 8 pulses at 40 KHz which is done to distinguish this from other ultrasonic noise. Then echo pins goes high and remains so until sensor detects the wave back, it has a time out of 38ms. [for more](https://lastminuteengineers.com/arduino-sr04-ultrasonic-sensor-tutorial/).
 - **Range**
    - 2cm to 400cm, but in real use below 4 cm it's inaccurate so warnings are there.
  


