from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def about_us(req):
    return render(req,'about_us/about_us.html')
