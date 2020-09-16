from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from . import models
from django.views.decorators.csrf import csrf_exempt
import time

# Create your views here.

def movieList(request):
    page = request.GET.get('page')
    if page:
        if int(page) > 0 and int(page) < 51:
            page = int(page)
        else:
            page = 1
    else:
        page = 1

    movieList = models.movieSlice.objects.all()
    paginator = Paginator(movieList, 20)
    moviePageList = paginator.page(page)
    pageNum = paginator.num_pages

    nextPage = 0
    if moviePageList.has_next():
        nextPage = page + 1
    else:
        nextPage = page

    prevPage = 0
    if moviePageList.has_previous():
        prevPage = page - 1
    else:
        prevPage = page

    return render(request, 'movieList.html', {
        'movieList': moviePageList,
        'pageNum': range(max(page - 2, 1), min(page + 2, paginator.num_pages + 1)),
        'nowPage': page,
        'nextPage': nextPage,
        'prevPage': prevPage,
        'len': str(len(movieList)),
        'pages': str(paginator.num_pages),
        'time': '0.000'
    })

def movieInfo(request, loc):
    chosenMovie = models.movieSlice.objects.filter(id = loc)[0]

    actorIdList = models.connect.objects.filter(movieId = loc)
    actorList = []
    for i in actorIdList:
        actorList.append({
            'actor': models.actor.objects.get(id = i.actorId),
            'url': 'http://127.0.0.1:8000/actor/' + str(i.actorId) + '/'
        })

    return render(request, 'movieDetail.html', {
        'slice': chosenMovie,
        'commentList': models.comment.objects.filter(movie = chosenMovie),
        'actorList': actorList
    })

def actorList(request):
    page = request.GET.get('page')
    if page:
        if int(page) > 323:
            page = 323
        if int(page) < 1:
            page = 1
        else:
            page = int(page)
    else:
        page = 1;

    actorList = models.actor.objects.all()
    paginator = Paginator(actorList, 20)
    actorListPage = paginator.page(page)
    pageNum = paginator.num_pages

    nextPage = 0
    if actorListPage.has_next():
        nextPage = page + 1
    else:
        nextPage = page

    prevPage = 0
    if actorListPage.has_previous():
        prevPage = page - 1
    else:
        prevPage = page

    return render(request, 'actorList.html', {
        'actorList': actorListPage,
        'pageNum': range(max(page - 2, 1), min(page + 2, 324)),
        'nowPage': page,
        'nextPage': nextPage,
        'prevPage': prevPage
    })

def actorInfo(request, loc):
    chosenActor = models.actor.objects.filter(id = loc)[0]

    movieIdList = models.connect.objects.filter(actorId = loc)
    movieList = []
    for i in movieIdList:
        movieList.append({
            'movie': models.movieSlice.objects.get(id = i.movieId),
            'url': 'http://127.0.0.1:8000/detail/' + str(i.movieId) + '/'
        })

    counter = []
    for connector in movieIdList:
        for _connector in models.connect.objects.filter(movieId = connector.movieId):
            if _connector.actorId != loc:
                hasFound = False
                for x in counter:
                    if x[0] == _connector.actorId:
                        x[1] += 1
                        hasFound = True
                if not hasFound:
                    counter.append([_connector.actorId, 1])

    counter.sort(key = lambda e: e[1], reverse = True)

    if len(counter) > 10:
        counter = counter[: 10]

    cooperator = []
    for x in counter:
        cooperator.append({
            'actor': models.actor.objects.get(id = x[0]),
            'num': str(x[1]),
            'url': 'http://127.0.0.1:8000/actor/' + str(x[0]) + '/'
        })


    return render(request, 'actorDetail.html', {
        'actor': chosenActor,
        'movieList': movieList,
        'cooperator': cooperator
    })

def search(request):
    return render(request, 'search.html', {})

