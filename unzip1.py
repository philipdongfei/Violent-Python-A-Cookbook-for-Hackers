#!/usr/bin/env python3

import zipfile
def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        return password
    except Exception as inst:
        print(inst)
        return

def main():
    zFile = zipfile.ZipFile('evil.zip')
    passFile = open('dictionary1.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(zFile, str.encode(password))
        if guess:
            print("[+] Password = " + password + "\n")
            zFile.close()
            passFile.close()
            exit(0)
    zFile.close()
    passFile.close()

if __name__ == '__main__':
    main()
