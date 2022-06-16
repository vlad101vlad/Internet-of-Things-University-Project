# Mock semaphore using Raspberry Pi Pico

This is my indivitual project which I have presented during the spring semester at Bábes Bolyai University in the 3rd year of my Bachelor's degree studies.

This small Raspberry Pi Pico project aims to simulate a traffic semaphore. After a set amount of time, the vehicle semaphore will switch between red, yellow and green. The pedestrian semaphore will stay on red until a pedestrian request to cross. When a request is made, the wait led for pedestrians is trigger(yellow), the vehicle semaphore will be set on red and the pedestrian semaphore will be set on green. A buzzer will beep for the whole period when pedestrians are allowed to cross the street

## Pre-requisites
* Raspberry Pi Pico
* Green 10MM LED x2
* Yellow 10MM LED x2
* Yellow 10MM LED x2
* Piezo Element Buzzer x1
* Push (button) switch x2
* Breadboard x1
* (330 ohm) resistors x6
* Male-to-Male Jumper Wires x14
* USB 3.0 to USB tybe B cable
 



## Demo Video
[![Video thumnail](http://img.youtube.com/vi/8uFQqm-ksW8/0.jpg)](https://youtu.be/8uFQqm-ksW8)

## Schematics

#### Raspberry Pi Pico Pins:

![Image of raspberry pi pico pins](https://i.ibb.co/7SSMgNX/Raspberry-Pico.png)

[Reference](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf) 

#### Wiring

![Image of wiring](https://i.postimg.cc/NFRF6smp/Screenshot-2.png)


### Setup and Build

Connect the Raspberry Pi Pico to a laptop and the circuit will start working.
Press any of the two buttons to trigger a green light for the pedestrians.

### Running

The code is run on two threas:
* the main thread: keeps track of the vehicle semaphore and will comute between red, yellow and green
* the second thread: is triggered by the main thread and will run the semaphore for the pedestrians (meanwhile, the main thread is put to sleep)
