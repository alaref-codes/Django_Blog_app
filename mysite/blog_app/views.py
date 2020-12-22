from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Alaref',
        'title' : 'Fiminism',
        'content' : 'This is widest door for athiesm',
        'published' : 'September 18, 2018',
    },
    {
        'author' : 'Mohammed',
        'title' : 'Flat Earth',
        'content' : 'This is Tightest door for athiesm',
        'published' : 'August 34, 2020',
    },

]

def home(request):
    context = {
        'posts' : posts,
    }
    return render(request, 'blog_app/home.html',context)

def about(request):
    return render(request, 'blog_app/about.html', {'title':'About'})
