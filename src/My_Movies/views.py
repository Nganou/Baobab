# Create your Home page views here.
# In this view, we will dynamically generate the movies entered in the database.
# Please make sure that the title and release date are valid, but also
# ensure that both the poster image URL and youtube trailer video are valid. 

from django.shortcuts import render, render_to_response, RequestContext
from django.db.models.query import RawQuerySet

from My_Movies.forms import HomePageForm
from My_Movies.fresh_tomatoes import open_movies_page

from addmovies.models import AddMovie

def home(request):
    
    form = HomePageForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    
    movies = form.add_movie_dict()
    
    open_movies_page()
    
    return render_to_response('fresh_tomatoes.html',
                              locals(),
                              context_instance=RequestContext(request))