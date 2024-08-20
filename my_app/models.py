from django.db import models
from django.urls import reverse 

# Create your models here.

TIME = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening'),
    ('N', 'Night')
)

class Bug(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    lifespan = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('bug-detail', kwargs={'bug_id': self.id})
    

class Sighting(models.Model):
    date = models.DateField('Sighting Date')
    time = models.CharField(
        max_length=1, 
        choices=TIME, 
        default=TIME[0][0]
    )

    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"