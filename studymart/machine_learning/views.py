from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine_learning(req):
    return HttpResponse("<h1>StudyMart is offering lots of free and paid courses</h1>")

def deep_learning(req):
    return HttpResponse("<h1>We are also offering Deep Learnig Course</h1>")

def about_us(req):
    return HttpResponse("<h1>We are one of the best online platform</h1>")
