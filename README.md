# RPi-WS2812-HAT
WS2812B intelligent RGB-LED Matrix HAT (Hardware Attached on Top) for Raspberry Pi Model A+ and B+.


![RPi-WS2812-HAT](https://raw.github.com/watterott/RPi-WS2812-HAT/master/img/rpi-ws2812-hat.jpg)


## Features
* WS2812 RGB-LED with 16777216 colors and built-in controller with serial interface
* ID EEPROM
* Atmel ATtiny85 microcontroller with [Micronucleus](https://github.com/micronucleus/micronucleus) USB Bootloader
* [Raspberry Pi HAT](https://github.com/raspberrypi/hats) compatible


## Hardware
* [Schematics + Layout](https://github.com/watterott/RPi-WS2812-HAT/tree/master/pcb)


## Software
* [Arduino Examples](https://github.com/watterott/RPi-WS2812-HAT/tree/master/src)
* [Little Wire](http://littlewire.cc) can also be used on the ATtiny85.
* For direct control of WS2812 LEDs from the Raspberry Pi have a look at the examples from: [626Pilot](https://github.com/626Pilot/RaspberryPi-NeoPixel-WS2812) and [jgarff](https://github.com/jgarff/rpi_ws281x).
