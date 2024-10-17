from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Miyuks',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 20, 2024'
    },
    {
        'author': 'Airah Sophia',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 26, 2024'
    },
    {
        'author': 'Jaci Mae Diaz',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'September 29, 2024'
    }

]

def home(request):
    context = {
        'posts': posts
    }
    #return HttpResponse('<h1> WELCOME </h1>')
    return render(request, 'javathread/home.html', context)

def about(request):
    #return HttpResponse('<h1> ABOUT </h1>')
    return render(request, 'javathread/about.html')