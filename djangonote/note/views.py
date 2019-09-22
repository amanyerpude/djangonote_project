from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.filter(author=request.user)
    }
    return render(request, 'note/home.html', context)


def about(request):
    return render(request, 'note/about.html', {'title': 'About'})