@csrf_exempt
def result(request):
    begin = time.time()

    type_ = request.GET.get("type")
    keyword = request.GET.get("kw")

    if type_ == "movie":
        movieList = list(models.movieSlice.objects.filter(name__contains = keyword))

        actorList = models.actor.objects.filter(name__contains = keyword)
        for x in actorList:
            cList = models.connect.objects.filter(actorId = x.id)
            for c in cList:
                movieList.append(models.movieSlice.objects.get(id = c.movieId))

        page = request.GET.get('page')
        if page:
            if int(page) > 0 and int(page) <= len(movieList) // 20 + 1:
                page = int(page)
            else:
                page = 1
        else:
            page = 1

        paginator = Paginator(movieList, 20)
        moviePageList = paginator.page(page)
        pageNum = paginator.num_pages

        nextPage = 0
        if moviePageList.has_next():
            nextPage = page + 1
        else:
            nextPage = page

        prevPage = 0
        if moviePageList.has_previous():
            prevPage = page - 1
        else:
            prevPage = page

        end = time.time()

        return render(request, 'movieResult.html', {
            'movieList': moviePageList,
            'pageNum': range(max(page - 2, 1), min(page + 2, paginator.num_pages + 1)),
            'nowPage': page,
            'nextPage': nextPage,
            'prevPage': prevPage,
            'len': str(len(movieList)),
            'pages': str(paginator.num_pages),
            'time': str(end - begin),
            'type': type_,
            'kw': keyword
        })


    if type_ == "actor":
        actorList = list(models.actor.objects.filter(name__contains = keyword))

        movieList = models.movieSlice.objects.filter(name__contains = keyword)
        for x in movieList:
            cList = models.connect.objects.filter(movieId = x.id)
            for c in cList:
                actorList.append(models.actor.objects.get(id = c.actorId))

        page = request.GET.get('page')
        if page:
            if int(page) > 0 and int(page) <= len(actorList) // 20 + 1:
                page = int(page)
            else:
                page = 1
        else:
            page = 1

        paginator = Paginator(actorList, 20)
        actorPageList = paginator.page(page)
        pageNum = paginator.num_pages

        nextPage = 0
        if actorPageList.has_next():
            nextPage = page + 1
        else:
            nextPage = page

        prevPage = 0
        if actorPageList.has_previous():
            prevPage = page - 1
        else:
            prevPage = page

        end = time.time()

        return render(request, 'actorResult.html', {
            'actorList': actorPageList,
            'pageNum': range(max(page - 2, 1), min(page + 2, paginator.num_pages + 1)),
            'nowPage': page,
            'nextPage': nextPage,
            'prevPage': prevPage,
            'len': str(len(actorList)),
            'pages': str(paginator.num_pages),
            'time': str(end - begin),
            'type': type_,
            'kw': keyword
        })

    if type_ == "comment":
        commentList = list(models.comment.objects.filter(content__contains = keyword))

        page = request.GET.get('page')
        if page:
            if int(page) > 0 and int(page) <= len(commentList) // 20 + 1:
                page = int(page)
            else:
                page = 1
        else:
            page = 1

        paginator = Paginator(commentList, 20)
        commentPageList = paginator.page(page)
        pageNum = paginator.num_pages

        nextPage = 0
        if commentPageList.has_next():
            nextPage = page + 1
        else:
            nextPage = page

        prevPage = 0
        if commentPageList.has_previous():
            prevPage = page - 1
        else:
            prevPage = page

        end = time.time()

        return render(request, 'commentResult.html', {
            'commentList': commentPageList,
            'pageNum': range(max(page - 2, 1), min(page + 2, paginator.num_pages + 1)),
            'nowPage': page,
            'nextPage': nextPage,
            'prevPage': prevPage,
            'len': str(len(commentList)),
            'pages': str(paginator.num_pages),
            'time': str(end - begin),
            'type': type_,
            'kw': keyword
        })

    