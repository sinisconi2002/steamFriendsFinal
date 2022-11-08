from django.shortcuts import render
from django.http import *

from blog.models import Post

def homepage(request):
    context ={
        'posts_up': Post.objects.all()[:2],
        'posts_down': Post.objects.all()[2:4]
    }
    return HttpResponse(render(request, 'index.html', context))


def profile1(request):
    return HttpResponse(render(request, 'profile1.html'))


def profile2(request):
    return HttpResponse(render(request, 'profile2.html'))


def profile3(request):
    return HttpResponse(render(request, 'profile3.html'))


def profile4(request):
    return HttpResponse(render(request, 'profile4.html'))


def america(request):
    return HttpResponse(render(request, 'america.html'))


def brad(request):
    return HttpResponse(render(request, 'brad.html'))


def celebre(request):
    return HttpResponse(render(request, 'celebre.html'))

def flying_scotsman(request):
    return HttpResponse(render(request, 'flying_scotsman.html'))

def british(request):
    return HttpResponse(render(request, 'galerie_british.html'))

def intretinere(request):
    return HttpResponse(render(request, 'intretinere.html'))

def proba(request):
    return HttpResponse(render(request, 'zlatna.html'))

def romania(request):
    return HttpResponse(render(request, 'romania.html'))