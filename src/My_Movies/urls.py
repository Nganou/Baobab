from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = patterns('',
    # This is the homepage url settings
    url(r'^$', 'My_Movies.views.home', name='home'),
    
    url(r'^addmovie', 'addmovies.views.addmovie', name='addmovie'),
    # url(r'^blog/', include('blog.urls')),
    
    #This is the url to sign up to the website
    url(r'^signup/', 'signups.views.signup', name='signup'),
    
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    
    #add the static urls specified in the settings.py
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    
    #add the media urls specified in the settings.py
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)