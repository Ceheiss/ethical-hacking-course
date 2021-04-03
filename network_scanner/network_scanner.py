#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
  scapy.arping(ip)

# You can check IP of your router by running "route -n" in the terminal
scan('')