from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bugs/', views.bug_index, name='bug-index'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug-detail'),
    path('bugs/create/', views.BugCreate.as_view(), name='bug-create'),
    path('bugs/<int:pk>/update/', views.BugUpdate.as_view(), name='bug-update'),
    path('bugs/<int:pk>/delete/', views.BugDelete.as_view(), name='bug-delete'),
    path(
        'bugs/<int:bug_id>/add-sighting/', 
        views.add_sighting, 
        name='add-sighting'
    ),
]