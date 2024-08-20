from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Bug
from .forms import SightingForm



# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def about(request): 
    return render(request, 'about.html')

def bug_index(request):
    bugs = Bug.objects.all()
    return render(request, 'bugs/index.html', {'bugs': bugs })

def bug_detail(request, bug_id):
    bug = Bug.objects.get(id=bug_id)
    sighting_form = SightingForm()
    return render(request, 'bugs/detail.html', {'bug': bug, 'sighting_form': sighting_form})

class BugCreate(CreateView):
    model = Bug
    fields = '__all__'
    success_url = '/bugs/'

class BugUpdate(UpdateView):
    model = Bug
    fields = ['species', 'description', 'lifespan']

class BugDelete(DeleteView):
    model = Bug
    success_url = '/bugs/'

def add_sighting(request, bug_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.bug_id = bug_id
        new_sighting.save()
    return redirect('bug-detail', bug_id=bug_id)