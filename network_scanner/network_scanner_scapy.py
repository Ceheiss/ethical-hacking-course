#!/usr/bin/env python
# This program is to discover all clients in the same network
# It works by using ARP requests
import scapy.all as scapy

#sccapy can receive a range as well, I enter like:
# scan("10.0.2.1/24")
def scan(ip):
  scapy.arping(ip)

# You can check IP of your router by running "route -n" in the terminal
scan('10.0.2.1')
