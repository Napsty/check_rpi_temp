# check_rpi_temp
Monitoring plugin to measure and check board temperature of a Raspberry Pi

## Parameters
-u / --unit  Show temperature in Celsius (c) or Fahrenheit (f), defaults to c

## Usage
```
pi@raspberrypi:~ $ ./check_rpi_temp.py -w 36 -c 42
RPI TEMP WARNING: Temperature 41.90 is higher than warning threshold (36.00) |rpi_temp=41.90;36.00;42.00;;
```
