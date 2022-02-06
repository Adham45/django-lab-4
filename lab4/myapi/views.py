from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from studentsapp.models import Student
from .serializers import StudentSerializer


class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, std_id):
    try:
        student = Student.objects.get(std_id=std_id)
    except Student.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
