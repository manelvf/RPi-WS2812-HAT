import time
import smbus
bus = smbus.SMBus(1)
addr = 0x20 #default: 0x20
intensity = 50 #0...255

#switch off leds
for x in range(64):
  bus.write_i2c_block_data(addr, x, [0, 0, 0]) #led red green blue
  time.sleep(0.005) #wait 5ms

#fade on leds
for i in range(intensity):
  for x in range(64):
    bus.write_i2c_block_data(addr, x, [0, 0, i]) #led red green blue
    time.sleep(0.005) #wait 5ms
