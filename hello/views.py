from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello Django</h1>")

def test(request):
    return HttpResponse("test")
