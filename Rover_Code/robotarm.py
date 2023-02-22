from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(23), freq=50)

for duty_cycle in range(20, 120, 1):
        servo.duty(duty_cycle)
        sleep(0.3)

print("Nu er maden klar!")

#Allans løsning...

def main1():
        from machine import Pin, PWM
        from time import sleep
        servo = PWM(Pin(23), freq=50)

        for duty_cycle in range(20, 120, 1):
                servo.duty(duty_cycle)
                sleep(0.6)
                if duty_cycle == 119:
                        print("Nu er maden klar!")


