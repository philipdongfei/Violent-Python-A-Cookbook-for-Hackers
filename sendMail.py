#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
def sendMail(user, pwd, to, subject, text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    try:
        smtpServer = smtplib.SMTP('smtp.gmail.com', 587)
        print('[+] Connecting To Mail Server.')
        smtpServer.ehlo()
        print("[+] Starting Encrypted Session.")
        smtpServer.starttls()
        smtpServer.ehlo()
        print("[+] Logging Into Mail Server.")
        smtpServer.login(user, pwd)
        print("[+] Sending Mail.")
        smtpServer.sendmail(user, to,msg.as_string())
        smtpServer.close()
        print("[+] Mail Sent Successfully.")
    except Exception as e:
        print("[-] Sending Mail Failed.")
        print(e)
user = 'philip.dongfei@gmail.com'
pwd = '1979416sting'
sendMail(user, pwd, 'philip.dong@hotmail.com',\
    'Re: Important', 'Test Message')

