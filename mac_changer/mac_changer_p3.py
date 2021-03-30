#!/usr/bin/env python3

import subprocess
import optparse
import re

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

def get_current_mac(interface):
  ifconfig_result = subprocess.check_output(["ifconfig", interface])
  mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

  if mac_address_search_result:
    return mac_address_search_result.group(0)
  else:
    print("[-] Could not read MAC address,")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
  print("[+] MAC address was succesfully changed to " + current_mac)
else:
  print("[-] MAC address did not get changed.")
# this is used like: python3 mac_changer_p3.py --interface eth0 --mac 00:11:22:33:44:55