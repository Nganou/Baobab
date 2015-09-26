# Create your signup views here.

from django.shortcuts import render, render_to_response, RequestContext

from signups.forms import SignUpForm
from django.contrib import messages

def signup(request):
    
    form = SignUpForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.SUCCESS(request, 'Welcome!')
    return render_to_response('signup.html',
                              locals(),
                              context_instance=RequestContext(request))