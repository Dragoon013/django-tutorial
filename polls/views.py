from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello m8. You are at the polls now.")
