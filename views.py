from django.shortcuts import render
from warehouse import models


# Create your views here.
def index(request):
    articles = models.Notes.objects.all()
    kwargs = {
        "articles": articles
    }
    return render(request, 'front/index.html', kwargs)


def not_found(request):
    return render(request, 'front/404.html')


def blank(request):
    return render(request, 'front/blank.html')


def buttons(request):
    return render(request, 'front/buttons.html')


def cards(request):
    return render(request, 'front/cards.html')


def charts(request):
    return render(request, 'front/charts.html')


def forget_pwd(request):
    return render(request, 'front/forgot-password.html')


def login(request):
    return render(request, 'front/login.html')


def register(request):
    return render(request, 'front/register.html')


def tables(request):
    return render(request, 'front/tables.html')


def animation(request):
    return render(request, 'front/utilities-animation.html')


def border(request):
    return render(request, 'front/utilities-border.html')


def color(request):
    return render(request, 'front/utilities-color.html')


def other(request):
    return render(request, 'front/utilities-other.html')
