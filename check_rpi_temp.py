#!/usr/bin/env python2
######################################################################
# check_rpi_temp.py
#
# This monitoring plugin can be used to constantly monitor the board
# temperature of a Raspberry Pi computer
# 
# Licence : GNU General Public Licence (GPL) http://www.gnu.org/
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#
# Copyright (c) 2019 Claudio Kuenzler www.claudiokuenzler.com
#
# History:
# 20190930 0.1: Created plugin
######################################################################
# version
version=0.1

# imports
import os
import sys
import argparse
import subprocess

# defaults
unit='c'
temp=0
warn=0
crit=0

# Parameters
usage = "Usage: %prog [-u (c|f)]\n"

parser = argparse.ArgumentParser(description='Monitor temperature of Raspberry Pi')
parser.add_argument('-u', '--unit', dest='unit', help='Set c for celsius or f for fahrenheit degrees')
parser.add_argument('-w', '--warning', dest='warn', type=float, help='Set warning threshold')
parser.add_argument('-c', '--critical', dest='crit', type=float, help='Set critical threshold')
args = parser.parse_args()

if (args.unit): 
    unit=args.unit

if (args.warn): 
    warn=args.warn

if (args.crit): 
    crit=args.crit


# Get temperature
temp = os.popen("/usr/bin/vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*'").read()
temp = float(temp)

if (unit == 'f'):
    temp = (temp*9/5)+32

# Prep performance data
perfdata = "|rpi_temp=%.2f;%.2f;%.2f;;" % (temp, warn, crit)

# Check against thresholds
if (crit > 0 and temp>=crit):
    print("RPI TEMP CRITICAL: Temperature %.2f is higher than critical threshold (%.2f) %s" % (temp, crit, perfdata))
    sys.exit(2)
elif (warn > 0 and temp>=warn):
    print("RPI TEMP WARNING: Temperature %.2f is higher than warning threshold (%.2f) %s" % (temp, warn, perfdata))
    sys.exit(1)
else:
    print("RPI TEMP OK: Temperature %.2f degrees %s %s" % (temp, unit, perfdata))
    sys.exit(0)

