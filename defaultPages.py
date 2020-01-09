import ftplib
def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print('[-] Could not list directory contents.')
        print('[-] Skipping To Next Target.')
        return
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print('[+] Found default page: ' + fileName)
            retList.append(fileName)
    return retList
host = '192.168.28.174'
#host = '192.168.95.179'
userName = 'philip'
passWord = 'philip'
ftp = ftplib.FTP(host)
ftp.login(userName, passWord)
print('\n[*] ' + str(host) +\
    ' FTP Logon Succeeded: '+userName+"/"+passWord)
returnDefault(ftp)

