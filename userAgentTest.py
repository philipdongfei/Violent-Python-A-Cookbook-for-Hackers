# search agent: http://www.useragentstring.com/pages/useragentstring.php
#!/usr/bin/env python3
import mechanize
def testUserAgent(url, userAgent):
    browser = mechanize.Browser()
    browser.set_handle_robots(False) # solve the problem: "Http Error 403: request disallowed by robots.txt"
    browser.addheaders = userAgent
    page = browser.open(url)
    #print(page.info())
    source_code = page.read()
    print(source_code)
#url = 'http://whatismyuseragent.dotdoh.com/'
#url = 'http://www.163.com/'
url = 'http://www.sina.com.cn'
#userAgent = [('User-agent','Mozilla/5.0 (X11; U; '+\
#    'Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.0.01')]
userAgent = [('User-agent', 'Mozilla/5.0 (Windows; U; '+\
        'Windows NT 6.1;rv:2.2) Gecko/20110201')]
testUserAgent(url, userAgent)

