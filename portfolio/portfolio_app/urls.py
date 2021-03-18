from django.urls import path     
from . import views
urlpatterns = [
    path('', views.home,name = 'home'),	   
    
    path('test', views.test, name = 'test'),	
    path('projects', views.projects, name = 'projects'), 
    path('aboutme', views.about, name = 'aboutme'),
    
]