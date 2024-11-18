"""
URL configuration for studymart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# 1.
# from machine_learning import views as v1
# from blogs import views as v2
#2. another wat to import
from machine_learning.views import machine_learning as ml, deep_learning as dpl1, about_us as abt1

from about_us.views import about_us
from blogs.views import blog1
from data_analysis.views import data_analysis
from deep_learning.views import deep_learning
urlpatterns = [
    path('admin/', admin.site.urls),
    # 1.
    # path('',v1.machine_learning),
    # path('dl/',v1.deep_learning),
    # path('about/',v1.about_us),
    # path('blogs/',v2.blog1)
    # 2.
    path('',ml),
    path('dpl1/',dpl1),
    path('about1/',abt1),
    path('blg/',blog1),
    path('about/',about_us),
    path('dpl/',deep_learning),
    path('analysis/',data_analysis),
]
