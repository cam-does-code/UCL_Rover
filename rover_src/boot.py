import hbro
from machine import Pin
import network
import espnow

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()   # Because ESP8266 auto-connects to last Access Point

e = espnow.ESPNow()
e.active(True)
peer = b'\xaa\xaa\xaa\xaa\xaa\xaa'   # MAC address of peer's wifi interface
e.add_peer(peer)

while True:
    host, msg = e.recv()
    if msg:             # msg == None if timeout in recv()
        print(host, msg)
        if msg == b'end':
            break
    #x equal to value from joystick something something ???
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

    if msg == b'left'
        hbro.motor_a_forward

    if msg == b'right'
        hbro.motor_b_forward


    if msg == b'stop':
        hbro.motor_a_stop()
        hbro.motor_b_stop()
        hbro.motor_c_stop()
        hbro.motor_d_stop()
