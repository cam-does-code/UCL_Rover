from dcmotor import DCMotor       
from machine import Pin, PWM   
from time import sleep 

frequency = 15000 

#Forhjul
FIN1 = PWM(Pin(23),freq=50)    
FIN2 = PWM(Pin(13),freq=50)
FIN3 = PWM(Pin(12),freq=50)   
FIN4 = PWM(Pin(14),freq=50)

#Baghjul
BIN1 = PWM(Pin(22),freq=50)   
BIN2 = PWM(Pin(1),freq=50)
BIN3 = PWM(Pin(3),freq=50)    
BIN4 = PWM(Pin(21),freq=50)
 
dc_motor_FV = DCMotor(FIN1, FIN2)      
dc_motor_FV = DCMotor(FIN1, FIN2, 350, 1023)
dc_motor_FV.forward(50)    
sleep(10)        
dc_motor_FV.stop()  
sleep(10)    
dc_motor_FV.backwards(100)  
sleep(10)       
dc_motor_FV.forward(60)
sleep(10)
dc_motor_FV.stop()

dc_motor_FH = DCMotor(FIN3, FIN4)      
dc_motor_FH = DCMotor(FIN3, FIN4, 350, 1023)
dc_motor_FH.forward(50)    
sleep(10)        
dc_motor_FH.stop()  
sleep(10)    
dc_motor_FH.backwards(100)  
sleep(10)       
dc_motor_FH.forward(60)
sleep(10)
dc_motor_FH.stop()

dc_motor_BV = DCMotor(BIN1, BIN2)      
dc_motor_BV = DCMotor(BIN1, BIN2, 350, 1023)
dc_motor_BV.forward(50)    
sleep(10)        
dc_motor_BV.stop()  
sleep(10)    
dc_motor_BV.backwards(100)  
sleep(10)       
dc_motor_BV.forward(60)
sleep(10)
dc_motor_BV.stop()

dc_motor_BH = DCMotor(BIN3, BIN4)      
dc_motor_BH = DCMotor(BIN3, BIN4, 350, 1023)
dc_motor_BH.forward(50)    
sleep(10)        
dc_motor_BH.stop()  
sleep(10)    
dc_motor_BH.backwards(100)  
sleep(10)       
dc_motor_BH.forward(60)
sleep(10)
dc_motor_BH.stop()