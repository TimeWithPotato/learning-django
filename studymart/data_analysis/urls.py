from django.urls import path
from . import views

urlpatterns=[
    path('analysis/',views.data_analysis),
]