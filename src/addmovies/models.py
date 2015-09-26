#Serge Nganou 

from django.db import models
from django.core.validators import URLValidator
from django.utils.encoding import smart_unicode

# Create your models here.
# Similar to creating class in OOP.
# This contains Movie models and will now allow duplicate values

class AddMovie(models.Model):
    title = models.CharField(max_length=120, null=True, blank=False)
    storyline = models.CharField(max_length=300, null=True, blank=True)
    poster_image_url = models.CharField(max_length=300, validators=[URLValidator()], null=True, blank=True)
    trailer_youtube_url = models.CharField(max_length=300, validators=[URLValidator()], null=True, blank=True)
    release_date = models.BigIntegerField(null=True, blank = False)
    genres = models.CharField(max_length=120, null=True, blank=True)
    runtime = models.CharField(max_length=120, null=True, blank=True)
    rating = models.CharField(max_length=3, null=True, blank=True)
    mini_image = models.CharField(max_length=120, validators=[URLValidator()], null=True, blank=True)
    class Meta:
        unique_together = ["title", "release_date"]

# This allows ours to represent each model by it's attributes.
# if you visite http://127.0.0.1:8000/admin, and click on Add movies, you will notice
# each movies is repesented by title (year)

    def __unicode__(self):
        return smart_unicode(self.title + " (" + str(self.release_date) + ")") 

