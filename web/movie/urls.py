from django.urls import path
from . import views

urlpatterns = [
    path('', views.movieList, name = 'Movie List'),
    path('detail/<int:loc>/', views.movieInfo, name = 'Movie Info'),
    path('actor/', views.actorList, name = 'Actor List'),
    path('actor/<int:loc>/', views.actorInfo, name = 'Actor Info'),
    path('search/', views.search, name = 'Search'),
    path('result/', views.result, name = 'Result')
]