# -*- coding: utf-8 -*-

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movieSite.settings")

from movie import models
import django

if django.VERSION >= (1, 7):
    django.setup()

def main():
    file = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/movie.txt')
    movieList = file.readlines()
    for x in movieList:
        info = x.split('*')
        models.movieSlice.objects.create(
            name = info[0],
            abstract = info[1],
            picUrl = info[2]
        )
    file.close()

if __name__ == '__main__':
    main()