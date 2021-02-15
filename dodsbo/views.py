from django.shortcuts import render    # Hjelper med å laste inn HTML filer
from django.http import HttpResponse

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
        BESKRIVELSE: " Dette er en beskrivelse av en maleri.",
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
        'assets': assets
    }
    return render(request, 'dodsbo/home.html', context)


def info(request):    # Denne funksjonen returnerer info siden
    return render(request, 'dodsbo/info.html', {"title": "info"})
