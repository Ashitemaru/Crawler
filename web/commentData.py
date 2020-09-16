# -*- coding: utf-8 -*-

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movieSite.settings")

from movie import models
import django

if django.VERSION >= (1, 7):
    django.setup()

def main():
    commentFile = open('/Users/ashitemaru/Downloads/CodingFolder/FreshmanSummer/movies/crawler/movieComment.txt')
    commentList = commentFile.readlines()
    for x in commentList:
        info = x.split('##########')
        belongTo = models.movieSlice.objects.filter(name = info[0])[0]

        for i in range(len(info) - 2):
            models.comment.objects.create(
                content = info[i + 2],
                movie = belongTo
            )

    commentFile.close()

if __name__ == '__main__':
    main()