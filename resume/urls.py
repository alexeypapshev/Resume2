from django.urls import path 
from . import views 
  
urlpatterns = [ 
    path("", views.home, name="home"), 
    path("projects/", views.projects, name="projects"), 
    path("blog/", views.blog, name="blog"),
    path("texet/", views.texet, name="texet"),
]
