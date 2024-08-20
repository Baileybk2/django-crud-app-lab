from django.contrib import admin
from .models import Bug, Sighting

admin.site.register(Bug)
# Register your models here.
admin.site.register(Sighting)