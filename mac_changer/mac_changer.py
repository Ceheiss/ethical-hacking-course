#!/usr/bin/env python

import subprocess

# second argument is the interface name (should be variable)
# mac number choice should also be variable
subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)