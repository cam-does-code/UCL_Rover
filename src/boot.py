from DCMotor import DCMotor
from machine import Pin

pin1 = Pin(2, Pin.OUT)  #h1in1
pin2 = Pin(0, Pin.OUT)  #h1in2
pin3 = Pin(4, Pin.OUT)  #h1in3
pin4 = Pin(16, Pin.OUT) #h1in4
pin5 = Pin(33, Pin.OUT)  #h2in3
pin6 = Pin(25, Pin.OUT)  #h2in4
pin7 = Pin(26, Pin.OUT)  #h2in1
pin8 = Pin(27, Pin.OUT) #h2in2
motor1 = DCMotor(pin1, pin2)
motor2 = DCMotor(pin3, pin4)
motor3 = DCMotor(pin7, pin8)
motor4 = DCMotor(pin5, pin6)

x = 0

if x == 1:
    motor1.forward()
    motor2.forward()
    motor3.forward()
    motor4.forward()
    
if x == 2:
    motor1.backwards()
    motor2.backwards()
    motor3.backwards()
    motor4.backwards()
    
if x == 0:
    motor1.stop()
    motor2.stop()
    motor3.stop()
    motor4.stop()