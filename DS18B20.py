from machine import Pin
import onewire
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("client ip address", port))

ow = onewire.OneWire(Pin(12))
ds = onewire.DS18B20(ow)
roms = ds.scan()

while True:
    for rom in roms:
       ds.convert_temp()
       time.sleep_ms(750)
       c = ds.read_temp(rom)
       f = (c * 1.8) + 32
       s.write('%.2f' %f)
       time.sleep(5)
