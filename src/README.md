# Arduino Examples for ATtiny85
The examples can be compiled and uploaded using the Arduino IDE with Digistump or our ATtiny85 extension.

## Files
* [Arduino IDE 1.5](http://arduino.cc/en/Main/Software)
* Extensions
  * [ATtiny85](https://github.com/watterott/wattuino/tree/master/src/Arduino)
  * [Digistump](https://github.com/digistump/DigistumpArduino)
* [Libraries](https://github.com/watterott/Arduino-Libs)
  * [light_WS2812](https://github.com/watterott/Arduino-Libs/tree/master/light_WS2812)
  * [TinyWire](https://github.com/watterott/Arduino-Libs/tree/master/TinyWire)
* [Examples](https://github.com/watterott/RPi-WS2812-HAT/tree/master/src)

## Upload
* Open the example.
* Select as Board: **ATtiny85 (internal 16.5MHz)** or **Digispark (16.5MHz)**.
* Select Upload.
* When the compiling has finished and "Uploading..." is shown, unplug and plug the USB connector or press the reset switch to start the bootloader.
* Wait till the upload has finished and "Done uploading" is shown.


# Raspberry Pi Examples

* Activate I2C:

    ```
    $ sudo modprobe i2c_bcm2708 baudrate=100000
    $ sudo modprobe i2c-dev
    ```

* Install i2c-tools:

    ```
    $ sudo apt-get update
    $ sudo apt-get install i2c-tools
    ```

* Test I2C bus:

    ```
    $ sudo i2cdetect -y 1
    ```

* Set first LED (0x00) to red (r=0x7F g=0x00 b=0x00):

    ```
    $ sudo i2cset -y 1 0x20 0x00
    $ sudo i2cset -y 1 0x20 0x7F
    $ sudo i2cset -y 1 0x20 0x00
    $ sudo i2cset -y 1 0x20 0x00
    ```
