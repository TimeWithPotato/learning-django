from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def about_us(req):
    return HttpResponse("<h1>This is about us platform</h1>")
