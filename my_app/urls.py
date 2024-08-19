from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bugs/', views.bug_index, name='bug-index'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug-detail'),
]