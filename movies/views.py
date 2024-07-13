
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Movie
from django.shortcuts import render

def index(request):
    movies = Movie.objects.order_by('name') 
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movies': movies}, request))

def movies(request, movies):
   
    movies=Movie.objects.get(id=movies)
    template = loader.get_template('display_movies.html')
    context = {
        'movies': movies
    }
    return HttpResponse(template.render(context, request))