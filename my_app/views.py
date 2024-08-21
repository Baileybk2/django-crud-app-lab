from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bug
from .forms import SightingForm


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def about(request): 
    return render(request, 'about.html')

@login_required
def bug_index(request):
    bugs = Bug.objects.filter(user=request.user)
    return render(request, 'bugs/index.html', {'bugs': bugs })

@login_required
def bug_detail(request, bug_id):
    bug = Bug.objects.get(id=bug_id)
    sighting_form = SightingForm()
    return render(request, 'bugs/detail.html', {'bug': bug, 'sighting_form': sighting_form})

class BugCreate(LoginRequiredMixin, CreateView):
    model = Bug
    fields = ['name', 'species', 'description', 'lifespan']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BugUpdate(LoginRequiredMixin, UpdateView):
    model = Bug
    fields = ['species', 'description', 'lifespan']

class BugDelete(LoginRequiredMixin, DeleteView):
    model = Bug
    success_url = '/bugs/'

@login_required
def add_sighting(request, bug_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.bug_id = bug_id
        new_sighting.save()
    return redirect('bug-detail', bug_id=bug_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('bug-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
