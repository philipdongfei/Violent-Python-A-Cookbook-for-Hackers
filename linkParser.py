from anonBrowser import *
from bs4 import BeautifulSoup
import os
import optparse
import re
def printLinks(url):
    ab = anonBrowser()
    ab.anonymize()
    page = ab.open(url, 'rb')
    html = page.read()
    try:
        print('==========================================')
        print('[+] Printing Links From Regex.')
        link_finder = re.compile('href="(.*?)"')
        links = link_finder.findall(str(html, encoding='UTF-8'))
        print(type(links))
        for link in links:
            print(link)
    except Exception as e:
        print("re find error: " + e)
        pass

    try:
        print('===========================================')
        print('\n[+] Printing Links From BeautifulSoup.')
        soup = BeautifulSoup(html)
        links = soup.findAll(name='a')
        for link in links:
            if link.has_key('href'):
                print(link['href'])
    except Exception as e:
        print("re find error: " + e)
        pass
def main():
    parser = optparse.OptionParser('usage%prog ' + \
        '-u <target url>')
    parser.add_option('-u', dest='tgtURL', type='string',\
        help='specify target url')
    (options, args) = parser.parse_args()
    url = options.tgtURL
    if url == None:
        print(parser.usage)
        exit(0)
    else:
        printLinks(url)
if __name__ == '__main__':
    main()

