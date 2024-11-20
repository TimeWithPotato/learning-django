from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def deep_learning(req):
    return render(req,'deep_learning/deep_learning.html')