#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
  parser = optparse.OptionParser()
  parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC adress")
  parser.add_option("-m", "--mac", dest="new_mac", help="New MAC adress")
  # the method returns to set of informations, and we are capturing them in variables
  (options, arguments) = parser.parse_arg()
  if not options.interface:
    parse.error("[-] Please specify an interface, use --help for more info")
  elif not options.new_mac:
    parse.error("[-] Please specify a new mac, use --help for more info")
  return options

def change_mac(interface, new_mac):
  print("[+] Changing MAC address for " + interface + " to " + new_mac)
  # each element of the list is a word in the command
  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
  subprocess.call(["ifconfig", interface, "up"])each element omber to change

options = get_argument()
change_mac(options.interface, options.new_mac)
# this is used like: python mac_changer.py --interface eth0 --mac 00:11:22:33:44:55