from django.shortcuts import render    # Hjelper med å laste inn HTML filer
from django.http import HttpResponse
from .models import Estate
from .models import Item
from .models import Comment
from .models import Wish
from .models import Participate

asserts = []


def home(request):    # Denne funksjonen returnerer hjemmesiden
    context = {
        # gjenstand funker som nøkkel til kodeblokken i home.html
        'assets': Item.objects.all()
    }
    return render(request, 'dodsbo/home.html', context)


def info(request):    # Denne funksjonen returnerer info siden
    return render(request, 'dodsbo/info.html', {"title": "info"})
