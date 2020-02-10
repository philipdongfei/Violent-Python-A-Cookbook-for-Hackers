#!/usr/bin/env python2
import obexftp
try:
    btPrinter = obexftp.client(obexftp.BLUETOOTH)
    btPrinter.connect('18:AF:61:2E:B3:33', 2)
    btPrinter.put_file('~/Pictures/IMG_0011.JPG')
    print '[+] Printed Ninja Image.'
except Exception as e:
    print '[-] Failed to print Ninja Image.'
    print e
