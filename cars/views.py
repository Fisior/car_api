from django.shortcuts import render, HttpResponse

from .models import Car
from .serializers import CarSerializer


def index(request):
    return HttpResponse("Hello World")
