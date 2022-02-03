"""lab4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from studentsapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home_page),
    path('login/', login_page),
    path('register', register_page),
    path('', welcome_page, name='welcomepage'),
    path('home(?<idd>)', delete_student, name='DeletePage'),
    path('home?<idu>', UpdateStudent.as_view(), name='UpdatePage'),
    path('trackshome',Tracksinsertview.as_view(),name='Trackshomepage'),
    path('trackshome(?<tr_id>)', delete_track, name='DeleteTrack'),
    path('trackshome?<tid>', UpdateTrack.as_view(), name='UpdateTrack'),
]
