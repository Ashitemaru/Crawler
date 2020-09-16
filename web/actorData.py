# -*- coding: utf-8 -*-

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movieSite.settings")

from movie import models
import django

if django.VERSION >= (1, 7):
    django.setup()

def main():
    actorFile = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/actorDetail.txt')
    actorList = actorFile.readlines()
    for x in actorList:
        info = x.split('##########')
        models.actor.objects.create(
            name = info[0],
            abstract = info[1],
            picUrl = info[2]
        )

    actorFile.close()

    bindFile = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/actorUrl.txt')
    bindList = bindFile.readlines()
    for x in bindList:
        info = x.split('*')
        nowActor = models.actor.objects.filter(name = info[0].strip())

        if len(nowActor) == 0:
            print(info[0].strip())
            continue

        for i in range(len(info) - 2):
            
            nowMovie = models.movieSlice.objects.filter(name = info[i + 2].strip())

            if len(nowMovie) == 0:
                print(info[0].strip() + info[i + 2].strip())
                continue

            models.connect.objects.create(
                actorId = nowActor[0].id,
                movieId = nowMovie[0].id
            )

if __name__ == '__main__':
    main()