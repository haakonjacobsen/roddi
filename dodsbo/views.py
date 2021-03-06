from django.contrib.auth.models import User
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
    user_count = User.objects.count()
    estates_count = Estate.objects.count()
    items_count = Item.objects.count()
    estates_count_finished = 0
    for estates in Estate.objects.all():
        if estates.isCompleted:
            estates_count_finished += 1
    stats = [user_count, estates_count, items_count, estates_count_finished]
    context = {
        "stats": stats,
        "title": "info"
    }

    return render(request, 'dodsbo/info.html', context)



