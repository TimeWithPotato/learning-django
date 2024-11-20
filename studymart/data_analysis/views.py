from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def data_analysis(req):
    return render(req,'data_analysis/data_analysis.html')