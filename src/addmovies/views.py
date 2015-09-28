# Serge Nganou
# Create your movie views here.
# This is where the request (POST or GET) get interpretted
# Also when a user tres to enter a movie with title and year, this will
# add the poster image, plot, runtime, and imdb rating.

from django.shortcuts import render, render_to_response, RequestContext

from addmovies.forms import AddMovieForm
from addmovies.models import AddMovie
from django.contrib import messages
from pattern import web
import requests
import json


# Create your views here.

def addmovie(request):
    form = AddMovieForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        #messages.SUCCESS(request, 'Movie added')
        imdb_url = 'http://www.omdbapi.com/?'
        
        srch_mov = {}
        for i in AddMovie.objects.raw('select * from addmovies_addmovie where id = (select max(id) from addmovies_addmovie)'):
            srch_mov["title"] = i.title
            srch_mov["release_date"] = str(i.release_date)
            srch_mov["storyline"] = i.storyline
            srch_mov["poster_image_url"] = i.poster_image_url
            srch_mov["id"] = i.id
            
        if srch_mov["storyline"] == "" and srch_mov["poster_image_url"] == "":     
            param = dict(t=srch_mov["title"] ,start=1,y=srch_mov["release_date"], plot='short', r='json', apikey='cb300224')
            r = requests.get(imdb_url, params=param)
            json_file = json.loads(r.content)
            
            #Debug
            #print json_file["Title"],json_file["Plot"], json_file["Poster"] , " " ,json_file["Year"], json_file["Genre"] , json_file["Runtime"], json_file["imdbRating"], " "
            
            new_movie = AddMovie(srch_mov["id"],json_file["Title"],json_file["Plot"], json_file["Poster"] , " " ,
                                 json_file["Year"], json_file["Genre"] , json_file["Runtime"], json_file["imdbRating"], " ")
            if json_file["Response"] == True:
                new_movie.save()
            new_movie.save()
        
    return render_to_response('addmovie.html',
                              locals(),
                              context_instance=RequestContext(request))
