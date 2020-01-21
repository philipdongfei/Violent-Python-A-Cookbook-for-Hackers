import sqlite3
def printDownloads(downloadDB):
    conn = sqlite3.connect(downloadDB)
    c = conn.cursor()
    c.execute('SELECT name, source, datetime(endTime/1000000,\
        \'unixepoch\') FROM moz_downloads;')
    print('\n[*] --- Files Downloaded ---')
    for row in c:
        print('[+] File: ' + str(row[0]) + ' from source: '\
            + str(row[1]) + ' at: ' + str(row[2]))

def main():
    parser = optparse.OptionParser("usage%prog "+\
        " -p <firefox profile path>")
    parser.add_option('-p', dest='pathName', type='string',\
        help='specify firefox profile path')
    (options, args) = parser.parse_args()
    pathName = options.pathName
    if pathName == None:
        print(parser.usage)
        exit(0)
    else:
        printDownloads(pathName)

if __name__ == "__main__":
    main()

