import urllib3
import optparse
#import requests
from urllib.parse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS

def findMagnets(url):
    print('[+] Finding Magnets on ' + url)
    http = urllib3.PoolManager()
    urlContent = http.request('GET', url)
    soup = BeautifulSoup(urlContent.data, "html.parser")
    magTags = soup.findAll('li')
    return magTags
def downloadMagnet(magTag):
    try:
        print('[+] Download magnet...')
        magSrc = magTag['data-magnet']
        print('magnet: ' + magSrc)
        path='mags.txt'
        mags_file = open(path, 'a')
        mags_file.write(magSrc+'\n')
        mags_file.close()
        return magSrc
    except:
        return ''

def main():
    parser = optparse.OptionParser('usage%prog "+\
            "-u <target url>')
    parser.add_option('-u', dest='url', type='string',
            help='specify url address')
    (options, args) = parser.parse_args()
    url = options.url
    if url == None:
        print(parser.usage)
        exit(0)
    else:
        magTags = findMagnets(url)
        for magTag in magTags:
            imgFileName = downloadMagnet(magTag)
            #if imgFileName != '':
            #    testForExif(imgFileName)
if __name__ == '__main__':
    main()

