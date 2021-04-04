#!/usr/bin/env python
# STEPS
# 1. Create arp request directed to broadcast MAC asking for IP.
# 2. Send packet and receive response.
# 3. Parse the response
# 4. Print result

import scapy.all as scapy

def scan(ip):
  # we are providing a value to the pdst argument
  arp_request = scapy.ARP(pdst=ip)

scan('')