## Pi-Fan
A Raspberry Pi Smart Fan that can be controlled through a browser or app  

This is a smart iot device that is a fan that can be controlled from anywhere.  

The current implementation of the project only works on a local network.  
<br>
**This is a work in progress** 
<br>

### Here is a list of the parts you will need

1. Raspberry Pi 3 -- may also work with other versions
2. Power supply for Pi
3. 4-AA Batteries and Holder
4. Mini Breadboard
5. Motor driver chip
6. 1 DC Motor
7. 1 Fan Blade
8. 1 DHT11 Temp/Humidity Sensor
8. M-M and M-F wires


### Directions

1. Connect the motor driver board on output 1 to one side of the motor.
May have to test the motor to make it spin the right way.

2. Connect the other side of the motor to output 2 of the motor driver.

3. Connect pin 12 of the Pi to input 1.

4. Connect the power of the battery to Vcc on the motor driver

5. Connect the ground of the battery to Gnd on the motor driver

6. Place the DHT11 chip on the breadboard, and connect the power 
of the chip to the 3.3 pin on the Pi and the ground to the ground
of the Pi.

7. Connect pin 17 on the Pi to the data of the sensor.

8. Make sure Flask and the Adafruit library for the DHT11 chip are installed
on your Pi.

9. Export main.py to Flask and start Flask by running: flask start.
