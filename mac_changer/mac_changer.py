#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC adress")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC adress")

# the method returns to set of informations, and we are capturing them in variables
(options, arguments) = parser.parse_arg()

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# each element of the list is a word in the command
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])each element omber to change

# this is used like: python mac_changer.py --interface eth0 --mac 00:11:22:33:44