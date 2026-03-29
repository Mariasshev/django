from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

def hello(request):
    return HttpResponse("Hello World!")

def index(request):
    template = loader.get_template('index.html')
    context = {
        'x': 10,
        'str': 'the string'
    }
    return HttpResponse(template.render(context, request))

def intro(request):
    now = datetime.now()
    timestamp = now.strftime("%H:%M %d.%m.%Y")
    context = {
        'load_time': timestamp
    }
    template = loader.get_template('intro.html')
    return HttpResponse(template.render(context,request))

def privacy(request):
    template = loader.get_template('privacy.html')
    return HttpResponse(template.render({}, request))