import time
import smbus
from random import randint

bus = smbus.SMBus(1)
addr = 0x20 #default: 0x20
intensity = 50 #0...255

#switch off leds
for x in range(64):
  bus.write_i2c_block_data(addr, x, [0, 0, 0]) #led red green blue
  time.sleep(0.005) #wait 5ms

#switch on random leds
while True:
  x = randint(0, 63)
  r = randint(0, intensity)
  g = randint(0, intensity)
  b = randint(0, intensity)
  bus.write_i2c_block_data(addr, x, [r, g, b]) #led red green blue
  time.sleep(0.1) #wait 100ms
