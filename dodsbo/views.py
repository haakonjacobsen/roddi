from django.shortcuts import render    # Hjelper med å laste inn HTML filer
from django.http import HttpResponse
from .models import Estate
from .models import Item
from .models import Comment
from .models import Wish
from .models import Participate

TITTEL = "title"
VALUE = "value"
BESKRIVELSE = "description"
FORDEL = "share"
DONATE = "donate"
DISCARD = "discard"

assets = [
    {
        TITTEL: 'Stol',
        VALUE: 50,
        BESKRIVELSE: " Dette er en beskrivelse av en stol.",
        "votes": {
            FORDEL: 1,
            DONATE: 1,
            DISCARD: 2
        }
    },
    {
        TITTEL: 'Bord',
        VALUE: 150,
        BESKRIVELSE: " Dette er en beskrivelse av en bord.",
        "votes": {
            FORDEL: 1,
            DONATE: 3,
            DISCARD: 0
        }
    },
    {
        TITTEL: 'Bil',
        VALUE: 50,
        BESKRIVELSE: " Dette er en beskrivelse av en bil.",
        "votes": {
            FORDEL: 0,
            DONATE: 1,
            DISCARD: 2
        }
    },
    {
        TITTEL: 'Maleri',
        VALUE: 50,
        BESKRIVELSE: " Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32.",
        "votes": {
            FORDEL: 0,
            DONATE: 1,
            DISCARD: 1
        }
    }
]


def home(request):    # Denne funksjonen returnerer hjemmesiden
    context = {
        # gjenstand funker som nøkkel til kodeblokken i home.html
        'assets': Item.objects.all()
    }
    return render(request, 'dodsbo/home.html', context)


def info(request):    # Denne funksjonen returnerer info siden
    return render(request, 'dodsbo/info.html', {"title": "info"})
