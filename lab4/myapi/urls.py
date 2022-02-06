from rest_framework import routers
from django.urls import path, include
from .views import StudentList,student_detail

from studentsapp.models import Student

router = routers.DefaultRouter()
router.register(r'Student', StudentList)
urlpatterns = [
    path('', include(router.urls)),
    path('detail/<int:std_id>/', student_detail),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
