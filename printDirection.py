#!/usr/bin/env python3
import dpkt
import socket
def printPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print('[+] Src: ' + src + ' --> Dst: ' + dst)
        except:
            pass
def main():
    f = open('geotest.pcap', 'rb')
    pcap = dpkt.pcap.Reader(f)
    printPcap(pcap)
if __name__ == '__main__':
    main()

