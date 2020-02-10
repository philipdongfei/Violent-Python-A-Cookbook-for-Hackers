#!/usr/bin/env python3
from bluetooth import *
def sdpBrowse(addr):
    print("scan addr: " + addr)
    services = find_service(address=addr)
    for service in services:
        name = service['name']
        proto = service['protocol']
        port = str(service['port'])
        print('[+] Found ' + str(name) + ' on ' + \
            str(proto) + ':' + port)
#sdpBrowse('14:20:5E:24:E4:E7')
sdpBrowse('18:AF:61:2E:B3:33')
#sdpBrowse('2C:DD:95:2E:D3:E6')

