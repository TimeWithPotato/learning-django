from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine_learning(req):
    course = 'Machine Learning'
    duration = '2.5hr'
    fees = 1200
    algorithm = ['random forest','knn','decision tree']
    offering = {
        'course': course,
        'duration': duration,
        'fees':fees,
        'algorithms' : algorithm,
        'updated_course' : True, 
    }
    return render(req,'machine_learning/machine_learning.html',context=offering)

def random_forest(req):
    algorithm = 'Machine Learning Algorithm, random forest'
    duration = '1hr'
    fees = 1000

    details = {
        'algorithm' : algorithm,
        'duration' : duration,
        'fees': fees,
    }
    return render(req,'machine_learning/random_forest.html',context = details)

def decision_tree(req):
    return render(req,'machine_learning/decision_tree.html')

def knn(req):
    return render(req,'machine_learning/knn.html')

def nearest_neighbour(req):
    return render(req,'machine_learning/nearest_neighbour.html')
# def deep_learning(req):
#     return HttpResponse("<h1>We are also offering Deep Learnig Course</h1>")

# def about_us(req):
#     return HttpResponse("<h1>We are one of the best online platform</h1>")
