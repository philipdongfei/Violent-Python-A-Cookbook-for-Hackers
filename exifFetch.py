import urllib3
import optparse
#import requests
from urllib.parse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS
def findImages(url):
    print('[+] Finding images on ' + url)
    http = urllib3.PoolManager()
    urlContent = http.request('GET', url)
    #urlContent = urllib3.urlopen(url).read()
   # soup = BeautifulSoup(urlContent.data.decode('utf-8'), 'html.parser')
    soup = BeautifulSoup(urlContent.data, "html.parser")
    imgTags = soup.findAll('img')
    return imgTags
def downloadImage(imgTag):
    try:
        print('[+] Downloading image...')
        imgSrc = imgTag['src']
        #print('imgSrc: ' + imgSrc)
        http = urllib3.PoolManager()
        imgContent = http.request('GET', imgSrc)
        #imgContent = urllib3.urlopen(imgSrc).read()
        imgFileName = basename(urlsplit(imgSrc)[2])
        #print('imgFileName: ' + imgFileName)
        if imgFileName.find(".jpg") != -1:
            imgFile = open(imgFileName, 'wb')
            imgFile.write(imgContent.data)
            imgFile.close()
            return imgFileName
        else:
            return ''
    except:
        return ''
def testForExif(imgFileName):
    try:
        print("imgFileName: " + imgFileName)
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()

        if info:
            for (tag, value) in info.items():
                #print("tag: " + tag + " value: " + value)
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
            exifGPS = exifData['GPSInfo']
            if exifGPS:
                print('[*] ' + imgFileName +\
                    ' contains GPS MetaData')
    except:
        #print('testForExif error')
        pass
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
        imgTags = findImages(url)
        for imgTag in imgTags:
            imgFileName = downloadImage(imgTag)
            if imgFileName != '':
                testForExif(imgFileName)
if __name__ == '__main__':
    main()


