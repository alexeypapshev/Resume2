from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")

def projects(request):
    return render(request, "projects.html")

def blog(request):
    return render(request, "blog.html")

def texet(request):
    return render(request, "texet.html")

