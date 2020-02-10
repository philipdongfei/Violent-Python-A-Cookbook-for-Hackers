#!/usr/bin/env python3
import re
def findCreditCard(raw):
    #raw = pkt.sprintf('%Raw.load%')
    americaRE = re.findall("3[47][0-9]{13}", raw)
    masterRE = re.findall('5[1-5][0-9]{14}', raw)
    visaRE = re.findall('4[0-9]{12}(?:[0-9]{3})?', raw)
    if americaRE:
        print("[+] Found American Express Card: " + americaRE[0])
    if masterRE:
        print('[+] Found MasterCard: ' + masterRE[0])
    if visaRE:
        print('[+] Found Visa Card: ' + visaRE[0])
def main():
    tests=[]
    tests.append('I would like to buy 1337 copies of that dvd')
    tests.append('Bill my card: 378282246310005 for \$2600')
    tests.append('I would like to buy a book')
    tests.append('Bill my card: 4392260020600951 for \$5')
    for test in tests:
        findCreditCard(test)
if __name__ == '__main__':
    main()

