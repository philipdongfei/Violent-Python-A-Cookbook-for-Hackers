from bluetooth import *
def rfcommCon(addr, port):
    sock = BluetoothSocket(RFCOMM)
    try:
        sock.connect(addr, port)
        print('[+] RFCOMM Port ' + str(port) + ' open')
        sock.close()
    except Exception as e:
        print('[-] RFCOMM Port ' + str(port) + ' closed')
for port in range(1, 30):
    #rfcommCon('14:20:5E:24:E4:E8', port)
    #rfcommCon('90:B9:31:98:8B:E4', port)
    rfcommCon('18:AF:61:2E:B3:33', port)
    #rfcommCon('90:B9:31:98:8B:E4', port)

