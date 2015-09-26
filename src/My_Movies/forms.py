# This contains the homepage form 

from django import forms
from addmovies.models import AddMovie

class HomePageForm(forms.ModelForm):
    class Meta:
        model = AddMovie
        
    def add_movie_dict(self):
        moviedata = { "movie": []}
    
        for i in AddMovie.objects.raw('SELECT * FROM addmovies_addmovie'):
            mov = {}
            mov["title"]= i.title
            mov["storyline"]= i.storyline
            mov["poster_image_url"]= i.poster_image_url
            mov["trailer_youtube_url"]=i.trailer_youtube_url
            moviedata["movie"].append(mov)          
# Debug            
#           print moviedata
#           print " "
        return moviedata


