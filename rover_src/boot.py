import hbro
import network
import espnow
import machine
import time
import hcsr04

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)
sta.active(True)
#sta.disconnect()   # Because ESP8266 auto-connects to last Access Point

e = espnow.ESPNow()
e.active(True)
peer = b'@\x91Q\x9b\x18\x98'   # MAC address of controller
#peer = b'$\xd7\xeb\x0f\xc9d'   # MAC address of rover
e.add_peer(peer)

servo1 = machine.PWM(machine.Pin(23), freq=50)
servo2 = machine.PWM(machine.Pin(22), freq=50)
servo3 = machine.PWM(machine.Pin(21), freq=50)
servo4 = machine.PWM(machine.Pin(19), freq=50)

sensor1 = hcsr04(trigger_pin=33, echo_pin=32, echo_timeout_us=10000)
sensor2 = hcsr04(trigger_pin=17, echo_pin=16, echo_timeout_us=10000)

# hbro.motor_a_stop()
# time.sleep(1)
# hbro.motor_b_stop()
# time.sleep(1)
# hbro.motor_c_stop()
# time.sleep(1)
# hbro.motor_d_stop()

while True:
    host, msg = e.recv()
    print('harald')
    if msg:             # msg == None if timeout in recv()
        print(host, msg)
        if msg == b'end':
            break
    # x equal to value from joystick something something ???
    if msg == b'forward':
        hbro.motor_a_forward()
        hbro.motor_b_forward()
        hbro.motor_c_forward()
        hbro.motor_d_forward()
        
    if msg == b'backwards':
       hbro.motor_a_backwards()
       hbro.motor_b_backwards()
       hbro.motor_c_backwards()
       hbro.motor_d_backwards()

    if msg == b'left':
        hbro.motor_a_forward()

    if msg == b'right':
        hbro.motor_b_forward()

    if msg == b'stop':
        hbro.motor_a_stop()
        hbro.motor_b_stop()
        hbro.motor_c_stop()
        hbro.motor_d_stop()

    if msg == b'crane':
        servo1.duty(70)  # midt
        time.sleep(1)
        servo4.duty(80)  # hånd åben
        time.sleep(1)
        servo2.duty(90)  # max framad
        time.sleep(1)
        servo3.duty(50)  # max ned
        time.sleep(1)
        servo4.duty(20)  # hånd låkket
        time.sleep(1)
        servo3.duty(100)  # max op
        time.sleep(1)
        servo2.duty(50)  # max bag ud
        time.sleep(1)

    if msg == b'dance':
        hbro.motor_a_stop()
        hbro.motor_b_stop()
        hbro.motor_c_stop()
        hbro.motor_d_stop()
        time.sleep(1)
        hbro.motor_b_forward()
        time.sleep(2)
        hbro.motor_b_stop()
        time.sleep(1)
        for i in range (100):
            if sensor1.distance_cm() < 10.0:
                hbro.motor_a_forward()
                time.sleep(0.5)
                hbro.motor_a_stop()
            if sensor2.distance_cm() < 10.0:
                hbro.motor_b_forward()
                time.sleep(0.5)
                hbro.motor_b_stop()
            else:
                hbro.motor_a_forward()
                hbro.motor_b_forward()
                hbro.motor_c_forward()
                hbro.motor_d_forward()
                time.sleep(1)
                hbro.motor_a_stop()
                hbro.motor_b_stop()
                hbro.motor_c_stop()
                hbro.motor_d_stop()


