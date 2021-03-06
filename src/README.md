# Arduino Examples for ATtiny85
The examples can be compiled and uploaded using the Arduino IDE with Digistump or our ATtiny85 extension.

## Files
* [Arduino IDE v1.6](http://arduino.cc/en/Main/Software)
* Extensions
  * [ATtiny85](https://github.com/watterott/wattuino/tree/master/src/Arduino)
  * [Digistump](https://github.com/digistump/DigistumpArduino)
* [Micronucleus Windows Driver](https://github.com/watterott/wattuino/tree/master/src/Arduino/drivers/Micronucleus)
* [Libraries](https://github.com/watterott/Arduino-Libs)
  * [light_WS2812](https://github.com/watterott/Arduino-Libs/tree/master/light_WS2812)
  * [TinyWire](https://github.com/watterott/Arduino-Libs/tree/master/TinyWire)
* [Examples](https://github.com/watterott/RPi-WS2812-HAT/tree/master/src)

## Upload
* Open the example.
* Select under Tools->Board: **ATtiny85 (internal 16.5MHz)** or **Digispark (16.5MHz)**.
* Select Upload.
* When the compiling has finished and "Uploading..." is shown, unplug and plug back in the USB connector or press the reset switch to start the bootloader.
* Wait till the upload has finished and "Done uploading" is shown.


# Raspberry Pi Examples

* Upload the ```I2C_Slave.ino``` example to the ATtiny85 on the RPi-WS2812-HAT.

* Install i2c-tools and python-smbus:

    ```
    $ sudo apt-get install i2c-tools
    $ sudo apt-get install python-smbus
    ```

* Activate I2C device:

    ```
    $ sudo modprobe i2c_bcm2708 baudrate=400000
    $ sudo modprobe i2c-dev
    ```

* Test I2C bus:

    ```
    $ sudo i2cdetect -y 1
    ```

* Download and run the Python examples (Random.py, Fill.py...):

    ```
    $ wget https://github.com/watterott/RPi-WS2812-HAT/raw/master/src/Random.py
    $ sudo python Random.py
    ```
