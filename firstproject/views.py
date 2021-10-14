from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("This is our first project")

def demo(request):
    return HttpResponse("Good afternoon")