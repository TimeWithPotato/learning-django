from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def data_analysis(req):
    return HttpResponse("<h1>This data analysis platform</h1>")