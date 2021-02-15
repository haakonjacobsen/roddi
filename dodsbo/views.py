from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Dodsbo Home</h1>')


def info(request):
    return HttpResponse('<h1>Dodsbo</h1>')
