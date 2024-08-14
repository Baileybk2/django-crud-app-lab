from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello World!</h1>')

def about(request): 
    return HttpResponse("<h1>About A Bug's Life</h1>")