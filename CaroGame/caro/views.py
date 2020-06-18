# caro/views.py

from django.http import HttpResponse
from django.shortcuts import render
from . import caro

# Create your views here.

# Create caro game
caro = caro.Caro()

# Main page
def index(request):
    return render(request, "caro/index.html")