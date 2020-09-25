from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hello python")


def help(request):
    return HttpResponse("testing")
