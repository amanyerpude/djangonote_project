from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {
        'posts': Post.objects.filter(author=request.user)
    }
    return render(request, 'note/home.html', context)


def about(request):
    return render(request, 'note/about.html', {'title': 'About'})
