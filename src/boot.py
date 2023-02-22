from motor import DCMotor
from machine import Pin

pin1 = Pin(, Pin.OUT)  
pin2 = Pin(, Pin.OUT)  
pin3 = Pin(, Pin.OUT)  
pin4 = Pin(, Pin.OUT) 
pin5 = Pin(, Pin.OUT) 
pin6 = Pin(, Pin.OUT)  
pin7 = Pin(, Pin.OUT)  
pin8 = Pin(, Pin.OUT) 
motor1 = DCMotor(pin1, pin2)
motor2 = DCMotor(pin3, pin4)
motor3 = DCMotor(pin7, pin8)
motor4 = DCMotor(pin5, pin6)

x = 0
while(True):
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