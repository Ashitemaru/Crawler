# -*- coding: utf-8 -*-

from urllib.request import Request, urlopen
from html.parser import HTMLParser
import ssl
import json
import time

ssl._create_default_https_context = ssl._create_unverified_context

def fetchActor(url: str):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    }
    with urlopen(Request(url = url, headers = header)) as f:
        data = f.read()
        if f.status == 403:
            return ''
        else:
            return data.decode('utf-8')

def main():
    urlFile = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/actorUrl.txt', 'r')
    actorList = urlFile.readlines()

    print(len(actorList))

    for i in range(len(actorList)):
        if i < 7915:
            continue

        infoList = actorList[i].strip().split('*')
        actorFile = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/actorData/' + infoList[0] + '.html', 'w')

        print('Processing', i, infoList[0])

        htmlStr = fetchActor('https://movie.douban.com' + infoList[1])
        if htmlStr == '':
            print('IP banned')
            break

        actorFile.write(htmlStr)
        actorFile.close()

        if len(htmlStr) < 10000:
            print('IP banned')
            break
        
        print('Get length: ', len(htmlStr))
        # time.sleep(5)
    
if __name__ == '__main__':
    main()