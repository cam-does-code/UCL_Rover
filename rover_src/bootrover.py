import hbro
import network
import espnow
import machine
import time

p4 = machine.Pin(4)
#servo1 = machine.PWM(p4,freq=50)
# duty for servo is between 40 - 115
#servo.duty(100)
# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()   # Because ESP8266 auto-connects to last Access Point

e = espnow.ESPNow()
e.active(True)
peer = b'@\x91Q\x9b\x18\x98'   # MAC address of peer's wifi interface
e.add_peer(peer)

servo1 = machine.PWM(machine.Pin(23), freq=50)
servo2 = machine.PWM(machine.Pin(22), freq=50)
servo3 = machine.PWM(machine.Pin(21), freq=50)
servo4 = machine.PWM(machine.Pin(19), freq=50)

class HCSR04:
    """
    Driver to use the untrasonic sensor HC-SR04.
    The sensor range is between 2cm and 4m.
    The timeouts received listening to echo pin are converted to OSError('Out of range')
    """
    # echo_timeout_us is based in chip range limit (400cm)
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30):
        """
        trigger_pin: Output pin to send pulses
        echo_pin: Readonly pin to measure the distance. The pin should be protected with 1k resistor
        echo_timeout_us: Timeout in microseconds to listen to echo pin.
        By default is based in sensor limit range (4m)
        """
        self.echo_timeout_us = echo_timeout_us
        # Init trigger pin (out)
        self.trigger = machine.Pin(trigger_pin, mode=machine.Pin.OUT, pull=None)
        self.trigger.value(0)

        # Init echo pin (in)
        self.echo = machine.Pin(echo_pin, mode=machine.Pin.IN, pull=None)

    def _send_pulse_and_wait(self):
        """
        Send the pulse to trigger and listen on echo pin.
        We use the method `machine.time_pulse_us()` to get the microseconds until the echo is received.
        """
        self.trigger.value(0) # Stabilize the sensor
        time.sleep_us(5)
        self.trigger.value(1)
        # Send a 10us pulse.
        time.sleep_us(10)
        self.trigger.value(0)
        try:
            pulse_time = machine.time_pulse_us(self.echo, 1, self.echo_timeout_us)
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110: # 110 = ETIMEDOUT
                raise OSError('Out of range')
            raise ex

    def distance_mm(self):
        """
        Get the distance in milimeters without floating point operations.
        """
        pulse_time = self._send_pulse_and_wait()

        # To calculate the distance we get the pulse_time and divide it by 2
        # (the pulse walk the distance twice) and by 29.1 becasue
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.34320 mm/us that is 1mm each 2.91us
        # pulse_time // 2 // 2.91 -> pulse_time // 5.82 -> pulse_time * 100 // 582
        mm = pulse_time * 100 // 582
        return mm

    def distance_cm(self):
        """
        Get the distance in centimeters with floating point operations.
        It returns a float
        """
        pulse_time = self._send_pulse_and_wait()

        # To calculate the distance we get the pulse_time and divide it by 2
        # (the pulse walk the distance twice) and by 29.1 becasue
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.034320 cm/us that is 1cm each 29.1us
        cms = (pulse_time / 2) / 29.1
        return cms

sensor1 = HCSR04(triggerpin1, echopin1)
sensor2 = HCSR04(triggerpin2, echopin2)

while True:
    host, msg = e.recv()
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


