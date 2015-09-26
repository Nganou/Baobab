# This contains the Movie form
# This is what django uses to auto generate html text fields based on the db model.

from django import forms

from addmovies.models import AddMovie
from pattern import web
import requests
import json

class AddMovieForm(forms.ModelForm):
    class Meta:
        model = AddMovie
    
        imdb_url = 'http://www.omdbapi.com/?'
        
        srch_mov = {}
        for i in AddMovie.objects.raw('select * from addmovies_addmovie where id = (select max(id) from addmovies_addmovie)'):
            srch_mov["title"] = i.title
            srch_mov["release_date"] = str(i.release_date)
            srch_mov["storyline"] = i.storyline
            srch_mov["poster_image_url"] = i.poster_image_url
            srch_mov["id"] = i.id
            
        if srch_mov["storyline"] == "" and srch_mov["poster_image_url"] == "":     
            param = dict(t=srch_mov["title"] ,start=1,y=srch_mov["release_date"], plot='short', r='json')
            r = requests.get(imdb_url, params=param)
            json_file = json.loads(r.content)
            
            #json_file["Poster"]= "http://" + json_file["Poster"]
            x = json_file["Poster"]
            json_file["Poster"] = x.replace(x[:7], '')
            #Debug
            #print json_file["Title"],json_file["Plot"], json_file["Poster"] , " " ,json_file["Year"], json_file["Genre"] , json_file["Runtime"], json_file["imdbRating"], " "
            
            new_movie = AddMovie(srch_mov["id"],json_file["Title"],json_file["Plot"], json_file["Poster"] , " " ,
                                 json_file["Year"], json_file["Genre"] , json_file["Runtime"], json_file["imdbRating"], " ")
            #new_movie.save()
    
