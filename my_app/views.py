from django.shortcuts import render

from django.http import HttpResponse

class Bug:
    def __init__(self, commonName, species, description, lifespan):
        self.name = commonName 
        self.species = species
        self.description = description
        self.lifespan = lifespan 

bugs = [
    Bug('June Bug', 'Cotinis nitida', 'Shiny, green beetle', 3),
    Bug('Praying Mantis', 'Mantis religiosa', 'Triangular head with large eyes; long, pointed arms',1),
    Bug('Jumping Spider', 'Salticidae', 'Small, fuzzy, adorable; loves to dance', 2),
    Bug('Dragonfly', 'Anisoptera', 'Long body with large eyes; high aspect ratio wings', 1),
]

# Create your views here.
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello World!</h1>')

def about(request): 
    return render(request, 'about.html')

def bug_index(request):
    return render(request, 'bugs/index.html', {'bugs': bugs })