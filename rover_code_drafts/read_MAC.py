import ubinascii
from machine import unique_id
import network

wlan_sta = network.WLAN(network.STA_IF)
wlan_sta.active(True)

print("MAC adressen er: ",ubinascii.hexlify(unique_id(), ":").decode())
print("MAC adressen i bytes er: ", wlan_sta.config('mac'))