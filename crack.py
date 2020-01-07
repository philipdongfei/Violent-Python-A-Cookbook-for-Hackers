import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print("[+] Found Password: " + word + "\n")
            return
    print("[-] Password Not Found.\n")
    return
def testPass512(cryptPass):
    salt = cryptPass[0:11]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptword = crypt.crypt(word,salt)
        if (cryptword == cryptPass):
            print("[+] Found Password: " + word + "\n")
            return
    print("[-] Password not found.\n")
    return

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print("[*] Cracking Password For: " + user)
            #print("sha256:\n")
            #testPass(cryptPass)
            print("sha512:\n")
            testPass512(cryptPass)

if __name__ == "__main__":
    main()

