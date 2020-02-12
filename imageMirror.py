from anonBrowser import *
from bs4 import BeautifulSoup
import os
import optparse
def mirrorImage(url, dir):
    ab = anonBrowser()
    ab.anonymize()
    html = ab.open(url)
    soup = BeautifulSoup(html, "html5lib")
    image_tags = soup.findAll('img')
    for image in image_tags:
        filename = image['src'].lstrip('http://')
        filename = os.path.join(dir, \
            filename.replace('/', '_'))
        print('[+] Saving ' + str(filename))
        data = ab.open(image['src']).read()
        ab.back()
        save = open(filename, 'wb')
        save.write(data)
        save.close()
def main():
    parser = optparse.OptionParser('usage%prog '+\
        '-u <target url> -d <destination directory>')
    parser.add_option('-u', dest='tgtURL', type='string',\
        help='specify target url')
    parser.add_option('-d', dest='dir', type='string',\
        help='specify destination directory')
    (options, args) = parser.parse_args()
    url = options.tgtURL
    dir = options.dir
    if url == None or dir == None:
        print(parser.usage)
        exit(0)
    else:
        try:
            mirrorImage(url, dir)
        except Exception as e:
            print('[-] Error Mirroring Images.')
            print('[-]' + str(e))
if __name__ == '__main__':
    main()

