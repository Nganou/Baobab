from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
# This contains the Signup Models and will not allow duplicate values


# Create your models here.
class SignUp(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=False)
    last_name = models.CharField(max_length=120, null=True, blank=False)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now = False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    class Meta:
        unique_together = ["email"]
    
    def __unicode__(self):
        return smart_unicode(self.email)