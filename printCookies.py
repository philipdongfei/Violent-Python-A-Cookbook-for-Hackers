#!/usr/bin/env python3
import mechanize
import http.cookiejar as cookielib
def printCookies(url):
    browser = mechanize.Browser()
    cookie_jar = cookielib.LWPCookieJar()
    browser.set_handle_robots(False)
    browser.set_cookiejar(cookie_jar)
    page = browser.open(url)
    for cookie in cookie_jar:
        print(cookie)
#url = 'http://www.syngress.com'
#url = 'http://www.sina.com.cn'
url = 'http://www.csdn.net'
printCookies(url)

