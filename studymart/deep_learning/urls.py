from django.urls import path
from . import views

urlpatterns=[
    path('deep',views.deep_learning),
]