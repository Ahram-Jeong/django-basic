from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("HELLO THIS IS A VIEW INSIDE MY_APP")

def simple_view(request):
    return HttpResponse("SIMPLE VIEW")