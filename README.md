# check_rpi_temp
Monitoring plugin to measure and check board temperature of a Raspberry Pi

## Parameters
```
-u / --unit  Show temperature in Celsius (c) or Fahrenheit (f), defaults to c
-w / --warn  Define warning threshold
-c / --crit  Define critical threshold
```

## Usage
```
pi@raspberrypi:~ $ ./check_rpi_temp.py -w 36 -c 42
RPI TEMP WARNING: Temperature 41.90 is higher than warning threshold (36.00) |rpi_temp=41.90;36.00;42.00;;

pi@raspberrypi:~ $ ./check_rpi_temp.py -w 90 -c 105 -u f
RPI TEMP CRITICAL: Temperature 106.34 is higher than critical threshold (105.00) |rpi_temp=106.34;90.00;105.00;;
```

## NRPE example
```
# Without command args
command[check_rpi_temp]=/usr/lib/nagios/plugins/check_rpi_temp.py

# With command args
command[check_rpi_temp]=/usr/lib/nagios/plugins/check_rpi_temp.py -w $ARG1$ -c $ARG2$
```
