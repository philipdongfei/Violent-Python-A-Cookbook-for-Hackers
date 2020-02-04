import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
def calTSN(tgt):
    seqNum = 0
    preNum = 0
    diffSeq = 0
    for x in range(1, 5):
        if preNum != 0:
            preNum = seqNum
        pkt = IP(dst=tgt) / TCP()
        ans = sr1(pkt, verbose=0)
        seqNum = ans.getlayer(TCP).seq
        diffSeq = seqNum - preNum
        print('[+] TCP Seq Difference: ' + str(diffSeq))
    return seqNum + diffSeq

#tgt = "192.168.28.188"
tgt = "114.114.114.114"
seqNum = calTSN(tgt)
print("[+] Next TCP Sequence Number to ACK is: " + str(seqNum+1))

