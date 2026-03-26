from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

def index(request):
    template = loader.get_template('index.html')
    context = {
        'x': 10,
        'str': 'the string'
    }
    return HttpResponse(template.render(context, request))