#!/usr/bin/env python3
import time
from bluetooth import *
alreadyFound = []
def findDevs():
    print('[-] Scanning for Bluetooth Devices.')
    foundDevs = discover_devices(lookup_names=True)
    for (addr, name) in foundDevs:
        if addr not in alreadyFound:
            print('[*] Found Bluetooth Devices: ' + str(name))
            print('[+] MAC address: ' + str(addr))
            alreadyFound.append(addr)
while True:
    findDevs()
    time.sleep(5)

