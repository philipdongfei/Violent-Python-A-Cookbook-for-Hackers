import mechanize
def testProxy(url, proxy):
    browser = mechanize.Browser()
    browser.set_proxies(proxy)
    page = browser.open(url)
    source_code = page.read()
    print(source_code)
url = 'http://ip.nefsc.noaa.gov/'
#hideMeProxy = {'http': '216.155.139.115:3128'}
hideMeProxy = {'http': '127.0.0.1:35817'} #lantern
testProxy(url, hideMeProxy)

