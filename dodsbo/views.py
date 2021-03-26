from django.shortcuts import render    # Hjelper med å laste inn HTML filer
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Estate
from .models import Item
from .models import Comment
from .models import Wish
from .models import Participate


def home(request):    # Denne funksjonen returnerer hjemmesiden
    context = {
        # gjenstand funker som nøkkel til kodeblokken i home.html
        'assets': Item.objects.all()
    }
    return render(request, 'dodsbo/home.html', context)


class EstateListView(ListView):
    template_name = 'dodsbo/estates.html'
    model = Estate

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estates'] = Estate.objects.all()
        return context


class EstateDetailView(DetailView):
    template_name = 'dodsbo/estate.html'
    model = Estate

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Items'] = Item.objects.filter(estateID=self.object)
        return context
