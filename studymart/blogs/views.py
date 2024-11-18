from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog1(req):
    return HttpResponse("<h1>Our instructors blogs</h1>")
