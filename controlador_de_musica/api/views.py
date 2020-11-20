from django.shortcuts import render
from django.http import HttpResponse  # nuevo

# Create your views here.


def main(request):
    return HttpResponse("<h1>Hello</h1>")