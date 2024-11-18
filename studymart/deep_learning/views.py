from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def deep_learning(req):
    return HttpResponse("<h1>This is deep learning platform</h1>")