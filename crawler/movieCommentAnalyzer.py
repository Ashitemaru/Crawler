# -*- coding: utf-8 -*-

import os
from html.parser import HTMLParser
from json import loads

class movie(object):
    def __init__(self, name):
        self.name = name
        self.abstract = ''
        self.comment = []

movieList = []

class movieParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.nowTag = None
        self.nowAttrs = None

    def handle_starttag(self, tag, attrs):
        if tag != 'br':
            self.nowTag = tag
            self.nowAttrs = attrs

    def handle_endtag(self, tag):
        if tag != 'br':
            self.nowTag = None
            self.nowAttrs = None

    def handle_data(self, data):
        if self.nowTag == 'script' and self.nowAttrs == [('type', 'application/ld+json')]:
            basicInfo = loads(data.replace(' ', '').replace('\r', '').replace('\n', ''))
            movieList.append(movie(basicInfo['name']))

        if self.nowTag == 'span' and self.nowAttrs == [('property', 'v:summary'), ('class', '')]:
            if movieList[len(movieList) - 1].abstract != '':
                movieList[len(movieList) - 1].abstract += '\n'
            movieList[len(movieList) - 1].abstract += data.strip().replace('\r', '').replace('\n', '')

        if self.nowTag == 'span' and self.nowAttrs == [('class', 'short')]:
            if len(movieList[len(movieList) - 1].comment) > 5:
                return
            movieList[len(movieList) - 1].comment.append(data.strip().replace('\r', '').replace('\n', ''))

def main():
    fileList = os.listdir('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/database')

    for i, x in enumerate(fileList):
        if os.path.splitext(x)[1] == '.html':
            print('Now process: ', i, 'Name is: ', x)

            nowStr = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/database/' + x).read()
            movieParser().feed(nowStr)

    movieFile = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/movieComment.txt', 'w')
    movieFile.write('name,absract,comments\n')

    print(len(movieList))

    for x in movieList:
    
        movieFile.write(x.name.strip().replace('\r', '').replace('\n', '') + '##########' + x.abstract.strip().replace('\r', '').replace('\n', ''))
        for a in x.comment:
            movieFile.write('##########' + a.strip().replace('\r', '').replace('\n', '') )
        movieFile.write('\n')

    movieFile.close()

if __name__ == '__main__':
    main()