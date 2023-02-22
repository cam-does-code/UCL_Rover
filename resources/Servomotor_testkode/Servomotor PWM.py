from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(23), freq=5000)

for duty_cycle in range(0, 50, 1):
        servo.duty(duty_cycle)
        sleep(0.001)

print("Slut!")