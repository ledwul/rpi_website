from django.shortcuts import render
from django.http import HttpResponse
from django.utils.dateformat import format

from .forms import *

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TimeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                f = open("/home/pi/wakeuptime.txt", "w+")
                time = form.cleaned_data['time']
                f.write(str(format(time, 'U')))
                f.close()
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponse("Set timer to " + str(form.cleaned_data['time']))
            except TypeError as e:
                
                return HttpResponse("Your input " + str(form.cleaned_data['time']) + " is not a valid time: <br>" + str(e))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TimeForm()
    return render(request, 'wakeuptime/index.html', {'timeform' : form})

def set(request):
    
    return HttpResponse("You entered " + str(request.time))

# Create your views here.
