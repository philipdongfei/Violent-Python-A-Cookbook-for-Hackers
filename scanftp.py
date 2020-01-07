import socket
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner):
    f = open("vuln_banners.txt", 'r')
    for line in f.readlines():
        if line in f.readlines():
            if line.strip('\n') in banner:
                print("[+] Server is vulnerable: " + banner.strip('\n'))
    f.close()
    '''
    if "FreeFloat Ftp Server (Version 1.00)" in banner:
        print("[+] FreeFloat FTP Server is vulnerable")
    elif "3Com 3CDaemon FTP Server Version 2.0" in banner:
        print("[+] 3CDaemon FTP Server is vulnerable.")
    elif "Ability Server 2.34" in banner:
        print("[+] Ability FTP Server is vulnerable.")
    elif "Sami FTP Server 2.0.2" in banner:
        print("[+] Sami FTP Server is vulnerable.")
    else:
        print("[-] FTP Server is not vulnerable.")
    return
    '''




def main():
    portList = [21,22,25,80,110,443]
    print("begin to scan:")
    for x in range(1,255):
        ip = "192.168.28."+str(x)
        for port in portList:
            print("scan "+ip+":"+str(port))
            banner = retBanner(ip, port)
            if banner:
                print("[+]"+ip+":"+banner)
                checkVulns(banner)
    print("scan end")
if __name__ == '__main__':
    main()


