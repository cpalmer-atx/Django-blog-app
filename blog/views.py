from django.shortcuts import render
from django.http import HttpResponse


# What we want the user to see when they are sent to this route
# This is the logic for how we want to handle when a user goes to the blog page

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date': 'August 27, 2018'
    },

    {
        'author': 'Chad',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date': 'August 28, 2018'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})