from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog1(req):
    return render(req,'blogs/blogs.html')
