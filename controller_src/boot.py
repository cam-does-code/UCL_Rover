import network
import espnow
import machine

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()   # For ESP8266

e = espnow.ESPNow()
e.active(True)
peer = b'\xbb\xbb\xbb\xbb\xbb\xbb'   # MAC address of peer's wifi interface
e.add_peer(peer)

e.send("Starting...")       # Send to all peers
for i in range(100):
    e.send(peer, str(i)*20, True)
    e.send(b'end')

#https://github.com/GuyCarver/MicroPython/blob/master/esp32/joystick.py

class joystick(object) :
  _x_center = 1789.0
  _y_center = 1817.0
  _pos_x = 4095.0 - _x_center
  _pos_y = 4095.0 - _y_center

  def __init__( self, aX, aY, aButton ) :
    self._jx = machine.ADC(machine.Pin(aX))
    self._jy = machine.ADC(machine.Pin(aY))
    self._jx.width(machine.ADC.WIDTH_12BIT)
    self._jy.width(machine.ADC.WIDTH_12BIT)
    self._jx.atten(machine.ADC.ATTN_11DB)
    self._jy.atten(machine.ADC.ATTN_11DB)
    #Must be pull up.  Pull down doesn't register change.
    self._js = machine.Pin(aButton, machine.Pin.IN, machine.Pin.PULL_UP)

    self._x = 0.0
    self._y = 0.0
    self._button = False

    self._index = 0
    self._xA = [0, 0, 0]
    self._yA = [0, 0, 0]

  @property
  def x( self ) :
    '''Return value from -1.0 to 1.0.'''
    return self._x

  @property
  def y( self ) :
    '''Return value from -1.0 to 1.0.'''
    return self._y

  @property
  def button( self ) :
    '''return True or False.'''
    return self._button

  def update( self ) :
    self._xA[self._index] = self._jx.read()
    self._yA[self._index] = self._jy.read()

    self._index += 1
    if self._index >= 3 :
      self._index = 0

    rx = float(sum(self._xA)) / 3.0 - joystick._x_center
    ry = float(sum(self._yA)) / 3.0 - joystick._y_center
    dx = joystick._pos_x if rx >= 0 else joystick._x_center
    dy = joystick._pos_y if ry >= 0 else joystick._y_center
    self._x = rx / dx
    self._y = ry / dy

    #Value is 1 when not pressed and 0 when pressed.
    self._button = not self._js.value()

while True:
    