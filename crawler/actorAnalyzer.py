# -*- coding: utf-8 -*-

import os
from html.parser import HTMLParser
from json import loads

class actor(object):
    def __init__(self, name):
        self.name = name
        self.abstract = ''
        self.picUrl = ''
        self.cooperator = []

actorList = []

file = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/actorUrl.txt')

actors = file.readlines()
actors = actors[1: ]
map(lambda s: s.split('##########'), actors)

def addCooperate(ina, jna):
    i = 0
    j = 0
    for ind in range(len(actorList)):
        if actorList[ind].name == ina:
            i = ind
            break

    for ind in range(len(actorList)):
        if actorList[ind].name == jna:
            j = ind
            break

    findJ = False
    for x in actorList[i].cooperator:
        if x[0] == jna:
            x[1] += 1
            findJ = True
            break

    if not findJ:
        actorList[i].cooperator.append([jna, 0])

    findI = False
    for x in actorList[j].cooperator:
        if x[0] == ina:
            x[1] += 1
            findI = True
            break

    if not findI:
        actorList[j].cooperator.append([ina, 0])

def setCooperation(i: int, j: int):
    if i == j:
        return
    
    for ind in range(len(actors[i]) - 2):
        if actors[i][ind + 2] in actors[j]:
            addCooperate(actors[i][0], actors[j][0])

class actorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.nowTag = None
        self.nowAttr = None
        self.hasGetName = False

    def handle_starttag(self, tag, attrs):
        if tag != 'br':
            self.nowTag = tag
            self.nowAttr = attrs
    
    def handle_endtag(self, tag):
        if tag != 'br':
            self.nowTag = None
            self.nowAttr = None

    def handle_data(self, data):
        if self.nowTag == 'h1':
            actorList.append(actor(data))
            self.hasGetName = True

        if self.nowTag == 'div' and self.nowAttr == [('class', 'bd')] and self.hasGetName:
            if actorList[len(actorList) - 1].abstract != '':
                actorList[len(actorList) - 1].abstract += '\n'
            actorList[len(actorList) - 1].abstract += data.strip().replace('\r', '').replace('\n', '')

        if self.nowTag == 'img' and ('title', '点击看大图') in self.nowAttr and self.hasGetName:
            actorList[len(actorList) - 1].picUrl = self.nowAttr[2][1]

        if self.nowTag == 'span' and self.nowAttr == [('class', 'all hidden')] and self.hasGetName:
            if actorList[len(actorList) - 1].abstract != '':
                actorList[len(actorList) - 1].abstract += '\n'
            actorList[len(actorList) - 1].abstract += data.strip().replace('\r', '').replace('\n', '')



def main():
    fileList = os.listdir('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/actorData')

    for i, x in enumerate(fileList):
        if os.path.splitext(x)[1] == '.html':
            print('Now process: ', i, 'Name is: ', x)

            nowStr = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/actorData/' + x).read()
            actorParser().feed(nowStr)
    '''
    for i in range(len(actors)):
        for j in range(len(actors)):
            if i > j:
                print(i, j)
                setCooperation(i, j)
    '''

    actorFile = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/actorDetail.txt', 'w')
    actorFile.write('name,absract,picUrl,cooperator\n')
    for x in actorList:
        actorFile.write(x.name.strip().replace('\r', '').replace('\n', '').replace(' ', '') + '##########' + x.abstract.strip().replace('\r', '').replace('\n', '') + '##########' + x.picUrl.strip().replace('\r', '').replace('\n', ''))
        '''
        for a in x.cooperator:
            actorFile.write(a[0].strip().replace('\r', '').replace('\n', '') + '##########' + a[1])
        '''
        actorFile.write('\n')

    actorFile.close()

if __name__ == '__main__':
    main()