#!/usr/bin/env python3

import zipfile
zFile = zipfile.ZipFile("evil.zip", 'r')
passFile = open('dictionary.txt')
for line in passFile.readlines():
    password = line.strip('\n')
    try:
        zFile.extractall(pwd=password)
        print("[+] Password = " + password + '\n')
        zFile.close()
        passFile.close()
        exit(0)
    except Exception as inst:
        print(type(inst))
        print(inst)

'''
try:
    zFile.extractall(pwd=b'oranges')
except Exception as inst:
    print(type(inst))
    #print(inst.args)
    print(inst)
zFile.extractall(pwd=b'secret')
zFile.close()
'''
