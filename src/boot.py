import hbro
from machine import Pin

x = 0
while(True):
    #x equal to value from joystick something something ???
    if x == 1:
        hbro.motor_a_forward()
        hbro.motor_b_forward()
        hbro.motor_c_forward()
        hbro.motor_d_forward()
        
    if x == 2:
       hbro.motor_a_backwards()
       hbro.motor_b_backwards()
       hbro.motor_c_backwards()
       hbro.motor_d_backwards()

    if x == 0:
        hbro.motor_a_stop()
        hbro.motor_b_stop()
        hbro.motor_c_stop()
        hbro.motor_d_stop()
