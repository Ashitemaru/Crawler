# -*- coding: utf-8 -*-

import os
from html.parser import HTMLParser
from json import loads

class movie(object):
    def __init__(self, name, picUrl, rate):
        self.name = name
        self.picUrl = picUrl
        self.rate = rate
        self.actorList = []
        self.abstract = ''

    def addActor(self, m: str):
        self.actorList.append(m)

    def set(self, s: str):
        self.absract = s

class actor(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.movieList = []
    
    def addMovie(self, m: str):
        self.movieList.append(m)

actorList = []
movieList = []

def insertNewActor(n: actor, name: str):
    for i in range(len(actorList)):
        if actorList[i].name == n.name:
            actorList[i].movieList.append(name)
            return
    actorList.append(n)
    actorList[len(actorList) - 1].movieList.append(name)

class movieParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.nowTag = None
        self.nowAttr = None

    def handle_starttag(self, tag, attrs):
        self.nowTag = tag
        self.nowAttr = attrs

    def handle_data(self, data):
        if self.nowTag == 'script' and self.nowAttr == [('type', 'application/ld+json')]:
            basicInfo = loads(data.replace(' ', '').replace('\r', '').replace('\n', ''))

            nowActorList = basicInfo['actor']
            nowMovie = movie(basicInfo['name'], basicInfo['image'], basicInfo['aggregateRating']['ratingValue'])

            counter = 0
            for x in nowActorList:
                counter += 1
                nowActor = actor(x['name'], x['url'])
                insertNewActor(nowActor, basicInfo['name'])

                nowMovie.addActor(x['name'])
                if counter >= 10:
                    break

            
            movieList.append(nowMovie)

            self.nowTag = None
            self.nowAttr = None

        if self.nowTag == 'span' and self.nowAttr == [('property', 'v:summary'), ('class', '')]:
            movieList[len(movieList) - 1].abstract = data.strip()

            self.nowTag = None
            self.nowAttr = None

        if self.nowTag == 'span' and self.nowAttr == [('class', 'all hidden')]:
            movieList[len(movieList) - 1].abstract = data.strip()

            self.nowTag = None
            self.nowAttr = None

def main():
    fileList = os.listdir('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/database')

    # Actor of Movies
    # Extract the url of actors & deduplication
    for i, x in enumerate(fileList):
        if os.path.splitext(x)[1] == '.html':
            print('Now process: ', i, 'Name is: ', x)

            nowStr = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/database/' + x).read()
            parser = movieParser()
            parser.feed(nowStr)
            parser.close()

    actorUrlFile = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/actorUrl.txt', 'w')
    movieFile = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/movie.txt', 'w')

    for x in actorList:

        actorUrlFile.write(x.name.replace('&#39;', '\'') + '*' + x.url)
        for m in x.movieList:
            actorUrlFile.write('*' + m)
        actorUrlFile.write('\n')

    for x in movieList:

        movieFile.write(x.name + '*' + x.abstract + '*' + x.picUrl + '*' + x.rate)
        for a in x.actorList:
            movieFile.write('*' + a)
        movieFile.write('\n')

    actorUrlFile.close()
    

if __name__ == '__main__':
    main()