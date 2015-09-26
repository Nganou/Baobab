# Register your movie models here.
# In this segment, we create, instantiate it, and register our add movie model
# By importing the admin model, it allowes ours to use http://127.0.0.1:8000/admin to store data

from django.contrib import admin
from addmovies.models import AddMovie

class AddMovieAdmin(admin.ModelAdmin):
    class Meta:
        model = AddMovie
        
admin.site.register(AddMovie, AddMovieAdmin)